import spacy
from pathlib import Path
import random
from tqdm import tqdm
from trainingdata import *

def soldiers():

	model = None
	output_dir = Path("E:\\chatbot with spacy")
	n_iter = 100

	if model is not None:
		nlp = spacy.load(model)
	else:
		nlp = spacy.blank("en")

	if 'ner' not in nlp.pipe_names:
		ner = nlp.create_pipe("ner")
		nlp.add_pipe(ner, last=True)
	else:
		ner = nlp.get_pipe("ner")
	for _, annotation in TRAIN_DATA:
		for ent in annotation.get('entities'):
			ner.add_label(ent[2])
	other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
	with nlp.disable_pipes(*other_pipes):  # only train NER
		optimizer = nlp.begin_training()
		for itn in range(n_iter):
			random.shuffle(TRAIN_DATA)
			losses = {}
			for text, annotations in tqdm(TRAIN_DATA, desc= "Going through intense training."):
				nlp.update(
					[text],  # batch of texts
					[annotations],  # batch of annotations
					drop=0.35,  # dropout - make it harder to memorise data
					sgd=optimizer,  # callable to update weights
					losses=losses)
			print(losses)
	for text, _ in TRAIN_DATA:
	 		doc = nlp(text)
	 		print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
	 		print('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in doc])
	if output_dir is not None:
		Training_data = Path(output_dir)
		if not Training_data.exists():
			Training_data.mkdir()
		nlp.to_disk(Training_data)
		print("Saved model to", Training_data)
soldiers()

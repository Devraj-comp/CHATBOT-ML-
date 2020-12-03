from answer import *
question_block = ['what','where','how','when','who']
names_recognised = ['dbg','ss','brj','kj','ss','bkb','dt','pmp','rj','db','am','drm','bp']
#print("Nebula: ") 	
def question(*args):
	k = 0
	question_word = str(args[0])
	if (args[2]=="your" or args[2]=="nebula" or args[2]=="YOU"):
		about_me(question_word)
	name_word = str(args[1])
	#print(name_word)
	for i in question_block:
		if (question_word==i):
			#print("this is the question block {} ".format(args))
			for j in names_recognised:
				if(name_word==j):
					k=1
					break
				else:
					k = 2
		if(k==1):
			#print("I know this person.")
			answer(args[0],args[1])	
			break
		else:
			continue
		#for i in question_block:
		#	if(question_word.capitalize()!=i):
		#		print("Is this even a question?")
			

def about_me(question):
	if (question=='what'):
		print("I am a chatbot. I help to provide some information on some topic on KU.")
	elif(question == "who"):
		print("I am a chatbot.")
	elif(question == "how"):
		print("I help by providing information which is stored in my database.")
	elif(question=="where"):
		print("I was born in Allen Maharjan's computer.")
	print("You are asking {} question about Nebula".format(question))


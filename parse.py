def parse(*args):
	new_word = ""
	for i in args:
		for j in range(len(i)):
			if(i[j]=="?" or i[j]=='.' ):
				break
			else:
				new_word += i[j] 
	new_sentence= new_word.lower()
	return new_sentence

def name_parse(name):
	initials = []
	for i in name.split(" "):
		initials.append(i[0])
		new_name = ''.join(initials)
	print(new_name)
	return new_name




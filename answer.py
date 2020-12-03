def answer(*args):
	question = args[0]
	name = args[1]
	answers = open('Answers.txt','r')
	line = answers.readlines() 
	if (name == 'ss'):
		if(question=='who'):
			print(line[4])
		elif(question == 'where'):
			print(line[5])
		elif(question == 'how'):
			print(line[6])
	if (name == 'dbg'):
		if(question=='who'):
			print(line[8])
		elif(question == 'where'):
			print(line[9])
		elif(question == 'how'):
			print(line[10])
	if (name == 'brj'):
		if(question=='who'):
			print(line[0])
		elif(question == 'where'):
			print(line[1])
		elif(question == 'how'):
			print(line[2])
	if (name == 'kj'):
		if(question=='who'):
			print(line[12])
		elif(question == 'where'):
			print(line[13])
		elif(question == 'how'):
			print(line[14])
	if (name == 'bkb'):
		if(question=='who'):
			print(line[20])
		elif(question == 'where'):
			print(line[21])
		elif(question == 'how'):
			print(line[22])
	if (name == 'dt'):
		if(question=='who'):
			print(line[24])
		elif(question == 'where'):
			print(line[25])
		elif(question == 'how'):
			print(line[26])
	if (name == 'pmp'):
		if(question=='who'):
			print(line[28])
		elif(question == 'where'):
			print(line[29])
		elif(question == 'how'):
			print(line[30])
	if (name == 'rj'):
		if(question=='who'):
			print(line[32])
		elif(question == 'where'):
			print(line[33])
		elif(question == 'how'):
			print(line[34])

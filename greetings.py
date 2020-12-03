import random
def greetings(name):
    greetings_reply = ['Hello', 'Hi', 'Namaste']
    greetings_random = random.SystemRandom()
    #joining_tuple = ' '.join(args,)
    print(greetings_random.choice(greetings_reply), "{}".format(name.capitalize()))
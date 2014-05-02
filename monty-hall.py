import random

'''
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?
'''

# stay strategy clearly guesses right 1 out of 3 times
# but test the switch strategy
for n in xrange(10000):
    prize = random.randint(1,3)
    guess = random.randint(1,3)
    

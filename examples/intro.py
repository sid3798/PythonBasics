#this programs randomly gives an output
import random

toss_list = ('Head','Tails')
randomstudent = random.randint(1,12)
toss = random.choice(toss_list)
print("Lucky Student : {}".format(randomstudent))
input("Enter any Key...")
print(toss)


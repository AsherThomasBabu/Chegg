import random

guess_for_limit = 0.00 # Enter your guess here

def partsum(k):
    temp = 1/((k+1)*(k+2)*(k+3))
    return temp

sum =0
for i in range (random.randint(0,1000)):
    sum += partsum(i)

print(sum)


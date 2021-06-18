import random

randomlist = []
for i in range(0,10):
    n = random.randint(1,15)
    randomlist.append(n)

t_all = tuple(randomlist)
print("Tuple of 10 Random Numbers: {}".format(tuple(randomlist)))

t_a = t_all[:3]
print("Tuple of first 3 numbers: {}".format(t_a))

t_b = t_all[-3:]
print("Tuple of last 3 numbers: {}".format(t_b))

con_tup = t_a+t_b
print("Two tuples concatinated: {}".format(con_tup))

sort_con_tup = sorted(con_tup)
print("Two tuples concatinated and sorted: {}".format(sort_con_tup))




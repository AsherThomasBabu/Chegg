list_1 = [2,5,7,8]
list_2 = [1,2]

part_a = [(i*2)+1 for i in list_1]
print("part a: {}".format(part_a))

part_b = [i+1 for i in list_1 if i%2==0]
print("part b: {}".format(part_b))

part_c = [[i,i+1] for i in list_1]
print("part c: {}".format(part_c))

part_d = [[i,j] for i in list_1 for j in list_2]
print("part d: {}".format(part_d))

part_e = [[i+j for j in list_2] for i in list_1]
print("part e: {}".format(part_e))
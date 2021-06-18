j_list = []
print("Please Enter Jean's scores one by one")
for i in range(4):
    j_list.append(input("Enter a Score: "))
print("Jean's Score: {}".format(j_list))

k_list = []
print("Please Enter Kayla's scores one by one")
for i in range(4):
    k_list.append(input("Enter a Score: "))
print("Kayla's Score: {}".format(j_list))

c_list = []
print("Please Enter Connie's scores one by one")
for i in range(4):
    c_list.append(input("Enter a Score: "))
print("Connie's Score: {}".format(j_list))

all_scores = [j_list[:],k_list[:],c_list[:]]

print("All Scores: {}".format(all_scores))

for i in range(len(all_scores)):
    je = all_scores[i]
    for j in range(len(je)):
        je[j] = int(je[j]) + 1


print("All Scores after extra point: {}".format(all_scores))

for i in range(len(all_scores)):
    je = all_scores[i]
    for j in range(len(je)):
        je.sort()


print("All Scores after sorting: {}".format(all_scores))
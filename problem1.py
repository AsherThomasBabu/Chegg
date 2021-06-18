marklist = []
for i in range(5):
    marklist.append(input("Enter a Test Score: "))

print("All Scores:{}".format(marklist))
print("Students who scored below 60 get 10 points extra")

marklist_copy = marklist.copy()

for i in range(len(marklist_copy)):
    if int(marklist_copy[i])<60:
        marklist_copy[i] = int(marklist_copy[i])+10

print("All Scores: {}".format(marklist_copy))

for i in range(len(marklist)):
    if int(marklist_copy[i]) != int(marklist[i]):
        print("Old Score: {} New Score: {}".format(str(marklist[i]),str(marklist_copy[i])))
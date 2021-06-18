def emails():
    email_list=[]
    count = int(input("How many usernames will be inputed? "))
    for i in range(count):
        email_list.append(input('Enter Username #{} '.format(i+1))+"@g.cofc.edu")
    Output_string = "Emails : "
    for i in range(count):
        if(i == count-1):
            Output_string = Output_string + email_list[i]
        else:
            Output_string = Output_string + email_list[i]+", "


    print(Output_string)

def count_words():
    count = count = int(input("How many sentances will be inputed? "))
    for i in range(count):
        sentance = input("Enter Sentance: ")
        words = sentance.split()
        number_of_words = len(words)
        print("the sentance {} has {} words".format(sentance,number_of_words))

def word_avg():
    sentance = input("Enter Sentance: ")
    words = sentance.split()
    word_lengths = []
    for i in range(len(words)):
        word_lengths.append(len(words[i]))
    average_len = round(sum(word_lengths)/len(word_lengths),1)
    print("the sentance {} has an average word length of {}".format(sentance, average_len))

word_avg()


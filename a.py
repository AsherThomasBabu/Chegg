import os
path = 'D:/' 
text_files = [f for f in os.listdir(path) if f.endswith('.txt')]

print(text_files)

for p in text_files:
    with open("D:/"+p) as myfile:
     if 'password_' in myfile.read():
         print("File {} Contains the Passwords".format(p))
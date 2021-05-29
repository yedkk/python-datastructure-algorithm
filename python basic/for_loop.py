# This program is to read popular name from txt and give rank of the name
# Author Kangdong Yuan

# set the list

boy_name = []
girl_name = []

# open the file

with open("D:\\BoyNames.txt", "r") as boy_file:

# get the name from file
    for lines in boy_file.readlines():
        lines= lines.strip("\n")
        boy_name.append(lines)

# open the file

with open("D:\\GirlNames.txt","r") as girl_file:

# get the name from file
    for lines in girl_file.readlines():
        lines = lines.strip("\n")
        girl_name.append(lines)

# ask the name from user

name = input("Enter a name to see if it is a popular boys or girls name: ")

#set a wile loop

while name != "stop":

# check the name from list

    if name in girl_name:

# find the position from list

        rank1 = girl_name.index(name)+1
        print("The "+name+" is a popular girl name and is ranked "+str(rank1))
    else:
        print(name+ " is not a popular girl name")
    if name in boy_name:
        rank2 = boy_name.index(name)+1
        print("The "+name+" is a popular boy name and is ranked "+str(rank2))
    else:
        print(name+ " is not a popular boy name")

# ask user again

    name = input("Enter a name to see if it is a popular boys or girls name: ")





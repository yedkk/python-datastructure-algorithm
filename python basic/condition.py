# This program is to read popular name from txt and give rank of the name
# This program was rewrite by using function method
# Author Kangdong Yuan

# set the function to read the number from file
def getNamesList(file_name):

# Setting an empty list
    file_name_list = []
    with open("D:\\"+file_name+".txt", "r") as file_name_open:

# Writing the names into list
        for lines in file_name_open.readlines():
            lines = lines.strip("\n")
            file_name_list.append(lines)
        file_name = file_name_list
    return file_name

# Set the function
def checkName(name):

# get the list from function
    BoyNames = getNamesList("BoyNames")
    GirlNames = getNamesList("GirlNames")
    if name in GirlNames:

# find the position from list

        rank1 = GirlNames.index(name)+1
        print("The "+name+" is a popular girl name and is ranked "+str(rank1))
    else:
        print(name + " is not a popular girl name")
    if name in BoyNames:
        rank2 = BoyNames.index(name)+1
        print("The "+name+" is a popular boy name and is ranked "+str(rank2))
    else:
        print(name + " is not a popular boy name")

name = input("Enter a name to see if it is a popular boys or girls name: ")

#set a wile loop
while name != "stop":
    checkName(name)
    name = input("Enter a name to see if it is a popular boys or girls name: ")




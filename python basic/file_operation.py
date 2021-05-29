# This program is for read the random numbers from file and calculate the number and sum of random numbers
# Author: Kangdong Yuan

# set the variables
total = 0
counter = 0

# open the file
with open("D:\\random.txt", "r") as myfile:

# get the number from file
    for lines in myfile.readlines():
        lines = lines.strip("\n")

# get the sum and number
        total = int(lines) + total
        counter = counter + 1

# print it to user
        print(lines)
print("The total of the number is: "+str(total))
print("The file contained "+str(counter) +" numbers.")

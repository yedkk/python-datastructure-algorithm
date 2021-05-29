#This progroms want to get user's weight and height and calculate their then tell then the situation of their bmi
#First get the wieght and height of the user
#Second calculate the bemi throgh formula
#Third decide the situation of their bmi

# Author Kangdong Yuan

#Get the input of the height and the weight
height=float(input("Enter your height in inches: "))
weight=float(input("Enter your weight in pounds: "))

#Use the formula to get the bmi
bmi = weight*703//height**2

#Print the bmi for the user
print("Your BMI is "+str(bmi))

#Decide the bmi situation of bmi by range tha given by website
#And print the result of situation for users
if bmi >=18.5 and bmi <=25.0:
    print("Your BMI indicates that you are optimal wieght")
elif bmi <18.5:
    print("Your BMI indicates that you are underwieght")
elif bmi >25.0:
    print("Your BMI indicates that you are overwieght")

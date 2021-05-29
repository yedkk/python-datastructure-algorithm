# This program is to get the seconds from users and calculate the falling distance
# Author name: Kangdong Yuan

print("This program tells you how far will fall in number of seconds.")

# get the number from user
time = int(input("Enter the falling time in seconds :"))

# set the function
def falling(n):
    falling_distance = float(1/2*9.8*n**2)
    return falling_distance

# set the while loop to cancel the number below 0
while time > 0:

# use the function
    print("The distance of object will fall in "+str(time)+" seconds, is "+ str(falling(time)) +" meters.")
    time = int(input("Enter the falling time in seconds :"))

# This program is to get the temperature and wind speed from users and return windchill.

# Author: Kangdong Yuan

print("This program calculate the windchill from the fahrenheit and the wind speed.")

# Setting the variables

temp = int(input("Enter the fahrenheit temperature: "))
wind = int(input("Enter the wind speed: "))

# creating the function to calculate the windchill

def windchill(t,w):
    wind_chill = 35.74 + 0.6215 * t - 35.75 * w**0.16 + 0.4275 * t * w**0.16
    return wind_chill

# Printing the wind chill

print("The windchill is "+str(round(windchill(temp, wind),1)))

# Asking the users whether continue the program

decision = str(input("Would you like to calculate another windchill enter \"y\" or \"n\" ."))

# Setting the while loop for continuing program

while decision == "y":
    temp = int(input("Enter the fahrenheit temperature: "))
    wind = int(input("Enter the wind speed: "))
    print("The windchill is "+str(round(windchill(temp, wind),1)))

# Asking the user again whether continue this program

    decision = str(input("Would you like to calculate another windchill enter \"y\" or \"n\" ."))

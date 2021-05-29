# This program is to get the number and return average number to user
# Author: Kangdong Yuam

# Define the function to calculate the average
def calculateAverage(sum, count):
    total_Average = sum/count
    return total_Average

# Set the variable value
error1 = False

# Set the while loop for error exception
while error1 == False:

# Try the ZeroDivisonError and ValueError
    try:
        num = int(input("Enter a positive number to total or a negative number to calculate average: "))
        total_num = 0
        num_count = 0
        error1 = True
    except ValueError:
        print("What you entered was not a valid number. try again.")
        

error2 = False


# Set the while loop for second try
while error2 == False:

# Try the ZeroDivisonError and ValueError
    try:
        while num >= 0:
            total_num = total_num + num
            num_count = num_count + 1
            try:
                num = int(input("Enter a positive number to total or a negative number to calculate average: "))
            except ValueError:
                print("What you entered was not a valid number. try again.")
        error2 = True
        print(calculateAverage(total_num, num_count))
    except ZeroDivisionError:
        print("You did not enter any numbers to average")
    finally:
        try:
            num = int(input("Enter a positive number to total or a negative number to calculate average: "))
        except ValueError:
             print("What you entered was not a valid number. try again.")

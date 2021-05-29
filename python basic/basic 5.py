# This is the programs that convert Celsius to Fahrenheit
# I get the number of Celsius and print the list of convert

# Author Kangong Yuan

# Get the input from users
celsius = int(input("Enter the number of celsius temperatures to display: "))

# Print the title of list
print('Celsius\tFahrenheit')

# Set the variable
display_celsius = 0

# Convert the temperature and display it
while display_celsius <= celsius:
    fa_temperature = float(9/5*display_celsius+32)
    print(str(display_celsius) + '\t' + str(fa_temperature))
    display_celsius = display_celsius + 1


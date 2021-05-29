#This progrom want to get the number of package that user want to order and calculate the discount price and price after discount for user
#First get the number of package that user want to order
#Scond calculate the total price before the discount
#Third decide the rate of discount for user
#Fourth get the discount price by multiple the total price and discount rate
#Fifth get the price after discout by subtract discount price from total price

#Geting the number of packages
number=int(input("Enter the number of packages ordered: "))

#Calculating the price before discount
total_price = float(number*100)

#Set the discount variable first
discount = 0

#Deciding the rate of discount
discount_price = 0
if number >0 and number <=9:
    discount = 0
elif number>=10 and number <= 19:
    discount = 0.1
elif number >=20 and number <= 49:
    discount = 0.2
elif number >=50 and number <=99:
    discount = 0.3
elif number >= 100:
    discount = 0.4

#Calculating the price after the discount
discount_price = discount*total_price
total_price = total_price-discount_price

#Print the result for user
print("The total cost your purchase was $"+str(total_price)+" with a discount of $"+str(discount_price))

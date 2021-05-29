#Lab #5
#Due Date: 02/08/2019, 11:59PM
########################################
#                                      
# Name: Kangdong Yuan
# Collaboration Statement:             
#
########################################


class SodaMachine:
    '''
        >>> m = SodaMachine('Coke', 10)
        >>> m.purchase()
        'Product out of stock'
        >>> m.restock(2)
        'Current soda stock: 2'
        >>> m.purchase()
        'Please deposit $10'
        >>> m.deposit(7)
        'Balance: $7'
        >>> m.purchase()
        'Please deposit $3'
        >>> m.deposit(5)
        'Balance: $12'
        >>> m.purchase()
        'Coke dispensed, take your $2'
        >>> m.deposit(10)
        'Balance: $10'
        >>> m.purchase()
        'Coke dispensed'
        >>> m.deposit(15)
        'Sorry, out of stock. Take your $15 back'
    '''

# define the init function and variables
    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0
        self.depos = 0

# define the purchase
    def purchase(self):

# check the stock
        if self.stock != 0:

# if the deposit is enough return the soda
            if self.depos > self.price:
                chance = self.depos - self.price
                self.depos = 0
                self.stock = self.stock - 1
                return "{} dispensed, take your ${}".format(self.product,chance)

# if deposit is ok, return
            elif self.depos == self.price:
                self.depos = 0
                self.stock = self.stock - 1
                return "{} dispensed".format(self.product)

# if deposit is not enough
            else:
                need_depos = self.price - self.depos
                return "Please deposit ${}".format(need_depos)
        return "Product out of stock"

# define the deposit method
    def deposit(self, amount):

# if the stock is 0 ,plsu the amount
        if self.stock != 0:
            self.depos = self.depos + amount
            return "Balance: ${}".format(self.depos)

# if the deposit have some amount, plus those together
        else:
            self.depos = self.depos + amount
            return "Sorry, out of stock. Take your ${} back".format(self.depos)
# define the stock function
    def restock(self, amount):

# stock equal to the current stock plus amount
        self.stock = self.stock + amount
        return "Current soda stock: {}".format(self.stock)

    

class Line:
    ''' 
        Creates objects of the class Line, takes 2 tuples. Class must have 2 PROPERTY methods
        >>> line1=Line((-7,-9),(1,5.6))
        >>> line1.distance
        16.648
        >>> line1.slope
        1.825
        >>> line2=Line((2,6),(2,3))
        >>> line2.distance
        3.0
        >>> line2.slope
        'Infinity'
    '''

# define the init and set the two coords to list
    def __init__(self, coord1, coord2):
        self.plot1 = coord1
        self.plot2 = coord2

# calculate the distance between
        self.dis = (round(((self.plot1[0]-self.plot2[0])**2+(self.plot1[1]-self.plot2[1])**2)**0.5,3))

# if the slop is not Infinity, calculate it
        if self.plot1[0] != self.plot2[0]:

# if the plot1 is before, use p1-p2
            if self.plot1[0] > self.plot2[0]:
                self.line_slope = round(((self.plot1[1]-self.plot2[1])/(self.plot1[0]-self.plot2[0])),3)

# else the slope is p2-p1
            else:
                self.line_slope = round(((self.plot2[1]-self.plot1[1])/(self.plot2[0]-self.plot1[0])),3)

# return the Infinity
        else:
            self.line_slope = 'Infinity'

# use the property method to set the distance function and return
    @property
    def distance(self):
        return self.dis

# use the property method to set the slope function and return
    @property
    def slope(self):
        return self.line_slope
            
if __name__ == "__main__":
    import doctest
    doctest.testmod()

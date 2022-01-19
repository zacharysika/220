"""
Name: Zachary Sika
hw1.py

Problem: It calculates several different prices, areas, volumes,
and kilometers quickly and effectively
through user input.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input('What is the length?:'))
    width = eval(input('What is the width?:'))
    height = eval(input('What is the height?:'))
    volume = length * width * height
    print("The volume is", volume)

def shooting_percentage():
    shots = eval(input('How many shots did you take?:'))
    success = eval(input('How many shots did you hit the target with?:'))
    total = (success / shots) * 100
    print ('The total percent of shots made is', total)



def coffee():
    amount = eval(input('How many pounds of coffee would you like?'))
    shippingpp = 0.86
    order = 1.50
    coffeepp = 10.50
    total = (coffeepp + shippingpp) * amount + order
    print ("Your total for the coffee is: " , total)

def kilometers_to_miles():
    conversion = 1.61
    kilometers = eval(input('How many kilometers did you travel?'))
    miles = kilometers / conversion
    print ("The total number of miles is:", miles)




if __name__ == '__main__':
    pass
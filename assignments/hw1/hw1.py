"""
Name: Zachary Sika
hw1.py

Problem: It calculates several different prices, areas, volumes, and kilometers quickly and effectively
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
    length = int(input('What is the length?:'))
    width = int(input('What is the width?:'))
    height = int(input('What is the height?:'))
    volume = length * width * height
    print("The volume is", volume)

def shooting_percentage():
    shots = int(input('How many shots did you take?:'))
    success = int(input('How many shots did you hit the target with?:'))
    percent = success / shots
    print ('The total percent of shots made is', percent)



def coffee():
    cost = 0.86
    coffee = int(input('How much coffee would you like?'))
    total = coffee * cost
    print ("Your total for the coffee is: " + total)


def kilometers_to_miles():
    conversion = 1.61
    kilometers = int(input('How many kilometers did you travel?'))
    miles = kilometers / conversion
    print ("The total number of miles is:", miles)




if __name__ == '__main__':
    pass


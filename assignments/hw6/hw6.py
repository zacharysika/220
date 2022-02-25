"""
Name: Zachary Sika
hw6.py

Problem:  encodes messages and creates formatted currency from user input

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def cash_converter():
    integer = eval(input("enter an integer:"))
    value = integer * 1.00
    print("That is ${0:0.2f}".format(value))

def encode():
   characters = ""
   message = input("enter a message:")
   key = eval(input("enter a key:"))
   for i in range(len(message)):
       text_strings = message[i]
       characters = characters + chr((ord(text_strings) + key))
   print(characters)
def sphere_area(radius):
    pass
def sphere_volume(radius):
    pass


def sum_n(number):
    pass


def sum_n_cubes(number):
    pass


def encode_better():
    pass


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass

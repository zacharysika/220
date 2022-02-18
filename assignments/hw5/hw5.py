"""
Name: Zachary Sika
hw5.py

Problem: moves, splits, and separates items and string within a list created by user inputs

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name_entry = input("enter a name(first last):")
    name = name_entry.split()
    print(name[1]+",",name[0])
def company_name():
    website_entry = input("enter a domain:")
    website_name = website_entry.split(".")
    print(website_name[1])

def initials():
    roll_over = 0
    student_count = eval(input("how many students are in the class?"))
    for i in range(student_count):
        roll_over = roll_over + 1
        student = input("What is the name of student"+" "+str(roll_over)+"?").split()
        print(student[0][:1]+student[1][:1])


def names():
        pass
def thirds():
    count_over = 0
    number_sentences = eval(input("Enter the number of sentences"))
    for i in range(number_sentences):
        count_over = count_over + 1
        sentence = input("Enter sentence"+" " + str(count_over)+":")
        thirds = sentence[0::3]
    print(thirds)

def word_average():
    sum_count = 0
    sentence = input("enter a sentence:")
    for i in sentence.split():
        average = len(i)
        sum_count = average + sum_count
    average = (sum_count) / (len(sentence.split()))
    print (average)

def pig_latin():
    sentence_entry = str(input("enter a sentence to convert to pig latin")).split()
    for i in sentence_entry:
        print(i[1:]+ i[0]+ "ay",end = " ")
    print()


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass

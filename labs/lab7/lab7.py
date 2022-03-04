"""
Name: Zachary Sika
lab7.py

Problem: Creates an input file from the user input and creates an output
file after finding the average grade of the given student's grades and grade weights

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
def weighted_average():
    tally = 1
    infile = open("grades.txt",'w')
    outfile = open("avg.txt",'w')
    student_count = input("How many students are there?:")
    for i in range(int(student_count)):
        student_names = input("What is the student's name?:")
        print(student_names+":", file =infile)
        weights = input("What is the weight?:")
        weights_list = weights.split()
        for a in weights_list:
            weights_list = weights_list * tally
        grades = input("What is the grade?:")
        grades_list = grades.split()
        for b in grades_list:
            grades_list = grades_list * tally
        print(weights,grades, file = infile)
        summary = int(a)*int(b)/100
        print(student_names+":",summary, file=outfile)
    infile = open("grades.txt","r")
    outfile = open("avg.txt","r")
    file_read = infile.read()
    infile.close()
    outfile.close()



weighted_average()

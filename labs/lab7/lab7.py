"""
Name: Zachary Sika
lab7.py

Problem: Creates an input file from the user input and creates an output
file after finding the average grade of the given student's grades and grade weights

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
def weighted_average():
    grade_list = []
    infile = open("grades.txt",'w')
    outfile = open("avg.txt",'w')
    student_count = input("How many students are there?:")
    for i in range(int(student_count)):
        student_names = input("What is the students name?:")
        print(student_names + ":", file =infile)
        weights = int(input("What is the weight?:"))
        grades = int(input("What is the grade?:"))
        grade_list = grades.split()
        weights_list = weights.split()
        print(weights,grades, file = infile)
        if (weights>100):
            print("Error: The weights are more than 100.",file = outfile)
        elif(weights<100):
            print("Error: The weights are less than 100.",file = outfile)
        else:
            print()
    infile = open("grades.txt","r")
    outfile = open("avg.txt","r")
    file_read = infile.read(1)

    print(file_read)
    print(grade_list)



weighted_average()

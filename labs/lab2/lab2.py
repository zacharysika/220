"""
Zachary Sika
lab2.py
To calculate the RMS, the harmonic mean, and the geometric mean
I have created this with the help of Ms. Callahart
"""

def means():
    rms_acc = 0
    harmonic_acc = 0
    geo_acc = 1
    value_amount = eval(input("How many values would you like?"))
    for i in range(value_amount):
        value_x = eval(input("Enter a value for x: "))
        rms_acc = rms_acc + value_x ** 2
        harmonic_acc = harmonic_acc + 1/value_x
        geo_acc = geo_acc * value_x
    rms_mean = rms_acc / value_amount
    rms_mean = rms_mean ** (1/2)
    harmonic_mean = value_amount / harmonic_acc
    geometric_mean = geo_acc ** (1/value_amount)

    print(geometric_mean)
    print(harmonic_mean)
    print(rms_mean)

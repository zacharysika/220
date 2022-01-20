"""
Zachary Sika
lab1.py
To help a user calculate the monthly interest rates of their account
I have created this on my own
"""
def monthly_interest():
    annual_interest = eval (input("What is the annual interest rate?"))
    days = eval (input("What is the number of days in the billing cycle?"))
    pbalance = eval(input("What was the previous balance?"))
    payment = eval (input("What is the payment amount?"))
    dpayment = eval (input("What day was the payment made?"))

    interest = annual_interest / 12
    percentage_interest = interest / 100

    step1 = pbalance * days
    step2 = payment * (days - dpayment)
    step3 = step1 - step2
    daily_balance = step3 / days
    monthly_interest = daily_balance * percentage_interest

    print ("Your monthly interest is $", monthly_interest)
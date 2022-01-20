"""
Zachary Sika
lab1.py
To help a user calculate the monthly interest rates of their account
I have created this on my own
"""

interest = eval (input("What is the interest rate?"))
days = eval (input("What is the number of days in the billing cycle?"))
pbalance = eval(input("What was the previous balance?"))
payment = eval (input("What is the payment amount?"))
dpayment = eval (input("What day was the payment made?"))

percentage_interest = interest / 100

step1 = pbalance * days
step2 = payment * (dpayment - days)
step3 = step1 - step2
daily_balance = step3 / days
monthly_interest = daily_balance * percentage_interest





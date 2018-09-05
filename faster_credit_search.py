
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:55:23 2018

@author: arpanpain
"""
balance = int(input("enter the loan ammount:"))
annualInterestRate = float(input("enter the interest decimals:"))
months_paid = int(input("enter months to be paid: "))
lowerBound = balance / months_paid
monthlyInterestRate = annualInterestRate/12.0
upperBound = (balance * (1 + monthlyInterestRate) ** months_paid) / months_paid


def monthlyPayoff(lowestPayment , balance):
    """
        input: lowestPayment(float)
                balance(float)
        output: if debt is paid return "done"
                if debt is positive return "up"
                else return "down"
    """
    monthsRemaining = months_paid
    remainingBalance = balance
    while monthsRemaining > 0 :
        unpaidBalance = balance - lowestPayment
        remainingBalance = unpaidBalance + unpaidBalance * (annualInterestRate / 12.0)
        balance = remainingBalance
        monthsRemaining -= 1
    remainingBalance = round(remainingBalance , 2)
    if remainingBalance == 0:
        return "done"
    elif remainingBalance > 0 :
        return "up"
    else:
        return "down"
        
def searchPayoff( balance , lowerBound , upperBound):
    """
        input: balance(int)
                lowerBound(float): lowerBound of the search region
                upperBound(float) : upperbound of the search region 
        output: if monthlyPayoff return "done"
                return lowestPayment
                else use bisection search to find the lowest Payment
                
    """
    lowestPayment = (upperBound + lowerBound) /2
    flag = monthlyPayoff(lowestPayment , balance)
    if flag == 'done':
        return lowestPayment
    elif flag == 'up':
        lowerBound = lowestPayment
    else:
        upperBound = lowestPayment
    return searchPayoff(balance , lowerBound , upperBound)
    
        
print("Lowest Payment:",round(searchPayoff(balance , lowerBound , upperBound) , 2)) 


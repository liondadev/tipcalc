"""
    TipCalc
    Calulate tips and split the check dynamically
"""
import math

check = float(input("Check Price: "))
tipPercentage = float(input("Tip Percentage: "))
numPeople = float(input("Splitting People: "))

def calcTip(total, percentage):
    return (total * (percentage / 100)) + total

def split(total, ways):
    return round(total / ways)

print(split(calcTip(check, tipPercentage), numPeople))

from tkinter import *
from tkinter import messagebox
import mysql.connector

# creating a function to calculate Profit that
# accepts the cost price(cp) and selling price(sp) as arguments
def calculateProfit(cp, sp):
   # formula for calculating profit
   resultProfit = (sp - cp)
   # returning the resulting profit
   return resultProfit
# creating a function to calculate Loss that
# accepts the cost price(cp) and selling price(sp) as arguments
def calculateLoss(cp, sp):
   # formula for calculating loss
   resultLoss = (cp - sp)
   # returning the resultant loss.
   return resultLoss
# input cost price
cost_price = 500
# input selling price
selling_price = 1000
# checking whether the selling price is equal to the cost price
if selling_price == cost_price:
   # printing Neither profit nor loss if the condition is true
   print("Neither profit nor Loss")
# checking whether the selling price is greater than the cost price
elif selling_price > cost_price:
   # Calling calculateProfit function by passing cost price and selling price
   # as arguments and printing profit if the condition is true
   print("The Profit is", calculateProfit(cost_price, selling_price))
else:
   # Else calling calculateLoss function by passing cost price and
   # selling price as arguments and printing Loss
   print("The Loss is", calculateLoss(cost_price, selling_price))
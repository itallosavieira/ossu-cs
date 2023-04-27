# -*- coding: utf-8 -*-

# Part B: Saving, with a raise
# Background
# In Part A, we unrealistically assumed that your salary didn’t change. But you are an MIT graduate, and
# clearly you are going to be worth more to your company over time! So we are going to build on your
# solution to Part A by factoring in a raise every six months.
# In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery). Modify
# your program to include the following
# 1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
# 2. After the 6th month, increase your salary by that percentage. Do the same after the 12
# th
# th
# month, the 18 month, and so on.
# Write a program to calculate how many months it will take you save up enough money for a down
# payment. LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the
# required down payment percentage is 0.25 (or 25%). Have the user enter the following variables:
# 1. The starting annual salary (annual_salary)2
# 2. The percentage of salary to be saved (portion_saved)
# 3. The cost of your dream home (total_cost)
# 4. The semiannual salary r aise (semi_annual_raise)
# Hints
# To help you get started, here is a rough outline of the stages you should probably follow in writing your
# code:
# ● Retrieve user input.
# ● Initialize some state variables. You should decide what information you need. Be sure to be
# careful about values that represent annual amounts and those that represent monthly amounts.
# ● Be careful about when you increase your salary – this should only happen after the 6th, 12th, 18th
# month, and so on.
# Try different inputs and see how quickly or slowly you can save enough for a down payment. Please
# make your program print results in the format shown in the test cases below.
# Test Case 1
# >>>
# Enter your starting annual salary: 120000
# Enter the percent of your salary to save, as a decimal: .05
# Enter the cost of your dream home: 500000
# Enter the semiannual raise, as a deci mal: .03
# Number of months: 142
# >>>
# Test Case 2
# >>>
# Enter your starting annual salary: 80000
# Enter the percent of your salary to save, as a decimal: .1
# Enter the cost of your dream home: 800000
# Enter the semiannual raise, as a deci mal: .03
# Number of months: 159
# >>>
# Test Case 3
# >>>
# Enter your starting annual salary: 75000
# Enter the percent of your salary to save, as a decimal: .05
# Enter the cost of your dream home: 1500000
# Enter the semiannual raise, as a deci mal: .05
# Number of months: 261
# >>>


def calculateMonthlyPortion(value):
    return value / 12


def calculateMonthlySavingsRate(current_savings, monthly_rate):
    return current_savings * monthly_rate


def calculateCurrentSavings(current_savings, monthly_savings, monthly_rate):
    return monthly_savings + calculateMonthlySavingsRate(current_savings, monthly_rate)


def getUserInputs():
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))
    
    return annual_salary, portion_saved, total_cost, semi_annual_raise


def calculateMonthsToSave(current_savings, dpp, monthly_rate, semi_annual_raise):
    total_months = 0
    
    while(current_savings < dpp.calculateDownPaymentValue()):
        if (total_months != 0 and total_months % 6 == 0):
            dpp.setNewAnnualSalary(semi_annual_raise)
            
        current_savings += calculateCurrentSavings(current_savings, dpp.calculateMonthlySavedValue(), monthly_rate)
        total_months +=  1
        
    return total_months
    

class DownPaymentPlanner:

    def __init__(self, annual_salary, portion_saved, total_cost, portion_down_payment):

        self.annual_salary = annual_salary
        self.portion_saved = portion_saved
        self.total_cost = total_cost
        self.portion_down_payment = portion_down_payment

    def getAnnualSalary(self):
        return self.annual_salary
    
    def getMonthlySalary(self):
        return calculateMonthlyPortion(self.annual_salary)

    def getPortionSaved(self):
        return self.portion_saved

    def getTotalCost(self):
        return self.total_cost

    def getDownPaymentPortion(self):
        return self.portion_down_payment

    def calculateDownPaymentValue(self):
        return self.getTotalCost() * self.getDownPaymentPortion()

    def calculateMonthlySavedValue(self):
        return calculateMonthlyPortion(self.getAnnualSalary()) * self.getPortionSaved()
    
    def setNewAnnualSalary(self, semi_annual_raise):
        self.annual_salary += self.annual_salary * semi_annual_raise


annual_salary, \
portion_saved, \
total_cost, \
semi_annual_raise = getUserInputs()


portion_down_payment = 0.25
annual_rate = 0.04
monthly_rate = calculateMonthlyPortion(annual_rate)


dpp = DownPaymentPlanner(
        annual_salary,
        portion_saved,
        total_cost,
        portion_down_payment)


current_savings = 0
total_months = calculateMonthsToSave(current_savings, dpp, monthly_rate, semi_annual_raise)


print("Number of months:", total_months)
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 23:16:34 2021

@author: Jalaj
"""


annual_salary= float(input('Enter your annual salary: '))
portion_saved= float(input('Enter the portion to be saved in decimal: '))
monthly_savings= annual_salary/12*portion_saved

semi_annual_raise = float(input('Enter semi-annual-Raise:'))


total_cost= float(input('Enter the cost of your dream home:'))
portion_down_payment = 0.25
down_payment= total_cost*portion_down_payment

current_savings = 0.0
months=0.0
r= 0.04

while current_savings <= down_payment:
    current_savings+= monthly_savings + (current_savings*r)/12
    months +=1
    
    if months%6 == 0:
        annual_salary+= annual_salary*semi_annual_raise
        monthly_savings= annual_salary/12*portion_saved
    
print(int(months))
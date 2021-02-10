# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 22:38:51 2021

@author: Jalaj
"""

annual_salary= float(input('Enter your annual salary: '))
portion_saved= float(input('Enter the portion to be saved in decimal: '))
monthly_savings= annual_salary/12*portion_saved


total_cost= float(input('Enter the cost of your dream home:'))
portion_down_payment = 0.25
down_payment= total_cost*portion_down_payment

current_savings = 0.0
months=0.0
r= 0.04

while current_savings <= down_payment:
    current_savings+= monthly_savings + (current_savings*r)/12
    months +=1
    
print(int(months))

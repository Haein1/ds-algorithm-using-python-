# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 09:48:34 2021

@author: Administrator
"""

'''(STEP ONE: a clear problem statement):
Let us say your expense for every month are listed below,
    January - 2200
    February - 2350
    March - 2600
    April - 2130
    May - 2190
Create a list to store these monthly expenses and using that find out,

    1. In Feb, how many dollars you spent extra compare to January?
    2. Find out your total expense in first quarter (first three months) of the year.
    3. Find out if you spent exactly 2000 dollars in any month
    4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    5. You returned an item that you bought in a month of April and
    got a refund of 200$. Make a correction to your monthly expense list
    based on this
    
(STEP TWO: input, output, process):
    process:
        1. Initialize your_expense to [2200, 2350, 2600, 2130. 2190]
        2. Initialize extra_expense to (your_expense[1]-your_expense[0])
        3. Initialize first_quarter_expense to (your_expense[0] + your_expense[1] + your_expense[2])
        4. for i in range(0:len(your_expense)):
            if your_expense[i] == 2000:
                Initialize month_2000 to (i+1)
        5. your_expense.insert(5, 1980)
        6. your_expense[3] -=  200
        
        7.display:
            (1)"In Feb, how many dollars you spent extra compare to January? ", extra_expense
            (2)"your total expense in first quarter (first three months) of the year: ", first_quarter_expense
            (3)"if you spent exactly 2000 dollars in any month(True:other numbers;False:-1 )? ", month_2000
            (4)"June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list:", your_expense
            (5)"You returned an item that you bought in a month of April and
    got a refund of 200$. Make a correction to your monthly expense list
    based on this: ", your_expense

(STEP THREE: DESIGN AT LEAST FOUR TEST):


(STEP FOUR: WRITE THE ALGORITHM INTO PSEUDOCODE):
     these pseudocodes are displayed following the symbol #
     DONE        
'''

#1. Initialize your_expense to [2200, 2350, 2600, 2130. 2190]
your_expense = [2200, 2350, 2600, 2130, 2190]

#2. Initialize extra_expense to (your_expense[1]-your_expense[0])
extra_expense = your_expense[1]-your_expense[0]
#(1)"In Feb, how many dollars you spent extra compare to January? ", extra_expense
print("In Feb, how many dollars you spent extra compare to January? ", extra_expense)  

#3. Initialize first_quarter_expense to (your_expense[0] + your_expense[1] + your_expense[2])
first_quarter_expense = your_expense[0] + your_expense[1] + your_expense[2]
#(2)"your total expense in first quarter (first three months) of the year: ", first_quarter_expense
print("your total expense in first quarter (first three months) of the year: ", first_quarter_expense)

#4. for i in range(0:len(your_expense)):
            # if your_expense[i] == 2000:
            #     Initialize month_2000 to (i+1)
# month_2000 = 0
# for i in range(len(your_expense)):     
#     if your_expense[i] == 2000:
#         month_2000 = i+1 
if 2000 in your_expense:
    month_2000 = True
else:
    month_2000 = False
       
#(3)"if you spent exactly 2000 dollars in any month(True:other numbers;False:-1 )? ", month_2000
print("if you spent exactly 2000 dollars in any month(True:other numbers;False:-1 )? ", month_2000)        


#5. your_expense.insert(5, 1980)
your_expense.insert(5,1980)
#(4)"June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list:", your_expense
print("June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list:", your_expense)

#6. your_expense[3] -=  200
your_expense[3] -=  200
#(5)"You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this: ", your_expense
print("You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense listbased on this: ", your_expense)
#7.display:

 




# #(4)"June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list:", your_expense
# print("June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list:", your_expense)






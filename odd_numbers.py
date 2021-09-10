# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 16:09:03 2021

@author: Administrator
"""

'''(STEP ONE: a clear problem statement):
    Create a list of all odd numbers between 1 and a max number.
    Max number is something you need to take from a user using input() function
    
(STEP TWO: input, output, process):
    input: for max_number : 999
    process: 
        prompt for max_number with "Enter your max number: "
    display: 
        all odd numbers between 1 and a max number.
        
        
(STEP THREE: DESIGN AT LEAST FOUR TEST):
    input:
        for max_number: 999
    expected display:
        as you can see
        
        
(STEP FOUR: WRITE THE ALGORITHM INTO PSEUDOCODE):
     these pseudocodes are displayed following the symbol #
     DONE
     
(STEP FIVE: WRITE THE TRUE CODE)
        
            


'''
#1.initialize an empty list called odd_list
odd_list = []

#2. initialize max_number to an input function
# prompt for max_number with "Enter your max number: "
#convert it to int
max_number = int(input("Enter your max number: "))

'''
3. 
for num in range(max_number+1):
    if num % 2 == 1:
        odd_list.append(num + ' ')
        
'''
for num in range(max_number+1):
    if num % 2 == 1:
        odd_list.append(num)

#4.display:
    #print(odd_list)
print(odd_list)


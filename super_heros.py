# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 15:46:32 2021

@author: Administrator
"""

'''(STEP ONE: a clear problem statement):
    You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)



'''
heros=['spider man','thor','hulk','iron man','captain america']

#1. Length of the list
length = len(heros)
print(length)
print("--------------------")

#2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
print("--------------------")

#3. You realize that you need to add 'black panther' after 'hulk',
   #so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
i = heros.index('hulk')
heros[i+1] = 'black panther'
print(heros)
print("888888888888888888888888888888888888")

#4. Now you don't like thor and hulk because they get angry easily :)
   # So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   # Do that with one line of code.
#heros = [hero for hero in heros if hero == 'thor' or hero == 'hulk' replace(hero, 'doctor strange')]
heros[1:3] = ['doctor strange']
# s[i:j] = t   slice of s from i to j is replaced by the contents of the iterable t
print(heros)

print("*******************************************************")

#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)
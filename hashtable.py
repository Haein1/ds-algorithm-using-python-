# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 13:52:23 2021

@author: Administrator
"""

'''Try to achieve the hashmap/hashtable in python
actually it is the implementation of dictionary in python

'''

#create a class called HashTable:
class HashTable:
    
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    #achieve a __setitem__ function
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
    
        '''t['March 6'] = 900
        why change add to __setitem__ ?
            wanna use my dic like this t['March 6'] = 900
                rather than t.add(key, value)
        
        '''
    #achieve a __getitem__ function
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    #use to delete the value with a key called 'key'
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        
    
'''create a function called __init__, with a parameter called self,
        
        #define the biggest number that your container can include
        self.Max = 100
        #create a container called arr, put self.MAX None into it
        self.arr = [None for i in range(self.MAX)]

'''
    
#for __init__


'''create a function to help yout get the hash function, with two paramater: self, key
The function will help you get the unique index position in the memory of your computer

assign 0 to h
for every char in key(one of your parameter):
    assign the ASCII value of this char to h
    (use  ord() function to get your ASCII value of each char)

'''
    
#for get_hash ()          
        

'''define a function called add, with three parameters: self, key, value

use get_hash(key) function to get the unique index in memeory, assign it to the variable h

assgn the value to self.arr[h]


'''
    
# for add()    

'''define a function called get, with two parameters: self, key
use get_hash(key) function to get the unique index in memeory, assign it to the variable h

return self.arr[h]



'''
#for get()    



'''Test:
    

'''
t = HashTable()
# t.arr
#print(t.arr) # outut t before add any value into it
t['March 6'] = 900
t['Semp 12'] = 800
#print(t.arr)
a = t['March 6']
b = t['Semp 12']

#delete the value with the key called 'Semp 12'
del t['Semp 12']
print(t.arr)
# print(a)
# print(b)

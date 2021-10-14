# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:22:29 2021

@author: Administrator
"""
from collections import deque
class Stack:
    def __init__(self):
        self.container= deque()
    def push(self, val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)
    def print_in_order(self):
        for e in self.container:
                print(e)
                
                
                
def reverse_string(your_string):
    s = Stack()
    for e in your_string:
        s.push(e)
        
    reversed_string = ''
    while not s.is_empty():
        reversed_string += s.pop()
    return reversed_string
     

if __name__ == "__main__":
    print(reverse_string("We will conquere COVID-19"))
    print(reverse_string("Huang Shimu"))
     
#     def reverse_string(self, your_string):
#         self.container = your_string
        
#         reversed_string = ''
#         i = -1
#         while i >= (-len(self.container)):
#             reversed_string += self.container[i]
#             i -= 1
#         print(reversed_string)
        
# #test the stack class
# s = Stack()

# # s.push("We will conquere COVID-19")
# # s.push(2)
# # s.push(3)
# # s.push(4)
# s.reverse_string("We will conquere COVID-19")
# s.print_in_order()
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 08:58:32 2021

@author: Administrator
"""

'''Write a function in python 
that checks if paranthesis in the string are balanced or not.
 Possible parantheses are "{}',"()" or "[]". 
 Use Stack class from the tutorial.

'''
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def size(self):
        return len(self.container)
    def is_empty(self):
        return len(self.container) == 0

def is_match(ch1, ch2):
    std_match ={
        '}':'{',
        ')':'(',
        ']':'['
        }
    return std_match[ch1] == ch2;

def is_balanced(your_string):
    s = Stack()
   
    
    
    for ch in your_string:
        if ch == '{' or ch == '(' or ch == '[':
            s.push(ch)
        if ch == '}' or ch == ')' or ch == ']':
            if s.size() == 0:
                return False;
            if not is_match(ch, s.pop()):
                return False;
    return (s.size() == 0);
            
    
    

    

if __name__ == "__main__":
    
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
    
    
    
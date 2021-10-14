# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 21:02:55 2021

@author: Administrator
"""


'''Write a function in python 
that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.


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

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

'''
This part surprises me actually, 
which means that I never thought I can use dict to express this info
'''
def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    '''This function finds whether the parentheses in the special string are balanced.
    
    para: a string
    
    '''
    
    #initialize an instance of Stack class, called stack
    stack = Stack()
    
    '''
    for every elements in the string:
        if the element equals "(" or '{' or '[':
            add this element into your stack
        if the element equals ')' or '}' or ']':
            if the element appears at the beginning:
                which means there is no '(' or '[' or '{' that can pair with it
                so, let this function return False directly
            
            if is_match(ch, stack.pop()) is not true:
                return False directly
            
    Finally,
        return stack.size()==0
        (because every time you use is_match() above, the last element will be deleted,
         which means the number of elements in stack will decrease by one every time.
         
         if they are not match, it will return False alove;
         if it pops out all the elements in the stack, 
         which means every one find their soulmates))
    
    
    '''
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
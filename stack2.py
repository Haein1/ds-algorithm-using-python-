# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 20:19:52 2021

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
    def popleft(self):
        return self.container.popleft()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)
    def print_in_order(self):
        for e in self.container:
                print(e)
                
def is_balanced(your_string):
    your_string_list = list(your_string)
    s = Stack()
    j = 0
    while j < len(your_string_list):
        s.push(your_string_list[j])
        j += 1
        
    #s.push(your_string_list)
    
    std_paren_pair = ['{}', '()','[]']
    not_std_pair = ['{','}','[',']','(',')']
    your_s_list = []
    while s.size() >= 2:
        p = str(s.pop())
        lp = str(s.popleft())
        if (p in not_std_pair) and (lp in not_std_pair):
            test_pair = lp + p
            your_s_list.append(test_pair)
    
    
    is_paren_balanced = True
    for tp in your_s_list:
        if (tp in std_paren_pair):
            is_paren_balanced = True
            
        else:
            is_paren_balanced = False
    
    return is_paren_balanced
    
    
    


if __name__ == "__main__":
    # print(is_balanced("({a+b})"))  #True
    # print(is_balanced("))((a+b}{")) #False
    # print(is_balanced("((a+b))"))  #True
    # print(is_balanced("))"))       #False
    
    '''Needed to be solved
    
    '''
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))#True
    
    # s1 = Stack()
    # s1.push(1)
    # s1.push(2)

    # print(s1.popleft())
    
    
                
                
                
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:27:18 2021

@author: Administrator
"""

'''Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010
Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

You also need to add front() function in queue class that can return the front element in the queue.

'''

#achieve a python queue class first
from collections import deque
class Queue:
    def __init__(self):
        self.container = deque()
    def enqueue(self, val):
        self.container.appendleft(val)
    def dequeue(self):
        return self.container.pop()
    def size(self):
        return len(self.container)
    def is_empty(self):
        return (len(self.container) == 0)
    def front(self):
        return self.container[-1]



def produce_binary(n):
    binary_container = Queue()
    front = binary_container.enqueue('1')
    
    for i in range(n):
        front = binary_container.front()
        print('    ', front)
        
        binary_container.enqueue(front+'0')
        binary_container.enqueue(front+'1')
        
        binary_container.dequeue()
        
if __name__ == "__main__":
    produce_binary(10)        




        
# test whether the Queue class is right or not
# q1 = Queue()
# q1.enqueue('pizza')
# q1.enqueue('banana')
# print(q1.container)
# print(q1.size())
# print(q1.front())
# print(q1.dequeue())    #pizza
# print(q1.size())
# # q1.dequeue()
# # print(q1.size())
# print(q1.is_empty())        
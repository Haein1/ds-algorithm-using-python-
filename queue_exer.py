# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 08:22:20 2021

@author: Administrator
"""

'''Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
Use this video to get yourself familiar with multithreading in python

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.

'''
from collections import deque
import time
import threading

#create a queue class
class Queue():
    def __init__(self):
        self.container = deque()
    def enqueue(self, val):
        self.container.appendleft(val)
    def dequeue(self):
        return self.container.pop()
    def is_empty(self):
        return (len(self.container) == 0)
    def size(self):
        return len(self.container)
#create a producer function
def producer(order_queue):
    
    #order_que = Queue()
    for e in order_queue.container[0]:
        print("Produced: ", e)
        time.sleep(0.5)
    
    
#create a consumer function        
def consumer(order_queue):
    time.sleep(1)
    for e in order_queue.container[0]:
        if not order_queue.is_empty():
            print("Consumed:", e)
            time.sleep(2)
    
        
        
    
    
    
            
orders = ['pizza','samosa','pasta','biryani','burger']
order_queue = Queue()
order_queue.enqueue(orders)
# produced_o = producer(orders)
t = time.time()
producer_t = threading.Thread(target=producer, args = (order_queue,))
consumer_t = threading.Thread(target = consumer, args = (order_queue,))
# producer(order_queue)
# consumer(order_queue)

producer_t.start()
consumer_t.start()

producer_t.join() #wait until producer_t is done
consumer_t.join() #wait until consumer_t is done

print("Time spent:", time.time()-t)
print("All orders are done!")
        
# test whether the Queue class is right or not
# q1 = Queue()
# q1.enqueue('pizza')
# q1.enqueue('banana')
# print(q1.container)
# print(q1.size())
# print(q1.dequeue())    #pizza
# print(q1.size())
# q1.dequeue()
# print(q1.size())
# print(q1.is_empty())

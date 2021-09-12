# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 11:32:40 2021

@author: Administrator
"""


'''
Define a class called Node, 
    with two default parameters: data = None; next = None
    
'''

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

'''
Define a class called LinkedList,

(1)THE FIRST METHOD:
    
    set one data attribute called head that is the first Node of this linkedlist, 
    initialize it to None
    

'''        
class LinkedList:
    def __init__(self):
        self.head = None #the first node in the linkedList
        
    '''(2)THE SECOND METHOD:
         define a method called print with the self parameter:
             if the first node of this LinkedList is empty:
                 print("Your LinkedList is empty.")
                 finish this method
                 
             itr = self.head
             nodes = ''
             as long as itr is not empty:
                 nodes += (str(itr.data) + '---->') 
                 itr = itr.next
                 
             print(nodes)
                 
         
         
    
    '''
    def print(self):
        if self.head == None:
            print("Your LinkedList is empty.")
            return
        
        itr = self.head #itr rerpesents a node in the linkedlist
        all_nodes = ''
        while itr:
            all_nodes += (str(itr.data) + '-->')
            itr = itr.next
            
        print(all_nodes)
        
    
    '''(3)THE THIRD METHOD:
        define a method called insert_at_end with a parameter called data:
            if this linkedlist is empty:
                self.head = Node(data, None)
                finish this method
                
            itr = self.head # at this time, itr represents a node in the linkedlist
            
            as long as the node that is represented by itr now is not empty:
                continue to look for the next node
                
            (when I jump up the finding jouney, it means that I have already found
             the last node, 
             which means that right now itr represents the last node,
             so, if I wanna insert a new node into this linkedlist,
             what I need to do is to make the pointer of the last node that I found just now
             point to my new node)
        
    
    
    '''
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        
    '''(THE FOURTH METHOD:)
    define a method called insert_at_beginning with a parameter called data:
        self.head = Node(data, self.head)
    
    '''
    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)
        
        
    '''(THE FIFTH METHOD:)
    define a method called get_length:
        (1)initialize a variable called count, 
        which has a counting function
        
        (2)initialize itr to the first node of the linkedlist
        
        (3) 
        as long as the node that itr represents is not empty:
            count += 1
            itr = itr.next
            
        (4)
        make this method return count
    
    '''
    def get_length(self):
        count = 0
        
        itr = self.head
        
        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    
    '''(THE SIXTH METHOD: insert a node at the given index)
    define a method called insert_at with two parameters, index & data:
        (1) use if to decide whether the given index is valid:
          if not valid:
              print('Invalid index')
    
        (2)
        if the given index equals 0:
            insert_at_beginning()
            
        (3)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            count += 1 
            itr = itr.next
        
    '''
    def insert_at(self, index, data):
        if (index < 0) or (index > self.get_length()):
           
            raise Exception('Invalid index')
            '''
            Notice that there is a difference between use print and raise;
            if you use print here, 
            this method will display the info 'Invalid index',
            but, this method will execute these following codes 
            
            Conversely,
            if you use raise keyword,
            this method will stop to execute the following codes.
            Meanwhile,
            it will also give you the error info
            
            '''
            
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr  = self.head
        
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1
            
    '''(THE SEVENTH METHOD: WIPE OUT ALL THE DATA IN THE LINKEDLIST,
    INSERT A LIST OF DATA)
    define a method called insert_values with a list type parameter:
        make the linkedlist empty
        
        for every data in datalist:
            self.insert_at_end(data)
    
    '''
    def insert_values(self, datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)
    
    
    
    
    '''(THE EIGHTH METHOD: REMOVE AT)
    define a method called remove_at with a parameter called index:
        
    
    '''
    def remove_at(self, index):
        if (index < 0) or (index > self.get_length()):
            raise Exception('Invalid index')
            
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
        itr = itr.next
        count += 1
            
            
        
            
        
        
            
        
        
        
            
if __name__ == "__main__":
    #pass
    my_linked_list = LinkedList()
    my_linked_list.insert_at_end(2)
    
    my_linked_list.insert_at_beginning(1)
   
    my_linked_list.print()
    length1 = my_linked_list.get_length()
    print('the length of my linkedlist: ', length1)
    my_linked_list.insert_at_end(4)
    
    my_linked_list.insert_at_beginning(0)
    
    length = my_linked_list.get_length()
    
    my_linked_list.print()
    print('the length of my linkedlist: ', length)
    
    print('---------------------------------------------')
    my_linked_list.insert_at(3, 3)
    my_linked_list.print()
    
    print('************************************************')
    datalist = ['114','115','116','117','118']
    my_linked_list.insert_values(datalist)
    my_linked_list.print()
    
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    my_linked_list.remove_at(1)
    my_linked_list.print()
    
    
        
        
       

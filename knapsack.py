#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 10:22:26 2018

@author: arpanpain

The strategy used is value/ weight ratio

just change the __lt__() method to use other strategies

"""

class item(object):
    """
    creates an item object which can be comparable using values
    """
    def __init__(self , value , weight , name):
        '''
        creates an object with value , weight , name of the object
        '''
        self.value = value
        self.weight = weight
        self.name = name
        
    def __lt__(self, other):
        '''
        input: self , other -- item object
        output : True or False depending upon the comparision result
        helpful in case of sorting 
        '''
        return self.getValue() < other.getValue()
    
    def __str__(self):
        '''
        helpful in case of printing what objects are in the knapsack 
        '''
        return self.getName() + " , value" + str(self.getValue())
    
    def getValue(self):
        return self.value
    
    def getWeight(self):
        return self.weight
    
    def getName(self):
        return self.name
    
    
# test code for knapsack optimisation problem
shop_items = []
gold = item(25 , 12 , "golden necklace")
diamond = item(100 , 20 , "diamond")
silver = item(23 , 12 , "silver earrings")
shop_items.append(gold)
shop_items.append(silver)
shop_items.append(diamond)
max_knapsack_capacity = 40
shop_items.sort()
shop_items.reverse()
knapsack = []
weight = 0
for i in shop_items:
    if i.getWeight() + weight <= max_knapsack_capacity:
        knapsack.append(i)
        weight += i.getWeight()

total = 0
for i in knapsack:
    print(i)
    total += i.getValue()
    
print("total value of the knapsack",total)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 22:07:17 2018

@author: arpanpain
"""

def steps(steps_left , count = 0 , memo = {}):
    # if no steps left return count +1
    if steps_left ==0 :
        return count + 1
    #if steps_left is negative return 0
    elif steps_left < 0:
        return count
    #search in memo if memo[steps_left] exists then return stored result
    elif memo.get(steps_left , 0) != 0:
        return memo.get(steps_left , 0)
    #else
    else:
        #try one step value
        with1 = steps(steps_left - 1)
        #try two step value
        with2 = steps(steps_left - 2)
        #store the result for steps_left as a key
        memo = store(with1 + with2 , steps_left , memo)
        #return sum of one step and two step
        return with1 + with2
    

def store(count , s_l , memo):
    try:
        memo[s_l] += count
    except:
        memo[s_l] = count
    return memo
#steps(4)
#!/usr/bin/env python

# https://leetcode.com/problems/two-sum/description/

#_________________________________TASK__________________________________  

# Given an array of integers nums and an integer target. 
# Return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution.
# You may not use the same element twice.
# You can return the answer in any order.

import time

def Two_Sum(X, Y):
    count_i = 0
    count_j = 0
    success=0
    temp_sum = 0 

    for i in X:
        # print ("Index", count_i, ": Value", i)
        count_j = 0
        for j in X:
            if(i != j):
                temp_sum = i + j
                if (temp_sum == Y):
                    print ("(", count_i, ",", count_j, ")")
                    success += 1
            count_j += 1
            
        count_i += 1
    if success == 0:
        print ("No Combination of Two Values in the Array sum to", Y)

A = (2, 3, 5, 6)
print("We Have The Following Array: ", A)
print("Input An Integer and I will output which 2 indexes from the Array add up to the integer")
Desired_Sum = int(input("Enter Integer for Desired Sum: "))
Two_Sum(A, Desired_Sum)
            


#!/usr/bin/env python
import math
import time

# https://leetcode.com/problems/palindrome-number/

#_________________________________TASK__________________________________  

# Given an integer x, return true if x is a palindrome, and false otherwise.
# Palindrome is a number thats the same forwards and backwards

X=int(input("Enter Potential Palindrome: "))
Y=X
# print(X)
temp_mod=10
temp_value=0
Pal_Array=[]
Pal_Int=0

while X > 1:
    temp_value=X%(temp_mod)
    X-=temp_value
    Pal_Array.append(int((temp_value*10)/(temp_mod)))
    temp_mod*=10

length_Pal_Array = len(Pal_Array)
factor=10**(length_Pal_Array-1)

for i in Pal_Array:
    length_Pal_Array-=1
    Pal_Int+=int(i*factor)
    factor=factor/10

if(Y==Pal_Int):
    print("Success!!!", Y, "is a Palindrone")
    print(Y, "Equals", Pal_Int)
else:
    print("Fail!!", Y, "is Not a Palindrome")
    print(Y, "Does Not Equal", Pal_Int)




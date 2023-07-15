#!/usr/bin/env python
import math
import time

# https://leetcode.com/problems/palindrome-number/

#_________________________________TASK__________________________________  

# Given an integer x, return true if x is a palindrome, and false otherwise.

X=int(input("Enter Potential Palindrome: "))
Y=X
# print(X)
temp_mod=10
temp_value=0
Pal_Array=[]
Pal_Array_2=[]
Pal_Int=0



while X > 1:
    temp_value=X%(temp_mod)
    X-=temp_value
    Pal_Array_2.append(int((temp_value*10)/(temp_mod)))
    temp_mod*=10
    print("Removed Value: ", temp_value)
    print("Current Value of Potential Palindrome: ", X)
    Pal_Array.append(temp_value)


print(Pal_Array)
print(Pal_Array_2)
# print(len(Pal_Array))
length_Pal_Array = len(Pal_Array)
factor=10**(length_Pal_Array-1)
print("Factor: ", factor)



for i in Pal_Array_2:
    length_Pal_Array-=1
    print("i: ", i, "length of Pal Array: ", length_Pal_Array)
    Pal_Int+=int(i*factor)
    print("Current Value of Palindrome Test: ", Pal_Int)
    factor=factor/10

if(Y==Pal_Int):
    print("Success!!!", Y, "is a Palindrone")
    print(Y, "Equals", Pal_Int)
else:
    print("Fail!!", Y, "is Not a Palindrome")
    print(Y, "Does Not Equal", Pal_Int)



    # temp_value=X%(temp_mod)
    # Y-=temp_value
    # more_temp_value=temp_value
    # temp_mod*=10
    # more_temp_value=more_temp_value*factor
    # print("temp")
    # Pal_check+=temp_value
    # factor/=100
    # print("Current Value of Palindrome Test: ", Pal_check)

    
    


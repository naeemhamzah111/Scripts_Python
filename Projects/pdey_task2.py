#!/usr/bin/env python

def solution(A):

    sum_weight = 0
    max_weight = 5000
    count = -1

    for i in A:

        sum_weight += i
        count += 1

        if (sum_weight > max_weight):
            count -=1
            break

    print(count)

A = (4650, 150, 150, 150)
B = (500, 600, 700, 800)
C = (3000, 500, 200, 300, 200, 500, 700, 300)


solution(C)


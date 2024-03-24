import threading
import random as rand
import time
import os
from queue import LifoQueue

# What code does:
# Producer thread generates and stores random integers into an array that only stores 100 numbers.
# Producer thread generates MAX_COUNT (10000) integers where MAX_COUNT > BUFFER_SIZE

# • Producer thread randomly generates integers in the range of [LOWER_NUM; UPPER_NUM] and inserts each number to a bounded integer buffer (array) of length
# BUFFER_SIZE. The buffer is a stack, namely, the last inserted number will be removed
# first. Producer thread generates exactly MAX_COUNT integers, where MAX_COUNT >
# BUFFER_SIZE.
# • Producer thread must write all the generated numbers to the output file all.txt.
# • The first Customer thread removes only the even numbers from the top of the buffer (stack) and writes them to the file called odd.txt.
# • The second Customer thread removes only the odd numbers from the top of the buffer (stack) and writes them to the file called even.txt.
# • Note that Customer thread can read but not remove a number with wrong parity from the top of the buffer (stack).

# Constants
LOWER_NUM = 1
UPPER_NUM = 10000
BUFFER_SIZE = 100
MAX_COUNT = 10000

stack = []

# def reverse(lst):
#     startIndex = 0
#     endIndex = len(lst)-1

#     while endIndex > startIndex:
#             lst[startIndex], lst[endIndex] = lst[endIndex], lst[startIndex]
#             startIndex = startIndex + 1
#             endIndex = endIndex - 1

# Producer's task
# Producer thread must write all the generated numbers to the output file all.txt.
def producer():
    numList = []
    for i in range(MAX_COUNT):
        # time.sleep(1)
        numAll = str(rand.randint(LOWER_NUM, UPPER_NUM))
        numList.append(numAll)

        if len(stack) <= BUFFER_SIZE:
            stack.append(numAll)  

    with open('all.txt', 'w') as f:
        for j in numList:
            f.write(j)
            f.write('\n')
    


# Customer1's task
# removes only the even numbers from the top of the buffer (stack) and writes them to the file called odd.txt.
def customer1():
    startIndex = 0
    numOddList = []
    # print(stack)
    
    while startIndex < len(stack)-1:
        startIndex += 1
        num = (-1*startIndex)
        # Odd/Even filter
        if int(stack[num]) % 2 == 0:
            pass
        else:
            numOddList.append(stack[num])
    
    # print(numOddList)
    # for i in range(len(stack)-1, -1, -1):
    #     print (stack[i])
    
    with open('odd.txt', 'w') as f:
        for j in numOddList:
            f.write(j)
            f.write('\n')
        

# Customer2's task
# removes only the odd numbers from the top of the buffer (stack) and writes them to the file called even.txt.
def customer2():
    startIndex = 0
    numEvenList = []
    # print(stack)
    
    while startIndex < len(stack)-1:
        startIndex += 1
        num = (-1*startIndex)
        # Odd/Even filter
        if int(stack[num]) % 2 != 0:
            pass
        else:
            numEvenList.append(stack[num])
    
    # print(numOddList)
    # for i in range(len(stack)-1, -1, -1):
    #     print (stack[i])
    
    with open('even.txt', 'w') as f:
        for j in numEvenList:
            f.write(j)
            f.write('\n')

# main
producer()
customer1()
customer2()
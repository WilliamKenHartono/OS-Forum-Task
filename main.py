import threading
import random as rand
import time

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

# Buffering
buffer = []
lock = threading.Lock()
producer_finished = False
start_time = time.time()

# File Outputs
all_numbers_file = 'all.txt'
even_numbers_file = 'even.txt'
odd_numbers_file = 'odd.txt'

# Producer's task
# Producer thread must write all the generated numbers to the output file all.txt.
    
def producer():
    global producer_finished
    for i in range(MAX_COUNT):
        num = rand.randint(LOWER_NUM, UPPER_NUM)
        if len(buffer) < BUFFER_SIZE:
            buffer.append(num)
            with open(all_numbers_file, 'a') as file:
                file.write(f'{num}\n')
        time.sleep(0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003)
    producer_finished = True

# CustomerEven's task
# removes only the odd numbers from the top of the buffer and writes them to the file called even.txt.
def customerEven():
    while not producer_finished or buffer:
        with lock:
            if buffer and buffer[-1] % 2 == 0:
                evenNum = buffer.pop()
                with open(even_numbers_file, 'a') as file:
                    file.write(f'{evenNum}\n')

# CustomerOdd's task
# removes only the even numbers from the top of the buffer and writes them to the file called odd.txt.
def customerOdd():
    while not producer_finished or buffer:
        with lock:
            if buffer and buffer[-1] % 2 != 0:
                oddNum = buffer.pop()
                with open(odd_numbers_file, 'a') as file:
                    file.write(f'{oddNum}\n')
    
# main
producer_thread = threading.Thread(target=producer)
customer_even_thread = threading.Thread(target=customerEven)
customer_odd_thread = threading.Thread(target=customerOdd)


producer_thread.start()
customer_even_thread.start()
customer_odd_thread.start()

producer_thread.join()
customer_even_thread.join()
customer_odd_thread.join()


print("--- %s seconds ---" % (time.time() - start_time))
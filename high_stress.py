'''
Author: Qi7
Date: 2022-11-18 14:48:17
LastEditors: aaronli-uga ql61608@uga.edu
LastEditTime: 2022-11-18 15:32:19
Description: 
'''
import time
from random import *
import threading as th
from pytimedinput import timedInput

# define the countdown func.
def shutdown():
    global score
    print(f"Timeout! Score is {score}")
    time.sleep(15)
    exit()
    
# input time in seconds
# t = input("Enter the time in seconds: ")  

score = 0
t = 10 # 10 seconds per question
num_questions = 30 # 5 mins test. 10 questions per mintus
test_time = 300

cmd = input("Enter s to start the test, or q to exit:\n")
if cmd == "q":
    quit()


# 300 second
S = th.Timer(test_time, shutdown)
S.start()

while num_questions:
    print(f"current score: {score}")
    a, b = randint(1, 100), randint(1, 100)
    userText, timedOut = timedInput(f"{a} X {b} = ?\n", timeout=t)
    if(timedOut):
        print("Timeout!! score reset!")
        score = 0
    elif (int(userText) == a*b):
        print("correct!")
        score += 1
    else:
        print("Wrong answer! Score reset!")
        score = 0
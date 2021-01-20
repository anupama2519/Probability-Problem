# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 20:27:54 2021

@author: Anupama
"""
# Problem Statement:
#There is bag that contains 3 colours of ball (Red, Green & Blue).
#Numbers of ball count of each colours are A, B, and C respectively
#We will 3 picks and in each pick we will take 2 balls out and we won’t replace the 
#picked balls for subsequent picks or draws.
#We wanted to find out the probability of picking same of colour of balls in 3rd draw.


# Load required libraries:
import random

#Create a function to add no of balls of your choice:

def add_ball(A,B,C):
    colour = ['R','G','B']
    bag = []
    for i in colour:
        if i == 'R':
            for j in range(A):
                bag.append(i)
        elif i == 'G':
            for j in range(B):
                bag.append(i)
        else:
            for j in range(C):
                bag.append(i)
    return bag

# Choose the no of balls:
bag = add_ball(4,6,5)

# Create a function to remove balls from  bag:
    
def remove_ball(x):
    pick = random.choice(x)
    x.remove(pick)
    return pick, x

# As per the problem, remove 2 balls in each pick :
# Number of picks =3        
ball = []
cnt =0 
for draw in range(3):
    for i in range(2):
        pick, bag = remove_ball(bag)
        ball.append(pick)
    if draw == 2:
        if ball[4] == ball[5]:
            cnt +=1
            print("Probability of getting same colour balls: ",cnt/3)
        else:
            print("Sorry, Colour of balls in third pick are different. ")
        
print(cnt)       
print(ball)    
print(bag)


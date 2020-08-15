# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:12:19 2020

@author: lokesh
""" 
import turtle
import random

# setting turtles

p1 = turtle.Turtle()
p1.color('green')
p1.shape("turtle")
p1.penup()
p1.goto(-200,100)

p2=p1.clone()
p2.color("blue")
p2.shape("turtle")
p2.penup()
p2.goto(-200,-100)

# setting turtle's home

p1.goto(300,60)
p1.pendown()
p1.circle(40)
p1.penup()
p1.goto(-200,100)

p2.goto(300,-140)
p2.pendown()
p2.circle(40)
p2.penup()
p2.goto(-200,-100)

# setting dice
die = [1,2,3,4,5,6]

for i in range(20):
    if p1.pos()>= (300,100):
               print("Player One Wins!")
               break
                
    elif p2.pos()>= (300,-100):
               print("Player two Wins!")
               break
                
    else:
        p1_turn = input("Press Enter to roll the dice: ")
        d_out = random.choice(die)
        print(f"The outcome of dieroll is {d_out}")
        print("The numer of steps would be")
        print(20*d_out)
        p1.fd(20*d_out)
        
        p2_turn = input("Press Enter to roll the dice: ")
        d_out = random.choice(die)
        print(f"The outcome of dieroll is {d_out}")
        print("The numer of steps would be")
        print(20*d_out)
        p2.fd(20*d_out)



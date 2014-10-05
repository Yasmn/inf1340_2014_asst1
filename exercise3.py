#!/usr/bin/env python3

from random import choice
input ()

name = input("Enter your name : ")

print ("Rock breaks Scissors, Scissors cuts Paper, Paper beats Rock")
rps = ['r','p','s']
player1 = 0
player2 = 0

print ("R: Rock,      P: Paper,     S: Scissor")

user = input("Enter your choice among the three : ")
user = user.lower()

#Here is the choice()
py = choice(rps)
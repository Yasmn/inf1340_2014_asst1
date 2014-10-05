#!/usr/bin/env python3

#this is to designate the results for each entry
decide_rps = {}
decide_rps [("rock" "paper")] = 2
decide_rps [("rock" "scissors")] = 1
decide_rps [("rock" "rock")] = 0

decide_rps [("scissors" "paper")] = 1
decide_rps [("scissors" "rock")] = 2
decide_rps [("scissors" "scissors")] = 0

decide_rps [("paper" "scissors")] = 2
decide_rps [("paper" "rock")] = 1
decide_rps [("paper" "paper")] = 0


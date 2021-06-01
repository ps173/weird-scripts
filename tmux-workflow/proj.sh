#!/bin/sh
# so that I cna go to my folders quickly
cd $1
session="work"

tmux start-server

tmux new-session -d -s $session -n nvim 
tmux selectp -t 1 
tmux send-keys "nvim" C-m 

tmux new-window -t $session:1 -n server
tmux splitw -v -p 55
tmux send-keys "npm start" C-m 


# return to main nvim window
tmux select-window -t $session:0

tmux attach-session -t $session


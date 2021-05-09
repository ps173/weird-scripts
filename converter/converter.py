#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Webm converter for audio streams and video streams (can only convert 
# audio to audio and video to video) 

import subprocess
import sys

def convert_to_audio(filename):
    command = ['ffmpeg', '-i', filename , 'out.mp3']
    subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)

def convert_to_video(filename):
    command = ['ffmpeg', '-i', filename , 'out.mp4']
    subprocess.run(command,stdout=subprocess.PIPE,stdin=subprocess.PIPE)

def main():
    ask = input("what conversion do you want ? (mp3 or mp4 are option)")
    if ask == "mp4":
        file = input("what is file path ??\n")
        convert_to_video(file)
    if ask == "mp3":
        file = input("what is file path ??\n")
        convert_to_audio(file)

if __name__ == '__main__':
    main()

#!/usr/bin/python3
#script to alert myself every 25 minutes to rest my eyes

import time
import subprocess

count = 1500
while count > 0:
    print(f'Counting down . . . Remaining seconds left: {count} seconds . . .')
    time.sleep(1)
    count -= 1
    if count == 0:
        subprocess.Popen(
            ['cvlc', '/home/joe/Downloads/niceudes.mp3'])
        print('Look out your window right now!\n')
        # sleep the program for 40 seconds to rest eyes
        # alert again when time is up and restart counter
        time.sleep(40)
        subprocess.Popen(['cvlc', '/home/joe/Downloads/niceudes.mp3'])
        time.sleep(3)
        print('Restarting the program in 3 seconds . . .')
        count = 1500
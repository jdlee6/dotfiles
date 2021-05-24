#script to alert myself every 25 minutes to rest my eyes

import time
import subprocess
import playsound

mp3_path = '/Users/joe/Downloads/niceudes.mp3'

count = 1500
while count > 0:
    print(f'Counting down . . . Remaining seconds left: {count} seconds . . .')
    time.sleep(1)
    count -= 1
    if count == 0:
        playsound.playsound(mp3_path, False)
        print('Look away from your screen!\n')
        # sleep for 40 seconds to rest eyes
        # alert again when time is up and restart counter
        time.sleep(40)
        playsound.playsound(mp3_path, False)
        time.sleep(3)
        print('Restarting the program in 3 seconds . . .')
        count = 1500
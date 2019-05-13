from datetime import datetime
from random import randint
from time import sleep

odds=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

right_this_minute =datetime.today().minute

print(right_this_minute)
for i in range(5):
    pause_time=randint(1,10)
    print("random number generated is ",pause_time)
    sleep(pause_time)
    if right_this_minute in odds:
        print("odd minute")
    else:
         print("not odd minute")

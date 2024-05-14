import time 
import os

def countdown(seconds):
    elapsed_time = 0
    
    while elapsed_time < seconds:
        time.sleep(1)
        elapsed_time += 1
        time_left = seconds - elapsed_time
        
        seconds_left = time_left // 60
        minutes_left = time_left % 60
        
        print(f'{minutes_left}:{seconds_left}')
        
    print('RUN!')
countdown(10)
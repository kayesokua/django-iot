from helper_functions import *
import RPi.GPIO as GPIO
import time

def pour(motor) :
    pos = 80
    dc = degree_to_DC(pos)
    change_DC(motor,dc)
    
    
    
# def homing(motor):
#     pos = 180
#     dc = degree_to_DC(pos)
#     change_DC(motor,dc)
    
wrist = motor_setup(11)
# homing(wrist)                        
# pour(wrist)
# homing(wrist)


# clean_up(wrist)

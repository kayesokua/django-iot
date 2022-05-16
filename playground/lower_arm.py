from helper_functions import *
import RPi.GPIO as GPIO
import time

# def homing(motor):
#     pos = 120
#     dc = degree_to_DC(pos)
#     change_DC(motor,dc)


    
lower_arm = motor_setup(37)
# homing(lower_arm)

# clean_up(lower_arm)
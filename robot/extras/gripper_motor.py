from helper_functions import *
import time

def to_full_open(motor):
    pos = 60
    dc = degree_to_DC(pos)   
#     print(dc)
#     print(motor)
    change_DC(motor, dc)
    time.sleep(0.2)

def grab(motor):
#     for pos in range(50,-1,-1):
#         dc = degree_to_DC(pos)
#         change_DC(motor, dc)
#         print("current position: ",pos)
#         time.sleep(0.05)
    dc = degree_to_DC(0)
    change_DC(motor, dc)

from helper_functions import *

def pour(motor) :
    pos = 80
    dc = degree_to_DC(pos)
    change_DC(motor,dc)
    
def homing(motor):
    pos = 180
    dc = degree_to_DC(pos)
    change_DC(motor,dc)
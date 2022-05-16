from math import acos, atan, sqrt
from gripper_motor import *
from wrist_motor import *
from upper_arm import *
from lower_arm import *
from waist_motor import *
from helper_functions import *
# GPIO.setmode(GPIO.BOARD)

X = 26.2# desired X position of end-effector
Y = 0.0 # desired X position of end-effector
Z = 16.0 # desired X position of end-effector
a1= 16 #cm
a2= 11.4 #cm
a3= 14.8 #cm


r2 = sqrt(X*X+Y*Y) # equation 1

T1 = acos(((r2*r2)+(X*X)-(Y*Y))/(2*r2*X)) #equation 2

r1 = sqrt((Z-a1)*(Z-a1)+(r2*r2)) #equation 3

phi1 = atan((Z-a1)/r2) #equation 4

phi2 = acos(((a2*a2)+(r1*r1)-(a3*a3))/(2*a2*r1)) #equation 5

T2 = phi1+phi2 #radians #equation 6

phi3 = acos(((a3*a3)+(r1*r1)-(a2*a2))/(2*a3*r1)) #equation 7

T3 = 1.5708-phi2-phi3 #radians #equation 8

upper_arm_degree = 180-T3/3.14159*180.0-10
lower_arm_degree = T2/3.14159*180.0+10
waist_degree = T1/3.14159*180

print("r1:",r1,"r2:",r2,"Phi1:",phi1,"Phi2:",phi2,"Phi3:",phi3)
print("Theta 1: ", waist_degree, ". Theta 2: ", lower_arm_degree, "Theta 3: ", upper_arm_degree)
# 
# def homing():
#     turn(gripper,60)
#     turn(wrist,0)
#     turn(waist,0)
#     turn(lower_arm,120)
#     turn(upper_arm,150)
# motors = [gripper, wrist, upper_arm, lower_arm, waist]

def get_drink():
    turn(waist,waist_degree)
    turn(lower_arm,lower_arm_degree)
    turn(upper_arm,upper_arm_degree)
    stop_jittering(waist)
    stop_jittering(lower_arm)
    stop_jittering(upper_arm)
# get_drink()
to_full_open(gripper)
stop_jittering(gripper)
get_drink()
# 

time.sleep(1)
grab(gripper)

stop_jittering(gripper)
time.sleep(2)
# 
turn(lower_arm,60)
turn(upper_arm,105)
stop_jittering(lower_arm)
stop_jittering(upper_arm)
# turn(waist,180)
# turn(upper_arm,90)
# turn(lower_arm,20)
# 
# pour(wrist)
# turn(wrist,0)
# 
# for motor in motors:
#     stop_jittering(motor)












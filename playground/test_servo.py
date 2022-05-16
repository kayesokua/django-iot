# Write your code here :-)
import RPi.GPIO as GPIO
import time
from helper_functions import *
# GPIO.setmode(GPIO.BOARD)
pin1=15  
pin2=37

motor1 = motor_setup(pin1)
motor2 = motor_setup(pin2)




#motor1.ChangeDutyCycle(9.5)
#time.sleep(0.5)
#gripper 13 0 to 70
#lower 15 0 to 70


angle1 = 120
dc1 = degree_to_DC(angle1)
angle2 = 60
dc2 = degree_to_DC(angle2)

change_DC(motor1,dc1)
change_DC(motor1,dc2)
motor1.ChangeDutyCycle(dc1)
motor2.ChangeDutyCycle(dc2)
time.sleep(0.8)
motor1.ChangeDutyCycle(0)
motor2.ChangeDutyCycle(0)
time.sleep(1)


# 
# for degree in range(0,181,30):
#     dc = 1/18*(degree)+2
#     motor1.ChangeDutyCycle(dc)
#     time.sleep(0.2)
#     motor1.ChangeDutyCycle(0)
#     print("the degree turns to: ",degree)
#     time.sleep(0.5)
# 
# for degree in range(180,-1,-30):
#     dc = 1/18*(degree)+2
#     motor1.ChangeDutyCycle(dc)
#     time.sleep(0.2)
#     motor1.ChangeDutyCycle(0)
#     print("the degree turns to: ",degree)
#     time.sleep(0.5)
    




motor1.stop()
# motor2.stop()
GPIO.cleanup()
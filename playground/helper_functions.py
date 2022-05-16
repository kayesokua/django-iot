import RPi.GPIO as GPIO
import time


def motor_setup(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    motor = GPIO.PWM(pin, 50)
    motor.start(0)
    return motor

def degree_to_DC(degree):
    dc = 1/18*(degree)+2
    return dc

def change_DC(motor,dc):
    motor.ChangeDutyCycle(dc)
#     time.sleep(0.8)
#    motor.ChangeDutyCycle(0)
#    time.sleep(0.8)
def stop_jittering(motor):
    time.sleep(0.5)
    motor.ChangeDutyCycle(0)
    
#     time.sleep(0.8)
def turn(motor, degree) :
    dc = degree_to_DC(degree)
    change_DC(motor, dc)

def clean_up(motor):
    motor.stop()
    GPIO.cleanup()
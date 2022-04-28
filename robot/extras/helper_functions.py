import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

def motor_setup(pin):
    GPIO.setup(pin, GPIO.OUT)
    motor = GPIO.PWM(pin, 50)
    motor.start(0)
    return motor
    
def degree_to_DC(degree):
    dc = 1/18*(degree)+2
    return dc

def change_DC(motor,dc):
    motor.ChangeDutyCycle(dc)
    time.sleep(0.2)
    motor.ChangeDutyCycle(0)
    time.sleep(0.8)

def clean_up(motor):
    motor.stop()
    GPIO.cleanup()
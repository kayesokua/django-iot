import time
#from GPIOEmulator.EmulatorGUI import GPIO
import RPi.GPIO as GPIO

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

def test_range(motor):
    for degree in range(0,181,30):
        dc = degree_to_DC(degree)
        change_DC(motor,dc)
        print("the degree turns to: ",degree)


    for degree in range(180,-1,-30):
        dc = degree_to_DC(degree)
        change_DC(motor,dc)
        print("the degree turns to: ",degree)
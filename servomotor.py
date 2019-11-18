import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(03,GPIO.OUT)

pwm = GPIO.PWM(03.50)

pwm.start(0)

def rotateCycle():
    for i in range(4):
        GPIO.output(03,True)
        pwm.ChangeDutyCycle(7)
        sleep(1)
        GPIO.output(03,False)
        pwm.ChangeDutyCycle(0)

def move(time):
    for i in range(time):
        rotateCycle()

pwm.stop()
GPIO.cleanup()

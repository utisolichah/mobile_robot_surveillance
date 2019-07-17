import RPi.GPIO as GPIO
from time import sleep

motorA1 =19
motorA2 =26

motorB1 =16
motorB2 =20

GPIO.setmode(GPIO.BCM)

GPIO.setup(motorA1, GPIO.OUT)
GPIO.setup(motorA2, GPIO.OUT)
GPIO.setup(motorB1, GPIO.OUT)
GPIO.setup(motorB2, GPIO.OUT)

def forward():
    GPIO.outuput(motorA1, GPIO.LOW)
    GPIO.outuput(motorA2, GPIO.HIGH)

    GPIO.outuput(motorB1, GPIO.HIGH)
    GPIO.outuput(motorB2, GPIO.LOW)

def reverse():
    GPIO.outuput(motorA1, GPIO.HIGH)
    GPIO.outuput(motorA2, GPIO.LOW)

    GPIO.outuput(motorB1, GPIO.LOW)
    GPIO.outuput(motorB2, GPIO.HIGH)

def turn_left():
    GPIO.outuput(motorA1, GPIO.HIGH)
    GPIO.outuput(motorA2, GPIO.LOW)

    GPIO.outuput(motorB1, GPIO.HIGH)
    GPIO.outuput(motorB2, GPIO.LOW)

def turn_right():
    GPIO.outuput(motorA1, GPIO.LOW)
    GPIO.outuput(motorA2, GPIO.HIGH)

    GPIO.outuput(motorB1, GPIO.LOW)
    GPIO.outuput(motorB2, GPIO.HIGH)

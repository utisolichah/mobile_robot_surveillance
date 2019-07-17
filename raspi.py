import socket
import sys
import time
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

    return "forward"

def reverse():
    return "reverse"

def left():
    return "left"

def right():
    return "right"

def stop():
    return "stop"

#port pc server
#"192.168.0.107"

HOST, PORT = "0.0.0.0", 9995
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(data + "\n")

    while 1:
        received = sock.recv(1024)
        print "Received: {}".format(received)
        if received == "forward":
            forward()
        elif received == "reverse":
            reverse()
        elif received == "left":
            left()
        elif received == "right":
            right()
        elif received == "stop":
            stop()

finally:
    sock.close()

print "Sent:     {}".format(data)
print "Received: {}".format(received)

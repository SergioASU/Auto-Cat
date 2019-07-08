import RPi.GPIO as GPIO
import time
from Email import *
import datetime

class Motor:
    #its just how it goes
    def __init__(self, servoPin, htz,startAngle):
        self.email = Email(465,'Auto.Cat.Messaging@gmail.com','AutoCatProject')
        self.htz = htz
        self.servoPin = servoPin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servoPin, GPIO.OUT)
        self.p = GPIO.PWM(self.servoPin, self.htz)
        self.startAngle = startAngle
        self.p.ChangeDutyCycle(self.startAngle)
    def feed(self,toAngle,timeToRun):
        print("Feeding now")
        self.p.ChangeDutyCycle(toAngle)
        time.sleep(timeToRun)
        self.p.ChangeDutyCycle(self.startAngle)
        time.sleep(0.5)
        feedingMessage = 'Feeding complete on: ' + str(datetime.datetime.now())
        print(feedingMessage)
        self.email.sendEmail('sergio.c.842@gmail.com','Feeding Complete!')
        self.email.sendEmail('martin.c.842@gmail.com', 'Feeding Complete!')
        print("Feeding Complete")

    def end(self):
        self.p.stop()
        GPIO.cleanup()

import RPi.GPIO as GPIO
import time
class Motor:
    #its just how it goes
    def __init__(self, servoPin, htz,startAngle):
        self.servoPin = servoPin
        self.GPIO.setmode(GPIO.BCM)
        self.GPIO.setup(self.servoPIN, GPIO.OUT)
        self.p = GPIO.PWM(self.servoPIN, self.htz)
        self.startAngle = startAngle
        self.p.ChangeDutyCycle(self.startAngle)
    def feed(self,toAngle,timeToRun):
        print("Feeding now")
        self.p.ChangeDutyCycle(toAngle)
        time.sleep(timeToRun)
        self.ChangeDutyCycle(self.startAngle)
        time.sleep(0.5)
        print("Feeding Complete")

    def end(self):
        self.p.stop()
        self.GPIO.cleanup()

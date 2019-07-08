from Email import *
from Motor import *
import time
import schedule

def initialization():
    print("Auto-Cat initializing")
    email = Email(465,'Auto.Cat.Messaging@gmail.com','AutoCatProject')
    motor = Motor(21,50,5)
    #schedule.every(1).minutes.do(email.sendEmail,'sergio.c.842@gmail.com','This is a test')
    #schedule.every().day.at("22:19").do(email.sendEmail,'eliazar.d.842@gmail.com','hey :)')
    schedule.every(1).minutes.do(motor.feed,10,5)
    #Add any other initializing components here
    print("Auto-Cat initializing complete")

def main():
    #Call initilization function
    initialization()

    #loop forever
    while True:
        print('Auto-Cat running')
        schedule.run_pending()
        time.sleep(1)
    
#Call main function
main()

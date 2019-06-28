from Email import *
import time
import schedule

def initialization():
    print("Auto-Cat initializing")
    email = Email(465,'Auto.Cat.Messaging@gmail.com','AutoCatProject')
    #schedule.every().minutes.do(email.sendEmail,'sergio.c.842@gmail.com','This is a test')
    #Add any other initializing components here
    schedule.every().day.at("00:35").do(email.sendEmail,'martin.c.842@gmail.com','This is a test')
    print("Auto-Cat initializing complete")

def main():
    #Call initilization function
    initialization()

    #loop forever
    while True:
        print('Auto-Cat running')
        schedule.run_pending()
        time.sleep(1)

main()
        

from Email import *
import time
import schedule

def main():
    print("Auto-Cat initializing")
    email = Email(465,'Auto.Cat.Messaging@gmail.com','AutoCatProject')
    schedule.every(1).minutes.do(email.sendEmail,'sergio.c.842@gmail.com','This is a test')
    print("Auto-Cat initializing complete")
    
    while True:
        print('Auto-Cat running')
        schedule.run_pending()
        time.sleep(1)
    
main()

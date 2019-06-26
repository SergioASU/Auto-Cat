import smtplib, ssl

def main():
    print("Auto-Cat starting up")
    port = 465  # For SSL
    password = 'AutoCatProject'

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("Auto.Cat.Messaging@gmail.com", password)
        server.sendmail('Auto.Cat.Messaging@gmail.com', 'sergio.c.842@gmail.com', 'test')
        server.quit() 
main()

import smtplib, ssl

class Email:
    def __init__(self, port, fromEmail,fromEmailPassword):
        self.port = port
        self.fromEmail = fromEmail
        self.fromEmailPassword = fromEmailPassword
        self.context = ssl.create_default_context()
    
    def sendEmail(self, toEmail, message):
        print('Sending email')
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
            server.login(self.fromEmail, self.fromEmailPassword)
            server.sendmail(self.fromEmail, toEmail, message)
            server.quit()
            print('Email sent and server disconnected') 
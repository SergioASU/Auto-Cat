import smtplib

class SMS:
    carriers = {
	'att':    '@mms.att.net',
    'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
    }
    def __init__(self, carrier, number):
        self.carrier = carrier
        self.number = number
    def send(self,message):
        to_number = self.number.format(self.carriers[self.carrier])
        auth = ('**email**', '**password**')
        #Establish a secure session with gmail's outgoing SMTP server using your gmail account
        server = smtplib.SMTP( "smtp.gmail.com", 587 )
        server.starttls()
        server.login(auth[0], auth[1])
	    # Send text message through SMS gateway of destination number
        server.sendmail(auth[0],to_number,message)

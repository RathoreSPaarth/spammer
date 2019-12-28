##########PaarthSRathore##############paarthsinghrathore1@gmail.com###############


#https://docs.python.org/2/library/smtplib.html

import smtplib
  
#encapsulates connection 
spam = smtplib.SMTP('smtp.gmail.com', 587) 
  
#transport layer security
spam.starttls() 
  
#logging into senders email account
spam.login("enterYourEmail@here.com", "enterYourPassword") 
  
#message to be sent
message = "Enter your message123"
  
# sending the mail any number of times
for x in range(5):
     spam.sendmail("enterYourEmail@here.com", "enterReceiversEmail@here.com", message) 
  
#terminating the session 
spam.quit() 

##########PaarthSRathore##############paarthsinghrathore1@gmail.com###############

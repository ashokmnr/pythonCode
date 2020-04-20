
import smtplib

smtp_server = "smtp.com"
sender_email = "email"  
receiver_email = "email"

message = """\
Subject: Hi there

This message is sent from Python."""

try:
	server = smtplib.SMTP(smtp_server)
	server.ehlo()
	server.sendmail(sender_email, receiver_email, message)
	server.quit()
	print "Done. Sending Email" 
finally:
	print "Done. Sending Email" 

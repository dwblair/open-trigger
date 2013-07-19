import smtplib
 
to = 'abannigan@gmail.com'
gmail_user = 'donblair@gmail.com'
gmail_pwd = 'gmailcat1002'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
print header
msg = header + 'did this work? '
smtpserver.sendmail(gmail_user, to, msg)
print 'done!'
smtpserver.close()

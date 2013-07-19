import smtplib

to = 'donblair999@yahoo.com'
gmail_user = 'alerts@open-trigger.pvos.org'
gmail_pwd = 'opentriggercat999'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver = smtplib.SMTP("mail.open-trigger.pvos.org",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
print header
msg = header + 'how many fingerz]ssss?'
smtpserver.sendmail(gmail_user, to, msg)
print 'done!'
smtpserver.close()


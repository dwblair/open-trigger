
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from app import app
import os
from flask import Flask, render_template, send_from_directory, send_file, request, url_for, jsonify, redirect, Request, g

from cStringIO import StringIO
from werkzeug import secure_filename

SECRETKEY='bananas'

import smtplib
import datetime
import json, requests

@app.route("/mailer")
def mailer2():
    to = 'donblair999@yahoo.com'
    gmail_user = 'alerts@open-trigger.pvos.org'
    gmail_pwd = 'opentriggercat999'
    #smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver = smtplib.SMTP("mail.open-trigger.pvos.org",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
    #print header
    msg = header + 'how many fingerz]ssss?'
    smtpserver.sendmail(gmail_user, to, msg)
    #print 'done!'
    smtpserver.close()
    return "test"

@app.route("/")
def index():
    return "yep!"

@app.route('/checkStatus')
def checkStatus():
    recipient=request.args.get('recipient')
    secretKey=request.args.get('secretKey')
    feedID=request.args.get('feedID')
    timeout=1

    url = 'https://api.xively.com/v2/feeds/103261'
    data=requests.get(url=url, auth=('dwblair', 'cosmcat999'))
    #requests.get(url=url, params=params, timeout=timeout)
    binary = data.content
    xive = json.loads(binary)

    humidity = xive['datastreams'][0]['current_value']
    temp_ambient = xive['datastreams'][1]['current_value']
    temp_probe = xive['datastreams'][2]['current_value']

    dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
    timeNow=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    status = xive['status']

    if status=='live':
        message="FeedID "+feedID+" : temp=" + temp_ambient + " Celsius"
    else:
        message="Alert! FeedID "+feedID+" has stopped updating. This may mean sensor fail, internet disconnection, or electrical power out."

    to = recipient
    gmail_user = 'alerts@open-trigger.pvos.org'
    gmail_pwd = 'opentriggercat999'
    smtpserver = smtplib.SMTP("mail.open-trigger.pvos.org",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:'+ message+'\n'
    msg = header + 'Your feed generated an automatic alert on ' + timeNow + ' with the message:\n\n'+ message
    smtpserver.sendmail(gmail_user, to, msg)
    smtpserver.close()
    return "worked."


@app.route('/email')
def data():
    recipient=request.args.get('recipient')
    secretKey=request.args.get('secretKey')
    message=request.args.get('message')
  #  val1=request.args.get('val1')

    if secretKey==SECRETKEY:

        dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
        timeNow=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#        jsonR = jsonify(timestamp=timeNow,feedID=feedID,message=message)

        to = recipient
        gmail_user = 'alerts@open-trigger.pvos.org'
        gmail_pwd = 'opentriggercat999'
        #smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver = smtplib.SMTP("mail.open-trigger.pvos.org",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(gmail_user, gmail_pwd)
        header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:'+ message+'\n'
        #print header
        msg = header + 'Your feed generated an automatic alert on ' + timeNow + ' with the message:\n'+ message
        smtpserver.sendmail(gmail_user, to, msg)
        #print 'done!'
        smtpserver.close()
        return "Message sent to " + recipient + ' at ' + timeNow
        #return redirect(url_for('plot',feedID=feedID)) 
    else:
        return "You can't do that."

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')





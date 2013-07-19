
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



import smtplib

@app.route("/mailer")
def mailer2():
    to = 'donblair999@yahoo.com'
    gmail_user = 'donblair@gmail.com'
    gmail_pwd = 'gmailcat1002'
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
    print header
    msg = header + 'how many fingers?'
    smtpserver.sendmail(gmail_user, to, msg)
    print 'done!'
    smtpserver.close()
    return render_template('dragdrop.html')

#@app.errorhandler(413)
#def file_to_big(e):
#    return render_template('tooBig.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')





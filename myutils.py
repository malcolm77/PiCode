# from dropbox import DropboxOAuth2FlowNoRedirect

import json
import smtplib
import os
import glob
import dropbox

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def send_email_attachment(email_address,subject,text,attach):
    fromaddr = "malcolm.r.chalmers@gmail.com" 
    toaddrs  = email_address
    print("[INFO] Emailing to {}".format(email_address))
    message = 'Subject: {}\n\n{}'.format(subject, text)

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    # set attachments
    if attach <> 'nil': 
        files = glob.glob(attach)
        print("[INFO] Number of images attached to email: {}".format(len(files)))
        for f in files:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(f)
                )
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
                msg.attach(part)

    # Credentials (if needed) : EDIT THIS
    username = "malcolm.r.chalmers@gmail.com"
    password = "Kippa-Ring"

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()

def send_email(email_address,subject,text):
    fromaddr = "malcolm.r.chalmers@gmail.com" 
    toaddrs  = email_address
    print("[INFO] Emailing to {}".format(email_address))
    message = 'Subject: {}\n\n{}'.format(subject, text)

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    # Credentials (if needed) : EDIT THIS
    username = "malcolm.r.chalmers@gmail.com"
    password = "Kippa-Ring"

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()

def uploadtodropbox(localfilename,dropboxfilename):
    # this uploads given file to dropbox
    client = dropbox.Dropbox("ztAk1m6GGfoAAAAAAAAAbxrjRJ4I3t35xsY8FqParQiFhtagC8nZCUahvNdSD21S")
    client.files_upload(open(localfilename, "rb").read(), dropboxfilename)
    

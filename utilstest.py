from myutils import send_email_attachment, send_email, uploadtodropbox
from os.path import basename
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('filename', help='path to file to send')
args = parser.parse_args()
print("localpath: "+args.filename)
print("dropbox path: " + "/Temp"  +"/"+basename(args.filename))

# send email with an attachment
# send_email(to_email_address, subject, message, attachment(s))
# send_email_attachment('malcolmchalmers@hotmail.com','This is a test','message body',args.filename)

# send email without an attachment
# send_email(to_email_address, subject, message)
# send_email('malcolmchalmers@hotmail.com','This is a test','message body')

# upload file to dropbbox
# uploadtodropbox (localfilename, dropboxfilename)
# uploadtodropbox ('/home/pi/python/utils.py','/Temp/utils.py')
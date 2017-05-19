# Import smtplib for the actual sending function
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.nonmultipart import MIMENonMultipart
from email.mime.text import MIMEText
# For guessing MIME type
import mimetypes
import csv
#import Urllib
# Import the email modules we'll need
import email
import email.mime.application

arr=[]
i=0
#upload the database file
with open('book1.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            arr.append([])
            arr[i].append(row[0])   #column 1 contains company name
            arr[i].append(row[1])   #column 2 contains recipients name
            arr[i].append(row[2])   #column 3 contains mail addresses
            i=i+1
for x in range(len(arr)):
    # Create a text/plain message
    msg = email.mime.multipart.MIMEMultipart()
    msg['Subject'] = 'email subject'
    msg['From'] = 'your_email_address@gmail.com'
    msg['To'] = arr[x][2]
    name = string.capwords(arr[x][1])
    company_name = string.capwords(arr[x][0])
    sendto = arr[x][2]
    # The main body is just another attachment

    body = email.mime.text.MIMEText("""Hello """+ name +""",
Mail body

""")
    msg.attach(body)
    # PDF attachment
    filename='resume.pdf'
    fp=open(filename,'rb')
    att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
    fp.close()
    att.add_header('Content-Disposition','attachment',filename=filename)
    msg.attach(att)

    # send via Gmail server
    try:
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.ehlo()
        s.starttls()
        s.login('your_email_add@gmail.com','password')
        s.sendmail('your_email_add@gmail.com',sendto, msg.as_string())
        print('successfully sent to '+name+' at '+sendto)
        s.quit()
    except:
        print('Error')

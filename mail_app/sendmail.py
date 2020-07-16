import smtplib
from credentials import MAIL, PASSWORD
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(subject="Test Message", text="Email Body", from_email="Developer Channel <devchannel09@gmail.com>", to_emails=[None]):
    smtp = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465)
    smtp.login(MAIL, PASSWORD)
    msg = MIMEMultipart("Alternative")
    msg['From'] = from_email
    msg['To'] = ','.join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'html')
    msg.attach(txt_part)
    msg_str = msg.as_string()
    try:
        smtp.sendmail(from_email, to_emails, msg_str)
        sent = True
    except:
        sent = False
    smtp.quit()
    return sent

if __name__ == "__main__":
    with open('mail.html') as f:
        mail = f.read()

    if send_mail(subject="Hello World!", text=mail, to_emails=["devchannel09@gmail.com"]):
        print("Sent")
    else:
        print("Not Sent")

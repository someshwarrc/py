import imaplib
import email
import getpass
import sys

MAIL = input("Enter your gmail address: ")
PASSWORD = getpass.getpass(prompt="Enter your password: ")

mail = imaplib.IMAP4_SSL(host="imap.gmail.com", port=993)
try:
    mail.login(MAIL, PASSWORD)
    print("Logged In successfully! Welcome @", MAIL.split('@')[0].lstrip())
except:
    print("Couldn't login")

print("="*70)
mail.select(mailbox="INBOX")
_, search_data = mail.search(None, 'ALL')
for num in search_data[0].split():
    email_data = {}
    _, data = mail.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    for header in ['subject', 'to', 'from', 'date']:
        # print("{}: {}".format(header, email_message[header]))
        email_data[header] = msg[header]
    for part in msg.walk():
        if part.get_content_type == "text/plain":
            body = part.get_payload(decode=True)
            email_data['body'] = body.decode()
        elif part.get_content_type() == "text/html":
            html_body = part.get_payload(decode=True)
            email_data['html_body'] = html_body.decode()
    for key in email_data.keys():
        print("{}: {}".format(key, email_data[key]))
    print("="*70)
    # print(email_data)



mail.close()
mail.logout()

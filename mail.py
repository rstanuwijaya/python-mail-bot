# %%
import smtplib, ssl
import email
import dotenv
import os

from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

import maillist
import importlib
importlib.reload(maillist)

dotenv.load_dotenv()

PASS = os.getenv('PASS')

port = 587  # For starttls
smtp_server = "outlook.office365.com"
sender_email = "rstanuwijaya@connect.ust.hk"
password = PASS

for mail in maillist.mail_list:
    print(mail['email_addrs'])
    msg = MIMEMultipart()

    msg['Subject'] = f'Test Subject'
    msg['From'] = sender_email
    msg['To'] = mail['email_addrs']
    
    files = [r'C:\Users\stnav\OneDrive - HKUST Connect\Academics\Others\CV\CV_Randy Stefan Tanuwijaya.pdf']
    for path in files:
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(Path(path).name))
        msg.attach(part)
    
    content = f"""\
    mari makan tai at {mail['company_name']}.
    """
    msg.attach(MIMEText(content))

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.send_message(msg)

# %%

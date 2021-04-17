#%%
import json
import os

from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

Messages = []
filepath = os.path.dirname(os.path.abspath(__file__))

target_file = r'\targets\target.json'

with open(filepath + target_file, 'r') as f:
    MailingList = json.load(f)

for mail in MailingList:
    msg = MIMEMultipart()

    msg['Subject'] = f'Test Subject'
    msg['From'] = 'rstanuwijaya@connect.ust.hk'
    msg['To'] = mail['email_addrs']

    attachements = [
        r'\attachment\CV_Randy Stefan Tanuwijaya.pdf'
    ]

    for path in attachements:
        part = MIMEBase('application', "octet-stream")
        with open(filepath + path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(Path(path).name))
        msg.attach(part)

    text = f"""\
    mari makan tai at {mail['company_name']}.
    """

    msg.attach(MIMEText(text))
    Messages.append(msg)
# %%

#%%
import smtplib, ssl
import dotenv
import os

import components.message
import importlib
importlib.reload(components.message)

dotenv.load_dotenv()
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# HKUST SMTP SERVER
port = 587  
smtp_server = "outlook.office365.com"
sender_email = EMAIL_ADDRESS
password = EMAIL_PASSWORD

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    for msg in components.message.Messages:
        print(f'Sending email to: %s' % msg['To'])
        server.send_message(msg)

# %%

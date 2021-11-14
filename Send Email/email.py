import yagmail
# import os
import time


PASSWORD = 'YOUR_SECRET_KEY'

sender = 'SENDER_EMAIL'
receiver = 'RECEIVER_EMAIL'

subject = 'Test'

contents = """
Hi, this is the test emai!
"""


while True:
  # yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
  yag = yagmail.SMTP(user=sender, password=PASSWORD)
  yag.send(to=receiver, subject=subject, contents=contents)
  print('Email sent!')
  time.sleep(60)
# Жду от вас письмо! (слайды 14-18). Воспользуйтесь менеджером контекста (with … as) (слайд 20)
# (Не забудьте для себя понять код из официальной документации – слайд 17).

import smtplib

HOST = "smtp.gmail.com"
SUBJECT = "Test email from Python"
TO = "el.piankova@gmail.com"
FROM = "nptiutiunnyk@gmail.com"
text = "Test! Homework 6.4 from Tiutiunnyk Nataliia"

BODY = "\r\n".join([
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
])

login = 'nptiutiunnyk@gmail.com'
password = '####'

server = smtplib.SMTP_SSL(HOST, 465)

server.ehlo()
server.login(login, password)
server.sendmail(FROM, [TO], BODY)
server.quit()

import smtplib
from email.message import EmailMessage

# 보내는 메일 서버
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# 송신자, 수신자, 비밀번호
sender = 'ninanooo@gmail.com'
recipient = 'dusvlf12ro@sch.ac.kr'
password = 'adckidufwhiqrqla'

# 메시지 생성하기
msg = EmailMessage()
msg['Subject'] = '제목'
msg['From'] = sender
msg['To'] = recipient
text = '내용'
msg.set_content(text)

# SMTP 객체 생성 후, 메시지 전송
s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()
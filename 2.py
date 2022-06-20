import paramiko
import getpass
import smtplib
import filetype
from email.message import EmailMessage
import zipfile
import os

filename = '20171537.zip' 
dirname = '/home/net_pro/20171537' 
CMD = 'zip -r ' + filename + ' ' + dirname 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
user = input('Username: ')
pwd = getpass.getpass('Password: ')
ssh.connect('114.71.220.5', 22, username=user, password=pwd)
stdin, stdout, stderr = ssh.exec_command(CMD)
sftp = ssh.open_sftp()
sftp.get(filename, filename)
sftp.close()
ssh.close()

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'ninanooo@gmail.com'
recipient = 'daeheekim@sch.ac.kr'
password = 'adckidufwhiqrqla'


msg = EmailMessage()
msg['Subject'] = '네트워크 프로그래밍 기말고사'
msg['From'] = sender
msg['To'] = recipient
msg.set_content('네트워크 프로그래밍 기말고사 답안 제출합니다')


with open('20171537.zip', 'rb') as f:
    msg.add_attachment(f.read(), maintype='application', subtype='zip',\
    filename='20171537.zip')

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()

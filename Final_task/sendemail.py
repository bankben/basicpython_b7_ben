## Program untuk mengirim email. Alamat email penerima disimpan pada file txt
## referensi: 
## https://code.tutsplus.com/id/tutorials/sending-emails-in-python-with-smtp--cms-29975
## https://python.web.id/posts/detail/mengirim-email-gmail-via-python/
## https://ichi.pro/id/cara-mengirim-email-dengan-lampiran-dengan-python-188994555473139

## Membaca daftar penerima email dari file


with open('penerima_list.txt', 'r') as file:
    penerima = file.read().replace('\n', ',')

#-------------------------------------------------
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

import smtplib

# create message object instance
msg = MIMEMultipart()


# setup the parameters of the message
pengirim = input(str("Masukkan email pengirim: "))
password = input(str("masukkan password email pengirim = "))
msg ['Subject'] = input(str("Masukkan Subject: "))
msg ['From'] = pengirim
msg ['To'] = penerima



# attach text to message body
filename = "email_body.txt"
msg.attach(MIMEText(open(filename).read()))


# attach image to message body
with open('banner.png', 'rb') as fp:
    img = MIMEImage(fp.read())
    img.add_header('Content-Disposition', 'attachment', filename="banner.png")
    msg.attach(img)


# create server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

# Login Credentials for sending the mail
server.login(pengirim, password)


# send the message via the server.
server.sendmail(msg['From'], msg["To"].split(","), msg.as_string())

server.quit()

print ("berhasil mengirim email") 
print ("Terima kasih")

#Terima Kasih
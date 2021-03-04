#! /usr/bin/env python3
import smtplib, ssl
#SSL connection method
#smtpobj=smtplib.SMTP_SSL('smtp.qq.com',465)
smtpobj=smtplib.SMTP_SSL('smtp.gmail.com',465)
#TLS connection method
#smtpobj=smtplib.SMTP('smtp.qq.com',587)
smtpobj.ehlo()
#TLS need enable encryption for the connection
#smtpobj.starttls()
#smtpobj.login('413168358@qq.com','xossqpfzyazmcajd')
smtpobj.login('yuhaitao521ok@gmail.com','xyojptclbahgrhwe') #application-specific password
smtpobj.sendmail('yuhaitao521ok@gmail.com',['413168358@qq.com','yuhaitao521ok@gmail.com'],'Subject: Send for myself\n\ndear all, this is a mail.')
smtpobj.quit()

with smtplib.SMTP_SSL('smtp.qq.com',465) as server:
    server.login('413168358@qq.com','xossqpfzyazmcajd')
    server.sendmail('413168358@qq.com','413168358@qq.com','subject:123\n\n1234')
    server.quit()
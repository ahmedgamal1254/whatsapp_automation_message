"""
            project
            send whatsapp message by automation
            i can do array y reason when i donot use whatsapp
            program can choose one message and sent it
"""
import pyautogui as pg
import time
import webbrowser
import random
import pywhatkit as whatsapp

# choose user if he late in this day
value=input("Enter yes or no if you are late on day :- ")

if value=='no':
    print('thank you for time..')
else:
    # array of reasons which you can use it when you kate
    reasons=['لدى عمل كثير اليوم ربما أتى متاخر','لدينا اجتماع هام اليوم وسوف أتاخر']

    # make time which message sent on it
    time_sent=input("اختر الوقت المتاسب لارسال الرسالة بنظام ال24 مثل 20 8:- ")

    # input this phone which mssage sentt to it
    phone=input("اكتب رقم المحمول المراد ارسال رسالة له :- ")

    # get hours and minutes from time_sent
    h,m=list(map(int,time_sent.split()))

    # store message randomly
    msg=random.choice(reasons)

    # make format for phonenumber
    ph="+20"+phone

    whatsapp.sendwhatmsg(ph,msg, h, m)

    # break between this stop and next step
    time.sleep(3)

    # create repo
    pg.rightClick(131,968)
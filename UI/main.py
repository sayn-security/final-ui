import sys
import os
import re
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pynput import keyboard
import time
import decimal
import xlsxwriter
from threading import Thread
import time
import keyboard as newKeyboard

import tkinter
from Login import Ui_LOGIN
from Reset import Ui_reset
from Correct_password import Ui_correctpassword
from Incorrect_password import Ui_Incorrectpassword
from registration import Ui_Registration
from Secondary import Ui_secondary
from Secondary_2 import Ui_Secondary_Password
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
import CART_Final
#import emailsayn


class incorwindow(QtWidgets.QDialog, Ui_Incorrectpassword):
    def __init__(self, parent=None):
        super(incorwindow, self).__init__(parent)
        self.setupUi(self)
        self.OkButton.clicked.connect(self.hide)



class loginwindow(QtWidgets.QMainWindow, Ui_LOGIN):
    
    def __init__(self, parent=None):
        super(loginwindow, self).__init__(parent)
        self.setupUi(self)
        self.loginbutton.clicked.connect(self.hide)

class loginreset(QtWidgets.QMainWindow, Ui_LOGIN):
    
    def __init__(self, parent=None):
        super(loginreset, self).__init__(parent)
        self.setupUi(self)
        self.resetbutton.clicked.connect(self.hide)
          
class secd2window(QtWidgets.QMainWindow, Ui_Secondary_Password):
    
    def __init__(self, parent=None):
        super(secd2window, self).__init__(parent)
        self.setupUi(self)
        self.submit.clicked.connect(self.hide)
        #self.keylistener()
        

        
class resetwindow(QtWidgets.QMainWindow, Ui_reset,):
    def __init__(self, parent=None):
        super(resetwindow, self).__init__(parent)
        self.setupUi(self)
        '''abc = 2
        defg = 'suri.kaks@gmail.com'
        print(Manager.sender(self,abc,defg))'''
        #Manager.sender(2,'suri.kaks@gmail.com')
        self.backbutton.clicked.connect(self.hide)


class regwindow(QtWidgets.QMainWindow, Ui_Registration):
    
    def __init__(self, parent=None):
        super(regwindow, self).__init__(parent)
        self.setupUi(self)
        self.nextbutton.clicked.connect(self.hide)

class regsecdwindow(QtWidgets.QMainWindow, Ui_secondary):
    
    def __init__(self, parent=None):
        super(regsecdwindow, self).__init__(parent)
        self.setupUi(self)
        self.backbutton.clicked.connect(self.hide)
def keylistener():
        a = []
        tim = []
        pr = []
        rl = []
        prt = []
        rlt = []  

        def on_press(event):
            import write_to_sheet
            key = event.name
            print(key)
            if key is "enter":
            # Stop listener
                print("ended")
                
                #y=Thread(target=write2sheet(a, tim, pr, rl, prt, rlt), daemon=True)
                #y.start()

                write_to_sheet.write2sheet(a, tim, pr, rl, prt, rlt)
                print ("recorded one password entery")
                newKeyboard.unhook_all()
                return False
            else:
                value = str(key)
                pr.append(value)
                prt.append(decimal.Decimal(time.clock()))
                a.append(value)
                tim.append(decimal.Decimal(time.clock()))

        def on_release(event):
            key = event.name
            if key is "enter":
                # Stop listener
                newKeyboard.unhook_all()
                return False
    
            value = str(key)
            rl.append(value)
            rlt.append(decimal.Decimal(time.clock()))
            a.append(value)
            tim.append(decimal.Decimal(time.clock()))
    
        newKeyboard.block_key("left windows")
        newKeyboard.on_press(on_press)
        newKeyboard.hook(on_release)
        print("keylogger running")
class Manager:
   
    
    def check_order(self):
        from Secondary_2 import order1 as order
        ordoc=open("inoder.txt","r")
        regorder=open("order_reg.txt","r")
        for item1 in order:
            if (ordoc.mode=="r") & (regorder.mode=="r"):
                or1=ordoc.read()
                or2=regorder.read()
            if (or1 == or2):
                print("Welcome")
                break
            else:
                print("Wrong Pattern")
                order.clear()
                return Manager()
                #break       
           
        ordoc.close()
        regorder.close()

   

    def randomStringwithDigitsAndSymbols(self,stringLength=10):
        """Generate a random string of letters, digits and special characters """
        password_characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password_characters) for i in range(stringLength))

    def sender(self,code,user_email):
        print("abchere")
        from_user = 'saynsec2019@gmail.com'
        to_user = user_email
        password = 'sayn2019'
        server = smtplib.SMTP('smtp.gmail.com',587)
        #server.helo()
        server.ehlo()
        server.starttls()
        server.login(from_user,password)
        subject = 'Sayn Securities'
        print("reached heere1")
        msg = MIMEMultipart()
        msg['From'] = from_user
        msg['To'] = to_user
        msg['Subject'] = subject
        body = ''
        if(code == 1):
            body = 'Your device has been accessed. If this is you then please ignore this email. If this is not you then please check your device.'
        if(code==2):
            body = self.randomStringwithDigitsAndSymbols(10)
        print("reached here 2")
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail('',to_user,text)
        server.close()
        print("reached here 3")
        return body

        
   
    def keyPressEvent(self, e):
        print ("event", e)
        if e.key()  == QtCore.Qt.Key_Return :
            self.check_passlog()
        elif e.key() == QtCore.Qt.Key_Enter :   
            self.check_passlog()
    def incore(self):
        return Manager()

    def check_passlog(self):
                usdata1=self.login.passwordbox.text()
                usdoc1= open("temp_pass.txt","w")
                usdoc1.write(usdata1)
                usdoc1.close()
                temppass= open("temp_pass.txt","r")
                regpass=open("regpass.txt","r")
                tp=temppass.read()
                rp=regpass.read()
                if(tp == rp):
                    time.sleep(2)
                    if(CART_Final.machineLearning() != "sub24"):
                        print("Correct Password")
                        self.wrongpatt()
              
                        self.secd2.show()
                    else:
                        print("Welcome")

                else:
                    print("Incorrect Password")
                    self.inco.show()

                temppass.close()
                regpass.close()
    def wrongpatt(self):
        abc = 1
        defg = 'suri.kaks@gmail.com'
        wro=self.sender(abc,defg)
        print(wro)
    def resetcode(self):
        abc = 2
        defg = "suri.kaks@gmail.com"
        res=self.sender(abc,defg)
        print(res)
                 
    def __init__(self):
        self.login = loginwindow()
        self.inco = incorwindow()
        self.secd2=secd2window()
        self.reset=resetwindow()
        self.reg=regwindow()
        self.regsecd=regsecdwindow()
        self.logreset=loginreset()
        #x=Thread(target=self.login.show())
        #x.start()    
        #app.processEvents()
        keylistener()
        self.login.show()
 
        self.login.centralwidget.keyPressEvent = self.keyPressEvent
        self.login.loginbutton.clicked.connect(self.check_passlog)
        self.inco.OkButton.clicked.connect(self.login.show)
        self.inco.OkButton.clicked.connect(self.incore)
        self.login.resetbutton.clicked.connect(self.reset.show)
        self.login.resetbutton.clicked.connect(self.resetcode)
        self.reset.backbutton.clicked.connect(self.login.show)
        self.reset.resend.clicked.connect(self.resetcode)
        self.secd2.submit.clicked.connect(self.login.hide)
        self.secd2.submit.clicked.connect(self.check_order)
        self.reg.nextbutton.clicked.connect(self.regsecd.show)
        self.regsecd.backbutton.clicked.connect(self.reg.show)
        
        #self.reset.resend.clicked.connect(Manager.sender(self,abc,defg))
        #self.secd2.submit.clicked.connect(self.keylistener)       
        
        
def main():
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    
    #print(sender(2,'wasabiijunior@gmail.com'))
    sys.exit(app.exec_())

if __name__ == '__main__':
   main()
    
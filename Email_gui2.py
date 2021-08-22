from Email_gui1 import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def signals(self): #connect see_email_button clicked signal to template function
    self.see_email_button.clicked.connect(self.template)


def template(self): #turns input into text
    greeting = self.enter_greeting_box.text()
    remainder = f"""

I saw online you are interested in our Taekwondo Classes. I'd love to answer any and all questions you have. All I need to know is if the class is for you, your child(ren), or both? We have appointments available Tuesday evening (between 5-6) or Wednesday (between 3-4:15). I hope you enjoy your weekend and can enjoy some of the sunshine we are going to get! Thank you and I look forward to meeting you soon

Mr. Magness
--
"""
    full = f"{greeting} {remainder}"
    self.fullText.setText(str(full))
    return full


def html():
    sig = '''
    <div dir="ltr" data-smartmail="gmail_signature"><div dir="ltr"><div><div dir="ltr"><div><font face="arial narrow, sans-serif"><b>Ignite ATA Martial Arts</b></font></div><div><font face="arial narrow, sans-serif">805-650-5425</font></div><div><font face="arial narrow, sans-serif">3000 Bunsen Avenue, G,&nbsp;</font><span style="font-family:&quot;arial narrow&quot;,sans-serif">Ventura, CA 93003</span></div><div><font face="arial narrow, sans-serif"><a href="http://www.igniteata.com" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://www.igniteata.com&amp;source=gmail&amp;ust=1623439138213000&amp;usg=AFQjCNGmqdGohm2nMhQq12PhQOcVvl5CFw">www.igniteata.com</a></font></div><div><img src="https://ci5.googleusercontent.com/proxy/BgmdqxEfCVdFGDSewGFh8cwqytYdPv1qlQzzWV0CI_owSsaXcWU9FvsXhMjlmAgiDajNbkNtyLaSNQVhK9WBKiDxZYj4n_rj8YrP5Ldyk6ioC__o7k-LFmG2-rBXy2luxL6RV-NP_L2Q4SvQRxWGOmzT4dG170olJ35pr-dy9Uhni0JTRzlg4f8QugbnB58TJbrLbZQcLlI=s0-d-e1-ft#https://docs.google.com/uc?export=download&amp;id=0B_fMuyVEsLjgSENMVm5oYUdIUzg&amp;revid=0B_fMuyVEsLjgNXpnQW5CRktZT256QXVUYWI4OHRZQ05TZERRPQ" style="font-size:12.8px" class="CToWUd"></div></div></div></div></div>
    '''
    return sig


def message_sender(): #sends the message
    message = MIMEMultipart('mixed')
    text = template()

    txt_part = MIMEText(text, 'plain')
    message.attach(txt_part)

    html_part = MIMEText(html(), 'html')
    message.attach(html_part)

    def signals2(self):  # connect send_button clicked signal to sending_email function
        self.send_button.clicked.connect(self.sending_email())

    def sending_email():
        message['Subject'] = "Free Private Intro class - Summer Savings"
        message['From'] = "bessolomicah@gmail.com"
        message['to'] = self.enter_email_box.text()

        password = str("password")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(message['From'], password)
        print("login success")
        server.send_message(message)
        print("email has been sent")
    signals2()


Ui_MainWindow.signals = signals
Ui_MainWindow.template = template

if __name__ == "__main__": # A library or a stand-alone program
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())
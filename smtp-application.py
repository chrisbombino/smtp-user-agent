import smtplib
import auth
from email.mime.text import MIMEText
from tkinter import *


class pw_window():
    def __init__(self, master):
        self.master = master
        frame = Frame(master)

        self.pw_label = Label(frame, text='Password:', height=2)
        self.pw_label.pack()
        self.E5 = Entry(frame, bd=5, show='*')
        self.E5.pack()

        self.pw_submit = Button(frame, text='Submit', command=self.submit, height=2, width=10)
        self.pw_submit.pack()

        self.pw_cancel = Button(frame, text='Cancel', command=frame.quit, height=2, width=10)
        self.pw_cancel.pack()

        frame.pack()

    def submit(self):
        print(self.abc)

class emailWindow:
    def __init__(self, master):
        self.master = master
        frame = Frame(master)
        frame.pack()

        self.tk_to = Label(frame, text='To:')
        self.tk_to.pack()
        self.E1 = Entry(frame, bd=5)
        self.E1.pack()

        self.tk_from = Label(frame, text='From:')
        self.tk_from.pack()
        self.E2 = Entry(frame, bd=5)
        self.E2.pack()

        self.tk_subject = Label(frame, text='Subject:')
        self.tk_subject.pack()
        self.E3 = Entry(frame, bd=5)
        self.E3.pack()

        self.tk_body = Label(frame, text='Body:')
        self.tk_body.pack()
        self.E4 = Text(frame, bd=5, height=10)
        self.E4.pack()

        self.send_button = Button(frame, text='Send', command=self.open_pw, height=2, padx=50)
        self.send_button.pack()

    def get_msg_info(self):
        to = self.E1.get()
        print(to)

    def open_pw(self):
        abc = Tk()

        pw_label = Label(abc, text='Password:', height=2)
        pw_label.pack()

        self.E5 = Entry(abc, bd=5, show='*')
        self.E5.pack()

        pw_submit = Button(abc, text='Submit', command=self.send, height=2, width=10)
        pw_submit.pack()

        pw_cancel = Button(abc, text='Cancel', height=2, width=10)
        pw_cancel.pack()

        abc.mainloop()
        #self.newWindow = Toplevel(self.master)
        #w = pw_window(self.newWindow)

    def send(self):
        to_email = self.E1.get()
        from_email = self.E2.get()
        subject = self.E3.get()
        body = self.E4.get('1.0', END)
        pw = self.E5.get()
        print('To: ' + to_email)
        print('From: ' + from_email)
        print('Subject: ' + subject)
        print('Body: ' + body)
        print('Password: ' + pw)

root = Tk()
w = emailWindow(root)
root.mainloop()

'''
# initialize message info
from_email = 'cjbombino@gmail.com'
to_email = from_email
password = auth.app_password
subject = 'Test'
body = 'Hello World'

# xreate SMTP server and login
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(from_email, password)

# Create MIMEText messsage object
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = to_email

# Send mail and quit server
server.sendmail(from_email, to_email, msg.as_string())
server.quit()
'''
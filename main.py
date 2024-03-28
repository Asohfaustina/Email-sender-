from tkinter import *
from email.message import EmailMessage
import ssl
import smtplib
from tkinter import filedialog
# def attach_file():
#     files = filedialog.askopenfiles(mode='r',filetypes=[('txt file', '*.txt'),
#                                                         ('png file', '*.png')])
#     return files
def send_mail():
    email_sender = entryfrom.get()
    password = entrypwd.get()
    email_receiver = entryto.get()
    subject = entrysub.get()
    body = entrybody.get(1.0, END)
    # files = attach_file()

    em = EmailMessage()
    em['From'] = email_receiver
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    # em.add_attachment(files)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    suc_label.config(text='Mail sent succesfully...')


root = Tk()
root.geometry("800x900")
labelHead = Label(root, text="EMAIL SENDER", font='times 20 bold', fg='light green')
labelHead.pack()
labelfrom = Label(root, text= 'Whats your email', font='times 15')
labelfrom.place(x=200, y=50)
entryfrom = Entry(root, font='times 15', width=30 )
entryfrom.place(x=400, y=50)
labelpwd = Label(root, text= ' Email App password ', font='times 15')
labelpwd.place(x=200, y=90)
entrypwd = Entry(root, font='times 15', width=30 )
entrypwd.place(x=400, y=90)
labelto = Label(root, text= ' Who is the recipient', font='times 15')
labelto.place(x=200, y=140)
entryto = Entry(root, font='times 15', width=30 )
entryto.place(x=400, y=140)
labelsub = Label(root, text= ' What is the subject', font='times 15')
labelsub.place(x=200, y=190)
entrysub = Entry(root, font='times 15', width=30)
entrysub.place(x=400, y=190)
labelbody = Label(root, text= ' What is the body', font='times 15')
labelbody.place(x=200, y=240)
entrybody = Text(root, font='times 12', width=37, height=16)
entrybody.place(x=400, y=240)
buttonsend = Button(root, text="Send", font='times 15', bg="light green", width=35, command=send_mail)
buttonsend.place(x=200, y=600)
suc_label = Label(root, font='times 15', fg='green')
suc_label.place(x=200, y=650)
root.mainloop()
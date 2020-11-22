import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time

def get_pdf_path():
    """
    Récupérer le chemin absolu du pdf
    """
    arr = os.listdir(r"C:\attestation_derogatoire")
    pdf_path = ""
    for file in arr:
        if 'attestation' in file:
            pdf_path = "C:\\attestation_derogatoire\\"+file
    return pdf_path

def move_pdf_toarch():
    dest = "\\archive\\"
    root = r"C:\attestation_derogatoire"
    arr = os.listdir(r"C:\attestation_derogatoire")
    pdf_path = ""
    for file in arr:
        if 'attestation' in file:
            pdf_path = "C:\\attestation_derogatoire\\"+file
            if not os.path.exists(root+dest):
                os.makedirs(root+dest)
            os.replace(pdf_path, root+dest+file)

# print("pdf_path "+get_pdf_path())
# move_pdf_toarch()




def send_mail(mail, sujet_mail, body_mail, pwd):
    fromaddr = mail
    toaddr = fromaddr

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = sujet_mail

    # string to store the body of the mail
    body = body_mail

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    # filename = "attestation-2020-11-15_16-40.pdf"
    filename = get_pdf_path()
    attachment = open(filename, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, pwd)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()

# send_mail()
# time.sleep(2)
# move_pdf_toarch()

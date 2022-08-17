import smtplib

""" 
function to send email 
1st argument list of receivers
2nd argument subject of mail
3rd argument body of mail
"""


def send_mail(receiver, subject, body):

    sender = 'skyras.sih@gmail.com'
    password = 'qilrwoxeccqfkdjn'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sender, ", ".join(receiver), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, receiver, email_text)
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)

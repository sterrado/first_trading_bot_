import smtplib
from secrets import email_pass


def send_email(to, subject, body):
    gmail_user = 'santiagoterrado@gmail.com'
    gmail_password = email_pass
    sent_from = gmail_user

    to = to
    subject = subject
    body = body

    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)

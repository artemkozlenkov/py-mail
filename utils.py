import os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def creds():
    myvars = {}
    with open("creds.txt") as myfile:
        for line in myfile:
            name, var = line.partition("=")[::2]
            myvars[name.strip()] = var.strip()

    return myvars


def message(sender, receiver, subject, template):
    with open(template, 'r') as b:
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = subject

        # for filename in os.listdir('email-templates/1/images'):
        #     with open(f'email-templates/1/images/{filename}', 'rb') as image:
        #         msgImage = MIMEImage(image.read())
        #         # type = msgImage.get_content_type().split('/')[1]
        #         msgImage.add_header('Content-ID', f'<image_{filename}')
        #         msgImage.add_header('X-Attachment-Id', f'<image_{filename}')
        #         msgImage['Content-Disposition'] = f'inline; filename=image{filename}'
        #
        #         image.close()
        #         message.attach(msgImage)

        # The body and the attachments for the mail
        message.attach(MIMEText(b.read(), 'html'))
    return message

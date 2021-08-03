import smtplib
import yaml
import sys

from utils import message, creds


def main():
    for arg in sys.argv[1:]:
        print(arg)

    with open("data.yml", 'r') as f:
        file = yaml.load(f, Loader=yaml.FullLoader)['dev']

        sender_email = file['sender']['email']
        sender_pass = creds()['sender_pass']

    for receiver in file['receivers']:
        template = file['config']['template']

        body = message(sender_email, receiver, file['subject'], template)

        port = file['config']['port']
        smtp = file['config']['smtp']

        session = smtplib.SMTP(smtp, port)

        if port == 587:
            session.starttls()
            session.login(sender_email, sender_pass)

        text = body.as_string()
        session.sendmail(sender_email, receiver, text)
        session.quit()

        print(f'Mail to ---> {receiver} <--- sent.')


if __name__ == "__main__":
    main()

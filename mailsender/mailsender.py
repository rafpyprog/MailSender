import win32com.client as win32


__all__ = ['__version__', 'MailSender']


__version__ = '0.0.3'


class MailSender(object):
    ''' Send email using the active email on Outlook '''

    def __init__(self):
        self.outlook = win32.Dispatch('outlook.application')

    def new_email(self, to, subject, body, HTML_body=None, attachments=None):
        ''' Return a new email object. To send it use email.Send()'''
        mail = self.outlook.CreateItem(0)

        mail.To = to
        mail.Subject = subject
        mail.Body = body

        if HTML_body:
            mail.HTMLBody = HTML_body

        if isinstance(attachments, list) and attachments != []:
            for file in attachments:
                mail.Attachments.Add(file)

        return mail

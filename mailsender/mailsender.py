# -*- coding: utf-8 -*-
'''
    MailSender

    Send email using the active profile on Outlook.
'''
from os.path import isfile
from typing import Dict, List

from win32com.client import CDispatch
import win32com.client as win32


__all__ = ['MailSender']


class MailSender(object):
    ''' Send email using the active email on Outlook '''

    def __init__(self):
        self.outlook = win32.Dispatch('outlook.application')
        self.mail = None

    def add_email_headers(self, headers: Dict[str, str]):
        ''' Add email headers '''
        for field, value in headers.items():
            setattr(self.mail, field, value)

    def add_email_content(self, content: str, html_body=False):
        ''' Add email content '''
        if html_body is True:
            setattr(self.mail, 'HTMLBody', content)
        else:
            setattr(self.mail, 'Body', content)

    def add_email_attachments(self, attachments: List[str]):
        ''' Add email attachments '''
        if isinstance(attachments, list):
            for file in attachments:
                if isfile(file) is False:
                    msg = '{} attachment  is not a valid file.'
                    raise ValueError(msg.format(file))
                self.mail.Attachments.Add(file)
        else:
            raise ValueError('Attachments must be in a list')

    def new_email(
            self, headers: Dict[str, str], content: str, attachments=None,
            html_body=False) -> CDispatch:
        ''' Return a new email object. To send it use email.Send()'''
        self.mail: CDispatch = self.outlook.CreateItem(0)

        self.add_email_headers(headers)
        self.add_email_content(content, html_body=html_body)
        if attachments is not None:
            self.add_email_attachments(attachments)

        return self.mail

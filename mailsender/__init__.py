# -*- coding: utf-8 -*-

'''
MailSender
~~~~~~~~~~

Send email using Outlook. Basig usage:

    >>> ms = MailSender()
    >>>
    >>> user_email = 'user@gmail.com'
    >>> subject = 'Hi!'
    >>> message = 'This is a test. Thanks!'
    >>>
    >>> mail = ms.new_email(to=user_email, subject=subject, body=message')
    >>> mail.Send()
'''

__version__ = '0.0.5'

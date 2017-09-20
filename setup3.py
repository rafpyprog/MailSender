from setuptools import setup
from mailsender.mailsender import __version__

setup(
    author='Rafael Alves Ribeiro',
    author_email='rafael.alves.ribeiro@gmail.com',
    name='mailsender',
    packages=['mailsender'],
    version=__version__,
    description='Envia email utilizando o usuário ativo no Outlook.',
    dependency_links=[
        'https://github.com/rafpyprog/MailSender/raw/master/wheels/pywin32-221-cp36-none-win_amd64.whl'
    ]
    )

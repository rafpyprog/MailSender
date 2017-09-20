import pip

from setuptools import setup


setup(
    author='Rafael Alves Ribeiro',
    author_email='rafael.alves.ribeiro@gmail.com',
    name='mailsender',
    packages=['mailsender'],
    version='1.0.3',
    description='Envia email utilizando o usuário ativo no Outlook.',
    install_requires=['pywin32=2.2.1'],
    dependency_links=['https://github.com/rafpyprog/MailSender/raw/master/wheels/pywin32-221-py3.6-win-amd64.egg']
    )

# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
from distutils.version import StrictVersion
import platform
import pip

from setuptools import setup

from mailsender import __version__

setup(
    author='Rafael Alves Ribeiro',
    author_email='rafael.alves.ribeiro@gmail.com',
    name='mailsender',
    packages=['mailsender'],
    version=__version__,
    install_requires=[
        'pypiwin32==219;python_version<"3.6"',
    ],
    description='Envia email utilizando o usuário ativo no Outlook.',
    )


python_version = '.'.join(platform.python_version_tuple())
cp36 = '3.6.0'
bits = platform.architecture()[0]


pypiwin32_cp36_64bits = ('https://pypi.python.org/packages/d0/f7/56e35'
                                 '902d32299020cf9136264ca102ff0b03c0555621b469'
                                 'c825bc10d08/pypiwin32-220-cp36-none-win_amd6'
                                 '4.whl')

pypiwin32_cp36_32bits = ('https://pypi.python.org/packages/bb/5b/2f620'
                                 '7cab31f707fc4a8d33e3d6b14daa8750ecabf658127e'
                                 '31d16cdd06b/pypiwin32-220-cp36-none-win32.wh'
                                 'l')

proc = Popen(f'pip install {pypiwin32_cp36_32bits}', shell=True, stdout=PIPE)
stdout, err = proc.communicate()
print(stdout.decode())

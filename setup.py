#!/usr/bin/env python
from setuptools import setup

setup_info = dict(
    name='Alexander',
    version='1.0',
    author='ZZZlax',
    author_email='theoriginalashketchum@protonmail.com',
    url='https://github.com/ZZZlax/.Alex',
    download_url='https://github.com/ZZZlax/.Alex',
    description='Alexander',
    keywords = ["Alex", "Alexander"],
    long_description='Translate and search web and wiki with tts module',
    classifiers=[
        "Topic :: Utilities",
        'Development Status :: Production/Stable',
        'Environment :: X11 Applications',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=['googlesearch-python', 'wikipedia', 'pyttsx3', 'gtts', 'googletrans==4.0.0-rc1', 'locale',  'wikipedia', 'speechrecognition'])

setup(**setup_info)

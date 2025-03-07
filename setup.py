#!/usr/bin/env python

"""
Flask-Sockets
-------------

Elegant WebSockets for your Flask apps.
"""
from setuptools import setup


setup(
    name='Flask-Sockets',
    version='2.0.0',
        url='https://github.com/APrioriInvestments/flask-sockets',
    license='See License',
    author='Kenneth Reitz',
    author_email='_@kennethreitz.com',
    description='Elegant WebSockets for your Flask apps.',
    long_description=__doc__,
    py_modules=['flask_sockets'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask >= 2.0, < 3.0',
        'gevent',
        'gevent-websocket'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

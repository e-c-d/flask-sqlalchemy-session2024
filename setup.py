# -*- coding: utf-8 -*-
"""
Flask-SQLAlchemy-Session
-----------------------

Provides an SQLAlchemy scoped session that creates
unique sessions per Flask request
"""
import sys
import os
from setuptools import setup

if sys.version_info < (2, 6):
    raise Exception("Flask-SQLAlchemy-Session requires Python 2.6 or higher.")

# Hard linking doesn't work inside VirtualBox shared folders. This means that
# you can't use tox in a directory that is being shared with Vagrant,
# since tox relies on `python setup.py sdist` which uses hard links. As a
# workaround, disable hard-linking if setup.py is a descendant of /vagrant.
# See
# https://stackoverflow.com/questions/7719380/python-setup-py-sdist-error-operation-not-permitted
# for more details.
if os.path.abspath(__file__).split(os.path.sep)[1] == "vagrant":
    del os.link

with open("README.md", "rt", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Flask-SQLAlchemy-Session2024",
    version="2.0.0",
    packages=["flask_sqlalchemy_session2024"],
    author="Eduard Christian Dumitrescu",
    author_email="eduard.c.dumitrescu@gmail.com",
    url="https://github.com/e-c-d/flask-sqlalchemy-session2024",
    license="MIT",
    description="SQL Alchemy session scoped on Flask requests.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    # Flask should be >=0.10
    install_requires=["sqlalchemy", "Flask", "Werkzeug"],
    tests_require=["pytest"],
    extras_require={"docs": ["Sphinx", "alabaster"]},
)

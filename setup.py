# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from djangocms_github import __version__


setup(
    name='djangocms-github',
    version=__version__,
    description=open('README.rst').read(),
    author='Adam&#39;s personal organisation',
    author_email='None',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)

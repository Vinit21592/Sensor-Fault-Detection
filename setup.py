# Just to create proper packages, libraries so that it can be shared and used for multiple purposes

from setuptools import find_packages,setup

setup(
    name="sensor",
    version="0.0.1",
    author="vinit",
    author_email="vinit.londhe21@gmail.com",
    packages = find_packages(),
    install_requires=[]
)


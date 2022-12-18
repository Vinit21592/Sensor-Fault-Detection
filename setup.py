# Just to create proper packages, libraries so that it can be shared and used for multiple purposes

from setuptools import find_packages,setup
from typing import List     # The typing module provides us with Type Aliases, which is defined by assigning a type to the alias.

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []
    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="vinit",
    author_email="vinit.londhe21@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()  #["pymongo==4.2.0"]
)


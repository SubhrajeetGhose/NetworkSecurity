'''
The setup.py file is an part of packaging and distribution of a Python project. 
It is used by setuptools (or distutils in older Python versions) 
to define the configuration of the project, such as its metadata, dependencies, and more.
'''

from setuptools import setup, find_packages
from typing import List



def get_requirements()->List[str]:
    """
    Thiss function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")



    return requirement_lst

print(get_requirements())


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Subhrajit Ghose",
    author_email="subhrajeetghose5@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
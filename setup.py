
# from setuptools import setup
from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.3"
AUTHOR = "Nikita"
DESCRIPTION = "project on housing"
# PACKAGES =["housing"] #list of the names of the packages
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:

    """
    Description: This function is going to return list of requiremnet 
    mentioned in requirements.txt file.

    return This function is going to return a list of libraries. 
    """

    with open(REQUIREMENT_FILE_NAME, 'r') as requirement_file:
        return requirement_file.readlines().remove("-e .") #removing this because we already using find_packages() which is equivalent to -e .

setup(

    name= PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description=DESCRIPTION,
    packages = find_packages(), #any module present in the root directory will be passed as a list. wherever there is __init__.py #["housing"]
    install_requires = get_requirements_list()
)


# if __name__=="__main__":
#     print(get_requirements_list())


#to run this file do 
# python setup.py install
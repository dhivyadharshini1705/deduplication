from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this fuction will return the list of requirements
    '''
    reqiurements=[]
    with open(file_path) as file_obj:
        reqiurements=file_obj.readlines()
        reqiurements = [req.replace("/n", "") for req in reqiurements]

        if HYPEN_E_DOT in reqiurements:
            reqiurements.remove(HYPEN_E_DOT)
    
    return reqiurements

setup(
name='deduplication',
version='0.0.1',
author='Dhivya',
author_email='dhivya17@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
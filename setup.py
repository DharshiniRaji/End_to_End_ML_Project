from setuptools import setup, find_packages
from typing import List

hypen_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    Returns a list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("/n","")for req in requirements]
        
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements


setup(
name = 'End_to_End_ML_Project',
version = '0.0.1',
author = 'Dharshini',
author_email = 'dharshiniraji1520@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')


)
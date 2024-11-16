from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(path:str)->List[str]:
    """
    This function returns the list of requirements from the requirements file
    """
    
    reqs = []
    with open(path, 'r') as f:
        lines = f.readlines()
        reqs = [line.replace("\n","").strip() for line in lines]
    
    if HYPHEN_E_DOT in reqs:
        reqs.remove(HYPHEN_E_DOT)
        
    return reqs

setup(
    name='success_predictor',
    version='0.0.1',
    author="Abid Talukder",
    author_email="abidtalukder12@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
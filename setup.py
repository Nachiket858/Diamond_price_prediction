from setuptools import setup , find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path,'r') as f:
        requirements=f.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        return requirements

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author ='Nachiket Shinde',
    author_email='nachiketshinde8766@gmail.com',
    install_requires = get_requirements("requirements.txt"),
    packages=find_packages()

)
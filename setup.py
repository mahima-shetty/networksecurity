from setuptools import find_packages, setup # scans all the folders - find __init__.py and consider it parent folder as packages
from typing import List

def get_requirements() -> List[str]:
    """
    
    Returns List of strings (requirements list)
    
    """
    requirement_lst :List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            #read lines from file
        
            lines = file.readlines()
            ##Process each line
            for line in lines:
                requirement=line.strip()
                ##ignore empty lines and -e.
                if requirement and requirement!= '-e.':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')
        
        
    return requirement_lst

# print (get_requirements())

setup (
    name = "Network Security",
    version = "0.0.1",
    author = "Mahima Shetty",
    author_email="msshetty237@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)
    

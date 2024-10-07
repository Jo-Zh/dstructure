from setuptools import setup, find_packages

setup(
    name='mol_to_img',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=4.0',  
        'rdkit',         # Include rdkit
        'cairoSVG',      # Include cairoSVG
    ],
)

from setuptools import setup, find_packages

setup(
    name="projecteuler",
    version="1.0",
    packages=find_packages(exclude=['*test.py']),
    scripts=['runtests.bat'],
    
    author="Sam",
    author_email="levinsamuel000@gmail.com",
    url="https://github.com/levinsamuel/projecteuler",
    install_requires=[
        'numpy'
    ]
)
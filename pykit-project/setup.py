

from setuptools import setup, find_packages
import os


this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pykit-shyamal',
    version='0.1.0',
    author='Shyamal',
    author_email='kudipudishaymal0123@gmail.com',
    description='A Pragmatic Utility Library for Modern Python Development',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/shyamal005/pykit',  
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    keywords='utility utils tools helpers library',
    project_urls={
        'Bug Reports': 'https://github.com/shyamal005/pykit/issues',
        'Source': 'https://github.com/shyamal005/pykit/',
    },
)

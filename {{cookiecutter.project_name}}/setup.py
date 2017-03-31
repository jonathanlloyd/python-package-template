from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '{{cookiecutter.version}}'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    dependency_links=dependency_links,
    description='{{cookiecutter.project_description}}',
    include_package_data=True,
    install_requires=install_requires,
    long_description=long_description,
    name='{{cookiecutter.project_name}}',
    packages=find_packages(exclude=['tests']),
    version=__version__,
)

#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='ithenticate-api-python',
      version='0.7',
      url='https://github.com/JorrandeWit/ithenticate-api-python',
      author="Jorran de Wit",
      author_email="jorrandewit@outlook.com",
      description="iThenticate API Client",
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
      license='BSD',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'requests'
      ])

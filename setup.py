#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages
import yowsup
import platform
import sys

deps = ['python-dateutil', 'argparse', 'python-axolotl>=0.1.39', 'six', 'blinker', 'pillow', 'moviepy', 'audioread', 'preview-generator']

if sys.version_info < (2,7):
    deps += ['importlib']

if platform.system().lower() == "windows":
    deps.append('pyreadline')
else:
    try:
        import readline
    except ImportError:
        deps.append('readline')

setup(
    name='yowsup2',
    version=yowsup.__version__,
    url='http://github.com/danielcardeenas/yowsup/',
    license='GPL-3+',
    author='Tarek Galal, Daniel Cardenas',
    tests_require=[],
    install_requires = deps,
    scripts = ['yowsup-cli'],
    #cmdclass={'test': PyTest},
    author_email='danielcardeenas@gmail.com',
    description='A WhatsApp python library',
    #long_description=long_description,
    packages= find_packages(),
    include_package_data=True,
    data_files = [('yowsup/common', ['yowsup/common/mime.types'])],
    platforms='any',
    #test_suite='',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        #'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
    #extras_require={
    #    'testing': ['pytest'],
    #}
)
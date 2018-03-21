'''
https://stackoverflow.com/a/21530768/3166424
Need to install python dev
python setup.py build
'''
from distutils.core import setup, Extension, DEBUG

sfc_module = Extension('superfastcode', sources = ['main1.cpp'])

setup(name = 'superfastcode',
    version = '1.0',
    description = 'Python Package with superfastcode C++ extension',
    ext_modules = [sfc_module]
    )
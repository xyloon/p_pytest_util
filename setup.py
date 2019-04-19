from setuptools import find_packages, setup
from ptrait import __version__

setup(name='p_pytest_util',
      version=__version__,
      description='p_pytest_util',
      long_description='',
      url='https://github.com/xyloon/p_pytest_util',
      author='xyloon',
      author_email='xyloon@gmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      zip_safe=False)

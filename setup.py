import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='dbbs-scaffold',
     version='2.3.0',
     author="Robin De Schepper, Alice Geminiani, Elisa Marenzi, Stefano Casali, Claudia Casselato, Egidio D'Angelo",
     author_email="robingilbert.deschepper@unipv.it",
     description="A morphologically detailed scaffolding package for the scientific modelling of the cerebellum.",
     scripts=['bin/scaffold', 'bin/scaffold.bat'],
     include_package_data=True,
     data_files=[
        ('configurations', ['scaffold/configurations/mouse_cerebellum.json'])
     ],
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/dbbs-lab/scaffold",
     license='GPLv3',
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
     install_requires= [
         'cycler>=0.10.0',
         'h5py>=2.9.0',
         'kiwisolver>=1.1.0',
         'matplotlib>=3.1.1',
         'mkl-fft>=1.0.6',
         'mkl-random>=1.0',
         'mock>=2.0',
         'numpy>=1.16.4',
         'pyparsing>=2.4.2',
         'pyreadline>=2.1',
         'python-dateutil>=2.8.0',
         'pytz>=2019.2',
         'readme-renderer>=24.0',
         'requests-toolbelt>=0.9.1',
         'scikit-learn>=0.20.3',
         'scipy>=1.3.1',
         'six>=1.12.0',
         'tornado>=6.0.3',
         'twine>=1.13.0',
         'wincertstore>=0.2',
     ]
 )

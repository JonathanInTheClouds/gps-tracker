from setuptools import setup, find_packages

setup(
    name='gps-tracker',
    version='1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pyserial',
        'PyYAML',
        'gpsd-py3',
        'pytest'
    ],
)

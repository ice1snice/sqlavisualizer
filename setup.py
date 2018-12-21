import setuptools

version = '0.0.1'

with open('requirements.txt') as requirements:
    requires = [line.strip() for line in requirements.readlines()]


setuptools.setup(
    name='edu-flask-utils',
    version=version,
    packages=setuptools.find_packages(),
    install_requires=requires,
)

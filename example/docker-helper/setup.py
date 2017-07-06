from setuptools import setup, find_packages

setup(
    name='docker-helper',
    version='0.1.0.dev0',
    author='Jamie Hewland',
    author_email='jamie@praekelt.org',
    packages=find_packages(),
    install_requires=[
        'docker >= 2.4.0',
    ],
)

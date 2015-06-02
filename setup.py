from setuptools import setup

setup(
    name='histogram',
    version='0.1',
    description='a histogram class',
    url='http://github.com/MaxNoe/histogram',
    author='Maximilian Nöthe',
    author_email='maximilian.noethe@tu-dortmund.de',
    license='MIT',
    packages=['histogram'],
    install_requires=[
        'numpy',
    ],
)

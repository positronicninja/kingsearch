from setuptools import setup

setup(
    name='kingsearch',
    packages=['kingsearch'],
    include_package_data=True,
    install_requires=[
        'flask',
        'nltk',
    ],
)

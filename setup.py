from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

VERSION = '1.0.0'
DESCRIPTION = 'Flatten nested Python lists into a single-depth list'

setup(
    name="flatifylists",
    version=VERSION,
    author="Karishma Shukla",
    author_email="karishmashuklaa@gmail.com",
    url="https://github.com/karishmashuklaa/flatifyLists",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description= readme(),
    packages=find_packages(),
    install_requires=['pytest'],
    keywords=['flatten', 'lists', 'nested-lists', 'flatten-lists', 'nesting', 'flatify-list'],
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="spam",
    version="0.0.1",
    description="Classifies a text as Spam or Ham",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bnriiitb/spam-classifier",
    author="Naga Budigam",
    author_email="nagaraju.iith@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["pandas", "scikit_learn>=1.0.1"],
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)

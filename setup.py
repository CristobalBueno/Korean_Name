from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="Korean_name",
    version="0.0.1",
    description="A small example package, that returns your name based on date of birth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="CristobalB.",
    url="https://www.linkedin.com/in/crist%C3%B3balbuenocantarero/",
    packages=["Package"]
    )


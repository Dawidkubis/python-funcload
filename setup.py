import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="funcload",
    version="0.0.1",
    author="Dawid J. Kubis",
    author_email="dawid.kubis3@gmail.com",
    description="A simple package for loading function variables into the current interactive session",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dawidkubis/python-funcload",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


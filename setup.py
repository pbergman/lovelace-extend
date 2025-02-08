from setuptools import setup, find_packages

setup(
    name="lovelace_extend",
    version="0.6",
    packages=find_packages(),
    install_requires=['homeassistant>=2024.12.5'],
    author="Philip Bergman",
    author_email="pbergman@live.nl",
    description="Abstract base classes for the hass lovelace extend custom components",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pbergman/lovelace_extend",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.13',
)
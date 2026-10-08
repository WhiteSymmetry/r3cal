# -*- coding: utf-8 -*-
import io
import re
from setuptools import setup, find_packages
import sys
import os

# UTF-8 encoding sorunlarını çöz
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def get_version():
    with open('r3cal/__init__.py', 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", content, re.M)
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find version string.")

def get_install_requires():
    """Kurulum bağımlılıklarını dinamik olarak belirle"""
    base_requires = [

    ]

setup(
    name="r3cal",
    version=get_version(),
    description="r3cal: Resistor Color Code Calculator: Direnç Renk Kodu Hesaplayıcı Modülü",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mehmet Keçeci",
    maintainer="Mehmet Keçeci",
    author_email="enfo@tuta.io",
    maintainer_email="enfo@tuta.io",
    url="https://github.com/WhiteSymmetry/r3cal",
    packages=find_packages(),
    package_data={
        "r3cal": ["__init__.py", "_version.py", "*.pyi"]
    },
    install_requires=get_install_requires(),
    extras_require={
        'test': [
            "pytest",
            "pytest-cov",
        ],
        'dev': [
            "pytest",
            "pytest-cov",
            "twine",
            "wheel",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    python_requires='>=3.11',
    license="AGPL-3.0-or-later",
    keywords="r3cal, resistor, direnç",
    project_urls={
        "Documentation": "https://github.com/WhiteSymmetry/r3cal",
        "Source": "https://github.com/WhiteSymmetry/r3cal",
        "Tracker": "https://github.com/WhiteSymmetry/r3cal/issues",
    },
)

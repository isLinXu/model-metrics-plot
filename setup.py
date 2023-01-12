import os
import subprocess
import time
import setuptools
from setuptools import find_packages, setup
import io
from os import path

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

version_file = "mmplot/version.py"


def get_version():
    with open(version_file, "r") as f:
        exec(compile(f.read(), version_file, "exec"))
    return locals()["__version__"]


setuptools.setup(
    name="mmplot",
    version=get_version(),
    description="mmp is a plotting library for plotting metrics of deep learning models",
    long_description="",
    author="isLinXu",
    author_email="islinxu@163.com",
    keywords="computer vision, object detection，plotting, metrics",
    url="https://github.com/isLinXu/model-metrics-plot",
    package_dir={'':"mmplot"},
    # packages=find_packages(exclude=("utils", "core")),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    license="GPL",
    zip_safe=False,
)

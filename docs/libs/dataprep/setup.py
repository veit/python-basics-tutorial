from Cython.Build import cythonize
from setuptools import find_packages, setup

setup(
    ext_modules=cythonize("src/dataprep/cymean.pyx"),
)

from setuptools import setup
from Cython.Build import cythonize

# ! Deprecated
# ! Cythonize Not Used in Project

setup (
    ext_modules = cythonize('console/log.pyx')
)
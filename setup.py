from setuptools import setup, Extension
from Cython.Distutils import build_ext

NAME = "practice_leetcode"
VERSION = "0.1"
DESCR = "practice_leetcode"
URL = "http://www.google.com"
REQUIRES = ['cython']

AUTHOR = "Ching-Hua, Yang"
EMAIL = "penolove15@gmail.com"\

LICENSE = "Apache 2.0"

PACKAGES = []


ext_55 = Extension("leetcode.cython_55",
                   ["leetcode/55/cython_jump.pyx"],
                   libraries=[],
                   include_dirs=[],
                   language="c++")

# for the leetcode question 56
ext_56 = Extension("leetcode.cython_56",
                   ["leetcode/56/cython_merge.pyx"],
                   libraries=[],
                   include_dirs=[])

EXTENSIONS = [ext_56, ext_55]

if __name__ == "__main__":
    setup(install_requires=REQUIRES,
          packages=PACKAGES,
          zip_safe=False,
          name=NAME,
          version=VERSION,
          description=DESCR,
          author=AUTHOR,
          author_email=EMAIL,
          url=URL,
          license=LICENSE,
          cmdclass={"build_ext": build_ext},
          ext_modules=EXTENSIONS
          )

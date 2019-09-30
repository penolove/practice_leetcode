# practice leetcode

this repo is used to practice leetcode but keep good python manner

restrictions:
- the implemented method should pass the leetcode evaluation
- the implemented method should pass the flake8 check

optional:
- add unittest
- add performance benchmark
- add Cython implementation


## check if test pass every time before commit
```
flake8
# if you are using ipdb to debug please set the -s flag
coverage run -m pytest --verbose
```

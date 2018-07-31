---
layout: blogpost
title: Session 13
---

# Writing a Distributable Package

### Suggested Readings

* Automate Stuff: Chapter 17
* If you are not familiar with git or a modern revision control
  system, the following chapters of the (free!)
  [Pro Git](https://git-scm.com/book/en/v2) book are recommended:
  Chapters 1\*, 2\*, 3\*

### Suggested Exercises

* As was done in this session, take some module that you have written and
  turn it into a distributable python package with a `setup.py`, some basic
  unit tests, revision control.
  * Upload it to PyPA using twine. If you have something that you think other
    researchers can benefit from, upload to the real PyPA server. If you are
    not comfortable taking that step, upload to the test PyPA server.
* Once you have a project in GitHub or another distributed revision control
  server, have a friend submit a Pull Request with an improvement and review
  the request. Do the same for your friend's test project.

---

### Session Notes

* Start by making an `smath2018x` repository in github
  * Go over [choosing a license](https://choosealicense.com/)
  * Basic math functions, `fib`, etc...
  * Add some tests

* Follow [Python Packaging](https://packaging.python.org/tutorials/packaging-projects/)
  tutorial for general setup
  * Also look at Kenneth Reitz's [setup.py](https://github.com/kennethreitz/setup.py)

* Use tox as a test runner, hook into Travis-CI

* To be continued...


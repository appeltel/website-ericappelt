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

#### Package Basics

* Start by making an `smath2018x` repository in github
  * Go over [choosing a license](https://choosealicense.com/)
  * Basic math functions, `fib`, etc...

* Follow [Python Packaging](https://packaging.python.org/tutorials/packaging-projects/)
  tutorial for general setup
  * Also look at Kenneth Reitz's [setup.py](https://github.com/kennethreitz/setup.py)
  * Create a very basic setup.py to start

{% highlight python %}
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smath2018b",
    version="0.0.1",
    author="Eric Appelt",
    author_email="eric.appelt@gmail.com",
    description="Serious Math",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/appeltel/smath2018b",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
{% endhighlight %}

* Now create a venv in the repo base directory, `python -m venv venv`
  and use this to install packages for creating the release artifacts,
  activate the venv
* Need to have the latest setuptools, `pip install setuptools --upgrade`
* Need to have the wheel package, `pip install wheel`
* To build release artifacts, use `python setup.py sdist bdist_wheel`
* Now you have release artifacts created in the dist directory
  * You can use `pip install -f <filename>` to install the archive file
    directly. You can use either the wheel or the source tarball.
  * You could simply email the source artifact for collaborators to use
    or make it available online

#### Adding a CLI utility

Lets create a function `fib_cli` which expects a command line argument
for the number and prints the Fibonacci number and exits

{% highlight python %}
def fib_cli():
    """
    Command line interface for fib
    """
    n = int(sys.argv[1])
    print('fib({0}) = {1}'.format(n, fib(n)))
    sys.exit(0)
{% endhighlight %}

Now add the following to setup.py:

```
    entry_points={
        'console_scripts': ['fib=smath2018b.fib:fib_cli'],
    },
```

#### Testing

* Show usage of `pip install -e .` to be able to work interactively on the
  package
* Create a tests directory, put test modules in there, use pytest and
  auto-discover the tests

Install tox in the venv, make a tox.ini file:

```
[tox]
envlist = {py34,py35,py36}
[testenv]
deps =
    pytest
commands = py.test
```

If you don't have all those python versions installed, you can remove them
from the ini, but they are useful for Travis (below).

You can easily use Travis Continuous Integration to automatically run
your tests every time you push a commit to GitHub, or (more advanced) set
up your own CI system. Here we'll demo Travis.

Here's a Travis yml config to use tox:

```
language: python
python:
  - "3.4"
  - "3.5"
  - "3.6"
install: pip install tox-travis
script: tox
```

* Do an example pull request with a new feature and check with Travis

#### Linting

Install `pyflakes` and `pycodestyle`. Run these commands on the repo and
see if any errors occur.

* Try adding a wrong (5-character) indentation and see what pycodestyle does.
* Look at the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide.
* Try adding an unused import and see what pyflakes says.
* Try adding linters to Travis

#### Documentation

Install `sphinx` package into the venv

* Setup with `sphinx-quickstart`, discuss the options
* Use `sphinx-apidoc -o docs smath2018b` to generate autodocs
* Edit `index.rst` to add some text.
* Use `make html` to build the pages, and inspect

* Mention [ReadTheDocs](https://readthedocs.org/)


#### Publishing

Install twine into the venv

* Make a [test PyPI account](https://test.pypi.org/account/register/)
* Upload with twine `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
* Try installing the package in a fresh venv `pip install -i https://test.pypi.org/simple/ smath2018b`


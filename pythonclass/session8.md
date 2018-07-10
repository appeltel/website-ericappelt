---
layout: blogpost
title: Session 7
---

# Packages and PyTest

### Suggested Readings

* Automate Stuff: Chapter 12
* Learning Python: Chapters 24\*, 25\*

### Suggested Exercises

* Do some Test-Driven Development (TDD):
  * Define a function that takes a positive integer and returns the double
    factorial. The double factorial is defined differently for even and odd
    numbers. For example, `9!! = 9 * 7 * 5 * 3 * 1` and `6!! = 6 * 4 * 2`.
    The double factorial of zero is `0!! = 1`. Don't actually implement the
    function, just define it in a module and add a nice docstring.
    Otherwise leave the function body blank.
  * Now write some unit tests for the function that you haven't implemented
    yet. These tests should check that the function returns the right value
    for `0`, `1`, `2`, and a larger even and odd number.
    They should also make sure that a `ValueError` is raised for a negative
    number. Run the tests, which should all fail.
  * Implement the function body to return the correct double factorial.
    When you think you have done this correctly, run the test to ensure
    the validity of your implementation.
* Try out a third party-library:
  * Create a virtual environment with venv
  * Use pip to install pillow, an image manipulation library
  * Now write a python script to take an image file from the command line
    and make a 128 x 128 thumbnail of the image (check out the pillow
    tutorial for help).

---

### Session Notes

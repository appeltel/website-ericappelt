---
layout: blogpost
title: Session 12
---

# Functional Programming, Lambdas, and Decorators

### Suggested Readings

* Automate Stuff: Chapter 16
* Learning Python: Chapters 35, 36, 39\*

### Suggested Exercises

* Write a `calllog` decorator that causes a function
  to be logged when called with
  all arguments to the function and the return value printed in the log entry.
  * Make sure to use `functools.wraps` to retain docstrings
  * Make a number of test functions to use it on in a separate module
* Add a capability to your logging decorator module to call a function to
  turn on or off the logging of function calls. It's ok to use a global
  variable to control if logging calls is enabled.
* Add a capability to count the number of function calls made by each function
  when the call is logged. You can use a global dict for keeping track.
* (challenge) Create a "decorator factory" version of the logging decorator
  where you apply it to a function like `@calllog('DEBUG')` and pass it a
  level at which to log the function. The trick to using this notation is that
  `calllog` must now be a function that returns a decorator based on the level
  argument.

---

### Session Notes

---

### Preliminary Session Notes

These are scanned, handwritten notes to be replaced with typed notes:

* [Preliminary Session Notes](Python_lesson_12.pdf)

I will keep these available until the typed and updated notes are complete.

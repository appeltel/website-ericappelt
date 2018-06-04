---
layout: blogpost
title: Session 5
---

# Functions

### Suggested Readings

* Learning Python: Chapters 16\*, 17\*, 18\*

### Suggested Exercises

* Write a new temperature converter program written entirely in functions,
  that simply calls a `main()` function to run the interactive loop, with
  the following constraints:
  * There should be a function that takes a string of the form `23.4 K`,
    determines if it is Kelvin, Celsius, or Fahrenheit, and returns a
     3-tuple of numbers representing the temperature in C/K/F. An invalid
     string should raise an exception.
  * There should be a function that takes the 3-tuple of numbers representing
     C/K/F and prints a nicely formatted output of the temperatures to the screen
  * The main loop should prompt the user to input temperatures or quit and run
     a loop. The menu/prompt string should be a global constant.

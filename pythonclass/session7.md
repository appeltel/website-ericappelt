---
layout: blogpost
title: Session 7
---

# Modules, Dates, OS Functions, and Virtual Environments

### Suggested Readings

* Automate Stuff: Chapter 11
* Learning Python: Chapters 22\*, 23\*

### Suggested Exercises

* Write a module with a public function that takes a directory path as
  an argument and returns a dictionary all (regular) file names and
  their associated size in bytes
  * Hint: Use `os.listdir` for directory contents, `os.is_file` to
    filter non-regular files, and `os.stat` to get sizes.
  * Allow the module to be run as a script, in which case it should
    (nicely) print the sizes for all files in the current directory.
    If the module is imported it should not do this.
* Add another function similar to the first but that returns a dictionary
  of the file names and the number of days since each file was modified
  * Hint: Use `datetime.fromtimestamp(...)` and the `st_mtime` attribute
    of the `os.stat(...)` result to manipulate the modification time as
    a datetime object.

---

### Session Notes

#### Modules

* Modules are the basic unit of encapsulation in python!!!

Each python source file is a module, and each module defines its own namespace.
While python has classes, the fundamental method of encapsulating code
is within modules.

* Try `import this` and look at the last line of the poem!

Let's start with an example module, `smath.py`:

{% highlight python %}
"""
Serious math for serious people
"""
print('Initializing the smath module')


PI = 3.14
_PHI = 1.618


def circle_area(r):
    """
    Return the area of a circle given the radius
    """
    return PI * r**2


def square(x):
    """
    Return the square of a number
    """
    return x*x


def fib(n):
    """
    Return the nth Fibonacci number
    """
    if n < 0:
        raise ValueError(
            '{} is not a non-negative integer'.format(n)
        )
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
{% endhighlight %}

* Note that the first line of the module is a docstring. You can run
  `help(...)` on a module and it will print this docstring. For stand alone
  modules, authorship information often goes here.
* Note the `print(...)` function. Try running `import smath` and see how
  the function is run and prints to the screen. Importing a module in python
  does three things:
  * It runs the actual module code. Most modules only define functions,
    classes, and constants, so you may not notice anything happening.
  * It adds a module object to a system dictionary of loaded modules. A
    module is only run on the first import. Subsequent imports just fetch
    the object.
  * It binds the module object to the name of the module in your current
    namespace. With the module imported, you can access its namespace like
    you would any other object attribute, i.e. `smath.square(10)`.

---

### Preliminary Session Notes

These are scanned, handwritten notes to be replaced with typed notes:

* [Preliminary Session Notes](Python_lesson_7.pdf)

I will keep these available until the typed and updated notes are complete.

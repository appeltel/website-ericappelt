---
layout: blogpost
title: Session 6
---

# Exceptions, Logging, and Context Managers

### Suggested Readings

* Automate Stuff: Chapter 10\*
* Learning Python: Chapters 19, 20, 21

### Suggested Exercises

* Write a command line utility in python that counts the number of lines
  in a file and prints them. to standard output.
  * The utility should take the name of a file as an argument. To do
    this use `import sys` and then `sys.argv[1]` will be the first
    argument given.
  * By trial and error, determine the type of exception raised when the
    user fails to run the program with an argument, the file specified does
    not exist, or the user does not have permission to read the file specified.
  * using try/except blocks, handle each of these exception types separately
    and send an appropriate message to the user in each case.

---

### Session Notes

#### Handling exceptions

In python, exceptions are handled using a try/except block. Here is an
example handling a `ValueError` raised from the previous Fibonacci function
due to a negative number:

{% highlight python %}
def fib(n, a=0, b=1):
    """
    Return the nth number in the Fibonacci sequence
    """
    if n < 0:
        raise ValueError('Cannot accept a negative number: {}'.format(n))
    for _ in range(n):
        a, b = b, a + b
    return a

try:
    raw_num = input('Enter an integer: ')
    num = int(raw_num)
    result = fib(num)
    print('The {}th Fibonacci Number is {}'.format(num, result))
except ValueError:
    print('{} is not a positive integer'.format(raw_num))
{% endhighlight %}

When executed, an exception raised within the call to `fib` will be caught
by the except clause, and the `print` function will be executed.

The general form of a try/except compound statement is as follows:

```
try:
    statement
    statement
    ...
    statement
except <exception> [as <name>]:
    statement
    statement
    ...
    statement
except <exception> [as <name>]:
    statement
    statement
    ...
    statement
else:
    statement
    statement
    ...
    statement
finally:
    statement
    statement
    ...
    statement
```

* Zero or more `except` blocks can be used to catch different types of
  exceptions and handle them differently. An except block can also accept
  a tuple of exception types rather than a single type of exception.
* Each `except` block can optionally have an `as <name>` clause to store the
  raised exception object as the specified name so that it can be accessed
  in the handling code.
* The `else` clause will be executed if no exceptions are raised.
* The `finally` clause will *always* be executed, even if the try block
  raises an exception that is not handled. It can be used for safe cleanup
  of resources.

Try doing variations of exception handling with the `fib` function above
adding multiple except clauses, else, and finally.

Another good example to work with uses the `urllib` and handles a
404 not found:

{% highlight python %}
import urllib.request

try:
    url = input('Enter a URL: ')
    response = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print('Got an error code {}'.format(e.code))
{% endhighlight %}

* Try re-raising the exception if the error code is not 404. You can re-raise
  an exception in an except block with an empty `raise` statement
* Try handling `urllib.error.URLError` exceptions in a second except block
  for servers that do not respond at all
* Try doing something with the response like counting bytes

#### When to raise exceptions, when to catch them?

When to use exceptions is a somewhat controversial topic in
software engineering, with varying schools of thought. One general rule of
thumb is not to use exceptions for flow control, that is - don't use
exceptions to handle logic that could be handled with loops, break/continue,
if statements, and so forth. Taken to the extreme, this can effectively mean
not to use exceptions at all. Another common suggestion is to only use
exceptions for "unexpected" cases. But how do you code against things you
don't expect to happen?

*MY OPINION*: Each function should always return an object of the same type
with a specified meaning. For example, if I have a function that takes a URL
and returns the size of the server response in bytes, then it should always
return a positive integer representing the response size. If there is no
response, and it can't do that, then it shouldn't return anything at all, but
raise an exception.

Should exceptions be caught???

* YES - if we are ok with the error condition and can/should continue
  processing or retry the operation.
* NO - if we don't know what to do in this case or didn't expect the
  condition. (It's ok to not know).

In any case, if you catch an exception and continue in spite of it, you
should generally log the problem somewhere so that it doesn't pass unnoticed.
Code like the code below should be avoided:

{% highlight python %}
try:
    statement
    ...
    statement
except Exception:  # ignore all errors
    pass
{% endhighlight %}

In this case if there are unexpected errors then it will be very hard to
debug problems as they are silently removed!

#### Logging

Python comes with a useful logging utility as part of the standard library.
It allows one to create multiple "logger" objects, each with its own
configuration in terms of how messages are formatted, where they go, and
how verbose your program will be. Generally log messages have an associated
"level" of DEBUG, INFO, WARNING, ERROR, and CRITICAL. You can configure your
program to only log messages above a certain level, and change that level
if you need to further debug.

A good introduction is given in the
[logging cookbook](https://docs.python.org/3/howto/logging-cookbook.html)
in the official python documentation. Following this introduction, here is
our Fibonacci program with added logging:

{% highlight python %}
import logging

logger = logging.getLogger('fib')

logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.CRITICAL)

fh = logging.FileHandler('fib.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s : %(name)s - %(levelname)s - %(message)s'
)
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

def fib(n, a=0, b=1):
    """
    Return the nth number in the Fibonacci sequence
    """
    if n < 0:
        raise ValueError('Cannot accept a negative number: {}'.format(n))
    for _ in range(n):
        a, b = b, a + b
    return a

try:
    raw_num = input('Enter an integer: ')
    logger.debug('The user entered a number: %s', raw_num)
    num = int(raw_num)
    result = fib(num)
    print('The {}th Fibonacci Number is {}'.format(num, result))
except ValueError:
    logger.exception('An invalid number %s was entered', raw_num)
    print('{} is not a positive integer'.format(raw_num))
{% endhighlight %}

* Try modifying the log level of each of the two handlers and run the
  program, and note what is written to the `fib.log` file in each case.
* Note that `logger.exception` is equivalent to ERROR in terms of level,
  but unlike `logger.error` the exception method will print the stack trace
  for the exception.
* Try using info and warning level statements, and see how these appear in
  the log.
* Notice that the logging statements use a variation of the "old-style"
  python formatting with a `%s` in the string and an additional argument for
  the value. You can also use a format string, but the "old-style" usage is
  preferred here as you don't want another exception being raised due to
  a potentially failed format statement.

#### A note about exception speed

Exception handling is often considered slow. In the reference implementation
of python (CPython), handling exceptions is not any slower than other
language constructs. In fact, in cases where an exception is rarely raised
a try/catch block will sometimes execute faster than an equivalent if/then.

#### Context managers

Basic syntax:

```
with <context manager> as <name>:
    statement
    statement
    ...
    statement
```

A context manager is an object used in a `with` statement. This statement
will implicitly call a special `__enter__` function on the context manager
object and return the result. When the with-block ends, either by normal
execution or from an uncaught exception, the interpreter will *always* call
a special `__exit__` statement allowing for cleanup.

The `open(...)` builtin function is a good example of something that can
be used as a context manager:

{% highlight python %}
with open('fib.log') as stream:
    for line in stream:
        print(line, end='')
{% endhighlight %}

The use of this construct ensures that your file will always be closed
at the end of the block, so you don't need to worry about ensuring any
cleanup with a try/finally block.

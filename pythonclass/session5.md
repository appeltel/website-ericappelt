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

---

### Session Notes

#### Defining a function

Fibonacci example:

{% highlight python %}
def fib(n):
    """
    Return the nth Fibonacci number
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
{% endhighlight %}

* The `def` statement provides a function name that the new function object
  will be bound to, and in parenthesis a comma separated list of parameters
  that can be passed to the function.
* An indented suite of statements follows to form the function body. These
  are executed when the function is called
* If the first statement in the suite is a string literal expression
  statement, then this string becomes the function's docstring. Using a
  docstring is an important way to document functions (more on this later)
* One or more `return` statements may halt the function execution and return
  an expression. If no expression is given, `None` is returned.
* If a function suite ends without a return statement, the function returns
  `None` by default. A function always returns *something*!

#### Calling a Function

* Try calling `fib` with `fib(4)`, `fib(8)`, `fib(n=7)` (keyword)
* Also try `fib()`, `fib(4, 3)`, and `fib(a=7)` and observe errors.

#### A bit on Variable Scope

Prior to this session, there was no notion of variable scope. Once a name
was bound to an object with assignment, it was bound everywhere until either
reassigned or `del`ed. A function definition provides a local scope inside
its suite of instructions. If a name is bound by assignment inside the function
body, that becomes a *local name* that is completely separate from any
corresponding *global name*.

For example, notice how `fib` uses the names `n` and `a`. These are local
to the function. If we bound `a` and `n` outside the function, these are
separate global names and are not affected by the use of `n` and `a` inside
the function body:

```
>>> a = 3
>>> n = 7
>>> fib(8)
21
>>> n
7
>>> a
3
```

More on scope later!!!

#### Parameter default values

Python functions can have default values for parameters allowing these
parameters to be *optionally* specified when the function is called.
As an example, lets change the `fib` function to allow initial values for
`fib(0)` and `fib(1)` to be specified for variations on the classic
sequence:

{% highlight python %}
def fib(n, a=0, b=1):
    """
    Return the nth Fibonacci number
    """
    for _ in range(n):
        a, b = b, a + b
    return a
{% endhighlight %}

Try calling this in various ways and see what happens:

* `fib(8)`
* `fib(8, a=2, b=2)`
* `fib(8, b=2, a=2)`
* `fib(8, a=2)`
* `fib(8, 2)`
* `fib(8, b=2)`

#### Some Important Style / Engineering Suggestions

* Use default values anywhere that they make sense. Never call functions
  using more than a few (or even one!) positional parameter. Use keyword
  parameters for readability and to avoid getting the order wrong.
* Put most (even all!) of your code into functions. A script can just call
  a `main()` function at the end to do the work. Make functions *small*,
  focusing on a single task. Test functions interactively as you write them.

#### Side Effects

Functions can do more than just return a value. They can alter mutable
objects, print to the screen, open files, and send data over the network.
These are called side effects.

Example:

{% highlight python %}
def extend_fib(target, n):
    """
    Extend the target list with the first n Fibonacci numbers
    """
    print('Extending target list')
    target.extend([fib(x) for x in range(n)])
{% endhighlight %}

```
>>> mylist = [1, 2, 3]
>>> extend_fib(mylist, 5)
Extending target list
>>> mylist
[1, 2, 3, 0, 1, 1, 2, 3]
```

*Style Suggestion*: A function is called "pure" if it has no side effects and
the return value is always the same given the same inputs. Pure functions
are easy to reason about, debug, and test. If you move most of your code
into pure functions then you will become a happy person!

#### Return values and raising exceptions

This is an example of a poorly written function that tries to return
an error value when a negative number is passed to it:

{% highlight python %}
def fib(n, a=0, b=1):
    """
    Return the nth Fibonacci number
    """
    if n < 0:
        return "Invalid negative number"
    for _ in range(n):
        a, b = b, a + b
    return a
{% endhighlight %}

While a bad idea, this function does illustrate how you can have multiple
return statements. One good thing about this is that it avoids excessive
nesting, it is at least better than this:

{% highlight python %}
def fib(n, a=0, b=1):
    """
    Return the nth Fibonacci number
    """
    if n < 0:
        result = "Invalid negative number"
    else:
        for _ in range(n):
            a, b = b, a + b
        result = a
    return result
{% endhighlight %}

However, in either form, returning a sentinel value to designate an error
can have weird and unexpected effects. Consider some code that calls the
function and tries to multiply the result by an integer:

```
>>> fib(-5) * 3
'Invalid negative numberInvalid negative numberInvalid negative number'
```

This could result in very difficult to debug code. 

*STYLE SUGGESTION*: Functions should always return the same type. Its ok
to return different types if the input parameters were of different types,
for example a function could return an int if passed an int, or a float if
passed a float, but generally speaking, if a function takes input of a given
type, than the specific value of the input should not change the return type.

Sentinel values should also be avoided. We could have the `fib()` function
return something like `-1` to designate an invalid input. However, if the
consumer of the function is not careful to check for special values then
they may handle the error inappropriately and the result might be hard to
debug.

A better and more "pythonic" approach is to raise an Exception when its not
possible to return a valid result.

Raising an exception distrupts the normal flow of execution. All statements
are skipped until something "catches" the exception. Catching exceptions
will be discussed in the next session. For now, allowing an exception to
go uncaught is useful in that it supplies the end user with useful
debugging information to report when an unexpected condition occurs.

An uncaught exception will end a running python program and emit a stack
trace, which outlines where in each function call the program was when the
exception occurred. In the case of the interactive REPL, the exception will
be caught by the REPL and the stack trace printed to the screen.

Here is a better implementation of the function that raises an exception
with a "raise" statement:

{% highlight python %}
def fib(n, a=0, b=1):
    """
    Return the nth Fibonacci number
    """
    if n < 0:
        raise Exception("{} is a negative number.".format(n))
    for _ in range(n):
        a, b = b, a + b
    return a
{% endhighlight %}

Here is the exception being raised:
```
>>> fib(8)
21
>>> fib(-4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fib.py", line 6, in fib
    raise Exception("{} is a negative number.".format(n))
Exception: -4 is a negative number.
```

The stack trace explains exactly where the problem occurred, and if the
exception is written to have a useful message, then it is easy to try to
understand the bad state that led to the problem.

`Exception` is a very generic exception type. Python provides a number
of built-in exception types that can be raised as the situation dictates.
Raising a more specific exception helps code that catches exceptions to
decide what sort of error should be caught. The python library reference
details these specific types. In this case a
[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)
is the appropriate exception to raise, as the issue is that the parameter
was the correct type but an invalid value, and there is no more specific
exception type to describe this problem. So here is a better version of the
function:


{% highlight python %}
def fib(n, a=0, b=1):
    """
    Return the nth Fibonacci number
    """
    if n < 0:
        raise ValueError("{} is a negative number.".format(n))
    for _ in range(n):
        a, b = b, a + b
    return a
{% endhighlight %}

#### More on scope

Functions can *access* global names and *alter* mutable objects that they
refer to. It is generally common to use global names for constants that
will not be modifed and to use ALL-CAPS for the name. Example:

{% highlight python %}
PI = 3.14

def circle_area(radius):
    return PI * r**2 
{% endhighlight %}

This valid function makes use of a global name `PI` inside the function
body.

However, if a function contains `PI` as a parameter or has `PI` as the
target of an assignment statement within the function body, then `PI` is
a local name inside the function call, and the global name `PI` is ignored
by the function. For example:

```
>>> PI = 3.14
>>> def circle_area(radius):
...     PI = 4
...     return PI * radius**2
... 
>>> circle_area(5)
100
>>> PI
3.14
```

Note that in this function, `PI` *only* refers to the local name everywhere
in the function body. If I try to reference `PI` inside this function before
the assignment I will raise an exception:

```
>>> PI = 3.14
>>> def circle_area(radius):
...     print("PI is {}".format(PI))
...     PI = 4
...     return PI * radius**2
... 
>>> circle_area(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in circle_area
UnboundLocalError: local variable 'PI' referenced before assignment
```

If I really want `PI` to refer to the global name while inside the function
body and I want to use an assignment statement to bind `PI` to a different
object, then I can use a `global` statement to designate that `PI` should
refer to the global name:

```
>>> PI = 3.14
>>> def circle_area(radius):
...     global PI
...     print("PI is {}".format(PI))
...     PI = 4
...     return PI * radius**2
... 
>>> circle_area(5)
PI is 3.14
100
>>> circle_area(5)
PI is 4
100
>>> PI
4
```

Use of the global statement is generally discouraged if it is avoidable, as
it makes the function harder to reason about.

Note that if a global name refers to a mutable object, a function can
mutate that object without needing to have a global statement:

```
>>> spam = []
>>> def add_spam():
...     spam.append('spam')
... 
>>> add_spam()
>>> add_spam()
>>> spam
['spam', 'spam']
```

* A global statement is only required when a function needs to assign a
  new object to a global name.



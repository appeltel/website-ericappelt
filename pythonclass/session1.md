---
layout: blogpost
title: Session 1
---

# Language Basics

### Suggested Readings

* Automate Stuff: Chapters 0\*, 1\*, and 2\*
* Learning Python: Chapters 4\*, 5\*, 6\*, 7\* (especially 6)

### Suggested Exercises

* Write a program to take an integer that the user inputs and print
  the corresponding
  [Fibonacci Number](https://en.wikipedia.org/wiki/Fibonacci_number).
  The Fibonacci sequence begins 1, 1, 2, 3, 5, 8, 13, so if the user
  inputs 7, the user should see the 7th Fibonacci number printed,
  which is 13. If the user inputs a negative number the program should
  print an error message.
* Write a program to convert temperatures from Fahrenheit to Celsius or
  vice versa. Have the user select which one from a menu
  (use a triple-quoted string to make the menu text) or quit from the
  program. Use a while loop to allow the user to convert multiple values.

---

### Session Notes

#### Motivation

* Started in 1989 - hobby scripting language (a year before linux)
  by Guido Van Rossum
* Irreverant attitude - named after [Monty Python](https://en.wikipedia.org/wiki/Monty_Python)
* In 2000, python 2.0 moved to community backed model, [Python Software Foundation](https://www.python.org/psf/)
* Guido is still the "Benevolent Dictator for Life" (BDFL)
* CPython is the reference implementation of python, on [github](https://github.com/python/cpython)
* Not a single paradigm language, has elements of OOP and functional programming
  but also its own style, try `import this`.
* Interactive language - built in REPL, tracebacks, fast feedback and development
* Great community - mention [PyTN](https://www.pytennessee.org/), [PyOhio](https://www.pyohio.org/2018/)
* "Batteries Included" - lots of great standard libraries - `import antigravity`
* Python2 vs 3 - 2 is basically deprecated, support ends in 2020, this is a python3 class
* Community style guide - [PEP8](https://www.python.org/dev/peps/pep-0008/)

#### Objects (start with arithmetic)

* *integers* - try out basic operations `+`, `-`, `*`, `**`
  * demonstrated that the size of integers is variable with large exponents
  * "integers are immutable"
    * an integer sits in memory as long as it is needed
    * arithmetic operations produce new integers in memeory
    * the same integer in memory might get reused, up to the interpreter
    * the _contents_ of an integer object in memory never change

* *floats* - [double precision](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) also immutable
  * division operations
    * `/` - real division
    * `//` - floor division
    * `%` - remainder

* Order of operations - talk about parenthesis

* *names* - names are references to objects
  * can't have whitespace or most punctuation
  * utf-8 allowed, but if programming in english try to stick with `A-Z,a-z,_,0-9`
  * can't begin with a number

* *assignment statements* - bind a name to an object

Do the following example, explain with diagrams:

{% highlight python %} 
a = 3
b = 1024
a = b
b = 2000
print(a)
{% endhighlight %}

Also explain what happens in memory in the following:

{% highlight python %}
a = 500
a = a + 300
print(a)
{% endhighlight %}

* *del statement* - unbind a name, rarely used

* *augmented assignment statement* do examples of `+=` and `*=`

#### Line structure and comments

* by default, one statement per line
* can use a semicolon to separate multiple statements on a line
* can use a backslash before a newline to "escape" the newline
  and extend a statement to the next line, (avoid this if possible)
* newlines within parenthesis (or later brackets, curly braces) don't
  count as a line ending

* *comments* - everything after a `#` character (not in quotes - see string later)

#### Strings

* Strings are also immutable objects
* Strings are arrays of Unicode codepoints.
* See [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
* Go over ascii vs utf-16 vs utf-8
* Do examples of single and double quotes
* Triple quoted strings
* string literals can be concatenated by juxtaposition
* strings can be added with `+`, repeated with `*`
* as with integers, operations produce new string objects in memory,
  a string object can never be modified
* Empty string - `''`
* Mention python 2 vs python 3 here - in python 2 strings were arrays of bytes

#### Calling Functions

* functions take expressions as parameters separated by commas.
* Parameters can be positional or named, positional parameters must come first
* Some examples:
  * `print('Hello World!')`
  * `print('Hello ' + "World!")`
  * `print('Hello World', end='?\n')`
* [Builtin functions](https://docs.python.org/3/library/functions.html) (good thing to bookmark)
* Functions *always* return an object
  * do examples of `hex(...)`, `id(...)`, and `type(...)` builtin functions.
* Functions can have a side effect, like `print()`.
  * but what is the object returned by print???

#### None

* There is only one `None` object in memory of type `NoneType`
* it is often used as a general purpose sentinel object
* default return value of a function
* _not_ printed on the REPL if the result of an expression statement
  * Mention here the idea of an *expression statement*
    an expression is evaluated, but nothing is done with the result

#### More builtin functions

* `help(...)`
* General "casting" functions:
  * `float(...)`
  * `int(...)`
  * `str(...)`
* `repr(...)` - gives you either the code to make an object or a basic description `<...>`

#### Booleans

* `True` and `False`
* `bool(...)` builtin - all objects can be evaluated as a boolean!!!
* *TRUTHINESS*
  * experiment with some types
  * default truthiness of an object is `True`
  * falsiness generally denotes numberical "zeroness" or for a container "emptyness"
* Value comparisons - experiment with `<, >, <=, >=, !=, ==`
  * discuss identity and equality
    * `id(...)` operation and `is` comparison.
  * comparisons can be chained
    * evaluated left to right `a < b < c`
    * "short circuit" example `1 > 2 > "foo"` versus `1 < 2 > "foo"`
* discuss `and`, `or`, `not`

#### Conditionals

Basic form

{% highlight python %} 
if expression:
    ...
    ...
elif expression:
    ...
    ...
else:
    ...
    ...
{% endhighlight %}

Note: `expression` can be any valid python expression - will be converted to boolean!

* INDENTATION!!! - suite of expressions in each clause is defined by indentation
  * tabs or spaces can be used as long as they are used consistently
  * 4 spaces is preferred!

* Do a few examples here with correct and incorrect indentation, also
  ones that rely on the truthiness of various expressions.

#### While statements

Basic form

{% highlight python %} 
while expression:
    ...
    ...
    ...
{% endhighlight %}

* Executes suite of indented statements as long as expression evaluates to
  true

* Do examples with nested indentation, if statements
* Discuss *continue* and *break* statements with examples.
  * continue - stop current execution os suite and go back to top
  * break - stop current execution and exit the loop

* Discuss scope (or lack thereof so far) - in python compound statements
  like while and if do not create scope. A name bound within a while or if
  clause stays bound outside clause.
  * Mention `locals()` and `globals()` builtin to get a dictionary (explained
    later) of bound names and their objects

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


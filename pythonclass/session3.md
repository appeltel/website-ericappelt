---
layout: blogpost
title: Session 3
---

# Strings, Bytes, and Files

### Suggested Readings

* Automate Stuff: Chapters 5, 6\*, 7
* Learning Python: Chapters 10, 11, 12

### Suggested Exercises

* Save the csv content below into a file. This information is the
  last name, first name, and age of employees of an imaginary company,
  animals.com. Write a script to read in the csv file and then write a
  new file with all the information as well as a fourth column with the
  email address of each employee. The email address of an employee is
  comprised of their last name (up to the first seven letters, all
  lowercase) followed by the first letter of their first name (lowercase)
  at animals.com. For example, I am Eric Appelt and my email would
  be `appelte@animals.com`. Ada Lovelace would be `lovelaca@animals.com`.

{% highlight text %}
Aardvark,Alice,27
Badger,Bob,44
Catfish,Cynthia,32
Dingo,Drew,61
Elephant,Emily,24
Frog,Ferdinand,41
Gerbil,Greta,33
Heron,Harold,19
Iguana,Isabella,29
Jaguar,John,61
Kangaroo,Kate,63
Lemur,Leonard,54
Millipede,Marsha,47
Newt,Norman,21
Octopus,Olivia,42
Pelican,Peter,29
Quail,Quinlan,30
Raccoon,Rocky,50
Salamander,Stacy,36
Termite,Terrence,20
Uakari,Ursula,27
Vulture,Vincent,61
Warthog,Wanda,50
Xenops,Xavier,21
Yak,Yolanda,44
Zebra,Zackery,49
{% endhighlight %}

* Do the table printer project in chapter 6 of automate the boring stuff
  (it doesn't need to be a function, just a script to process the example
  list).

---

### Session Notes

#### Object attributes

As seen a little bit before, python objects can have *attributes*. These are
accessed with a dot notation as `<object>.<attribute>`. An attribute of
an object can be thought of like a name in that it itself refers to another
object, but it is "attached to" or "in the namespace" of the object it is
an attribute of.

Some attributes can be functions and these are called *methods*. Methods
are like other python functions in most ways, only they "know about" the
specific object they are attached to. The output of a method will depend on
the properties of the particular object it is called from, and may even
modify that object if it is mutable.

* the `dir()` builtin function will tell you the attributes of an object.
  * As an example, make a list and call `dir(mylist)` to return a list of
    the attribute names for the list.
  * Many of these begin and end with double-underscores. These are special
    attributes called "dunders". They are reserved for special significance
    by the python interpreter. You can ignore them for now, we will revisit
    them later
  * Try a list comprehension to filter out the dunders
    * `[a for a in dir(mylist) if not a.startswith('__')]`

Try out some of these list attributes. For example the `count` method:

{% highlight pycon %}
>>> mylist = [1, 1, 3, 4, 5, 5, 5]
>>> mylist.count(5)
3
>>> mylist.count(1)
2
{% endhighlight %}

* To see what a method is supposed to do, use the `help(...)` builtin
  function.
  * Example, try `help(mylist.reverse)`. Then use this to reverse a list.

#### More on Strings  

Strings have a lot of useful methods that one can discover with
`dir()` and `help()`. Try some out:

{% highlight pycon %}
>>> s = '   Hello world!!!  '
>>> [m for m in dir(s) if not m.startswith('__')]
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s.startswith('   H')
True
>>> s.endswith('!')
False
>>> s.lower()
'   hello world!!!  '
>>> s.upper()
'   HELLO WORLD!!!  '
>>> s.strip()
'Hello world!!!'
>>> s.strip().endswith('!')
True
>>> s.rjust(25)
'         Hello world!!!  '
>>> s.rjust(35)
'                   Hello world!!!  '
{% endhighlight %}

Two very useful string methods are `split()` and `splitlines`

* Do some examples

{% highlight pycon %}
>>> s = """
... foo,  bar,
... baz, 
... spam   , eggs
... 
... """
>>> [w.strip() for w in s.split(',')]
['foo', 'bar', 'baz', 'spam', 'eggs']
{% endhighlight %}

Another key string method is `join()`:

Join takes an iterable as an argument (assumed to contain strings) and
joins them together into one string with the string object it is called
from as a separator

* Start by taking the result of the example above and feeding it to
  `','.join(mylist)`
* Try using the empty string `''.join(...)` to join a list of strings
  without a separator

PROTIP: To build up a big string, it is tempting to repeatedly use
`mystring += more_text`. However, this can be sometimes hard to work with
down the road, and has very poor performance (`O(n^2)`). The reason for the
poor performance is that a new string is being created with each addition
and the old string thrown away.

A better way is to start a list of your string components and add more
using `mylist.append(more_text)`. Then at the end use `''.join(mylist)` to
create the final string. This also has the advantage that it's easy to insert
or remove things while building the list compared to a partially built string.

#### Format method

Arguably the most important and useful string method is `format()`. Some
examples of "format strings":

{% highlight pycon %}
>>> 'I had {} and {} for dinner'.format('spam', 'eggs')
'I had spam and eggs for dinner'
>>> 'I had {0} and {1} for dinner'.format('spam', 'eggs')
'I had spam and eggs for dinner'
>>> 'I had {1} and {0} for dinner'.format('spam', 'eggs')
'I had eggs and spam for dinner'
>>> 'I had {0} and {0}, and {0} for dinner'.format('spam', 'eggs')
'I had spam and spam, and spam for dinner'
{% endhighlight %}

Now is a good time to mention *keyword parameters*. These allow you
to specify function parameters by name rather than by position. This
is very useful for functions with lots of parameters as you don't need
to memorize the order of parameters:

{% highlight pycon %}
>>> 'I had {main} and {side} for dinner'.format(side='eggs', main='spam')
'I had spam and eggs for dinner'
{% endhighlight %}

Numeric formatting is available for floats:

{% highlight pycon %}
>>> 'The total is ${0:.2f}'.format(31.74348)
'The total is $31.74'
>>> 'The temperature is {0:.2e}K '.format(1400.3729)
'The temperature is 1.40e+03K '
{% endhighlight %}

A full description of the format "mini-language" is in the python
[library reference](https://docs.python.org/3/library/string.html#formatstrings)

#### Strings, Bytes, and ASCII - Some History

* *ASCII* encodes only 127 "characters" in 7-bits. Typically encoded into
  bytes with the first bit 0
  * Example `A` is 65, of `0x41` in hexidecimal, or `0100 0001` in binary
  * An ASCII text file would often be called a "plain text" file by
    English speakers, and sometimes still is.

* *Unicode* Encodes thousands of "characters" from various languages and
  symbol sets as integers or "codepoints". However, for simplicity the
  first 127 codepoints correspond exactly to ASCII characters.
  * Example: Greek lowercase `φ` is codepoint `0x03C6`
  * Example: Latin capital `A` is codepoint `0x0041`
  * Unicode has to be encoded into bytes to be represented in memory,
    and two old common encodings were `UTF-16` and `UTF-32` which would
    use two or four bytes to encode codepoints. `UTF-32` is the simplest
    as any existing codepoint can be encoded within four bytes.
  * The `utf-8` encoding is newer and space saving but has become
    ubiqutious on the web. For codepoints under 128 (ASCII), each
    character is encoded in a single byte. The leading 0 on the byte
    tells the computer that this is a single-character codepoint. Higher
    codepoints are designated with a 1 in the leading bit, indicating that
    multiple bytes are used for the current character.
  * One nice thing about `utf-8` is that ASCII files are effectively valid
    `utf-8` files as the valid ASCII bytes are all valid `utf-8` encodings
    for the same character.
  * Python3 uses `utf-8` as its default encoding

Python strings are arrays of unicode codepoints. To be written to the
screen, saved to a file, or transmitted over the network, they must be
encoded as an array of *bytes*. Similarly, to be understood in python as
a string, an array of *bytes* must be decoded into unicode codepoints.

Note: Python3 source files are by default `utf-8` encoded. So you can
use higher codepoints in the source and in the interpreter. The following
is valid python:

{% highlight python %}
the_snake = 'το φίδι'
{% endhighlight %}

You can even use non-whitespace, non-punctuation `utf-8` characters as
variable names in python, although if your code is written in English
you should stick to ASCII:

{% highlight python $}
το_φίδι = 'the snake'
{% endhighlight %}


#### The bytes type

A *byte* type is an immutable type, with many similarities to the
*str* type and many of the same methods. Instead of being an array of
codepoints, it is an array of bytes.

You can make a bytes object by calling the encode method on a string, and
supplying it with a "codec" to use to encode the codepoints:

{% highlight pycon %}
>>> s = 'το φίδι is Greek for "the snake"'
>>> s
'το φίδι is Greek for "the snake"'
>>> s.encode('utf-8')
b'\xcf\x84\xce\xbf \xcf\x86\xce\xaf\xce\xb4\xce\xb9 is Greek for "the snake"'
>>> s.encode('utf-16')
b'\xff\xfe\xc4\x03\xbf\x03 \x00\xc6\x03\xaf\x03\xb4\x03\xb9\x03 \x00i\x00s\x00 \x00G\x00r\x00e\x00e\x00k\x00 \x00f\x00o\x00r\x00 \x00"\x00t\x00h\x00e\x00 \x00s\x00n\x00a\x00k\x00e\x00"\x00'
>>> s.encode('utf-32')
b'\xff\xfe\x00\x00\xc4\x03\x00\x00\xbf\x03\x00\x00 \x00\x00\x00\xc6\x03\x00\x00\xaf\x03\x00\x00\xb4\x03\x00\x00\xb9\x03\x00\x00 \x00\x00\x00i\x00\x00\x00s\x00\x00\x00 \x00\x00\x00G\x00\x00\x00r\x00\x00\x00e\x00\x00\x00e\x00\x00\x00k\x00\x00\x00 \x00\x00\x00f\x00\x00\x00o\x00\x00\x00r\x00\x00\x00 \x00\x00\x00"\x00\x00\x00t\x00\x00\x00h\x00\x00\x00e\x00\x00\x00 \x00\x00\x00s\x00\x00\x00n\x00\x00\x00a\x00\x00\x00k\x00\x00\x00e\x00\x00\x00"\x00\x00\x00'
>>> s.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
{% endhighlight %}

Notice that a bytes object displays the character if it is a printable ascii
character but if not it uses the notation `\xcf` to state the byte in
hexidecimal. Also notice that you can't encode to ASCII if the characters
are not ASCII characters.

You can make a byte object literal by preceding your text with a b. You can
only put ASCII characters in a bytes literal, for values above 127 you must
use the `\x00` notation:

{% highlight pycon %}
>>> mybytes = b'\xcf\x84\xce\xbf \xcf\x86\xce\xaf\xce\xb4\xce\xb9 means snake'
>>> mybytes
b'\xcf\x84\xce\xbf \xcf\x86\xce\xaf\xce\xb4\xce\xb9 means snake'
>>> mybytes.decode('utf-8')
'το φίδι means snake'
{% endhighlight %}

The `decode()` method on a bytes object will decode your bytes into
unicode codepoints and return a string object.

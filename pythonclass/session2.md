---
layout: blogpost
title: Session 2
---

# Iterators and Sequences

### Suggested Readings

* Automate Stuff: Chapters 3, 4\*
* Learning Python: Chapters 8\*, 9\*

### Suggested Exercises

* Do the "Character Picture Grid" project in Automate Stuff Chapter 4.
  Note that `print("Hello World!", end="")` will print the string `Hello World!`
  without a newline.
* Do the "Comma Code" project in Automate Stuff Chapter 4, but don't worry about
  writing a function as we haven't gone over it yet.
  Just write code to handle the example string.

---

### Session Notes

*Iteration Protocol* is a central concept in python. Many object types
implement iteration protocol.

Later we will go over how to use iteration protocol, for now a simple
example is instructive:

{% highlight pycon %}
>>> s = 'hello'
>>> itr = iter(s)
>>> type(itr)
<class 'str_iterator'>
>>> next(itr)
'h'
>>> next(itr)
'e'
>>> next(itr)
'l'
>>> next(itr)
'l'
>>> next(itr)
'o'
>>> next(itr)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
{% endhighlight %}

Once a `StopIteration` exception is raised, we say that the iterator is
"exhausted".

*for loops* allow you to iterate over "containers" and perform a suite of
statements accessing each object in the "container". Here a "container" is
anything that implements iterator protocol.

For loop syntax:

{% highlight python %}
for name in expression:
    ...
    ...
    ...
{% endhighlight %}

Do a few examples iterating over the characters in a string, start with:

{% highlight python %}
for character in "Hello":
    print(character)
{% endhighlight %}

Note: for loops accept *continue* and *break* statements. Do examples.

#### Range Objects

Some examples:

* `range(4)` is an iterable that produces 0, 1, 2, 3 when iterated over
* `range(1, 4)` produces 1, 2, 3
* `range(1, 8, 2)` produces 1, 3, 5, 7

general form `range(<start>, <stop>, <step>)`  - note: step can be negative! Try an example.

Example in a for loop:

{% highlight python %}
for x in range(10):
    print(x**2)
{% endhighlight %}

#### The underscore name

The underscore by itself (`_`) is typically used as a throwaway placeholder when
we don't care for a resulting object. For example, if I just want to print "spam"
ten times:

{% highlight python %}
for _ in range(10):
    print("spam")
{% endhighlight%}

Underscore has a special meaning as well in the interactive REPL. If the previous
statement was an expression statement, the resulting object will be bound to `_`, for
example:

{% highlight pycon %}
>>> a = 13
>>> 2 + a**2
171
>>> _
171
>>> _ + 12
183
{% endhighlight %}

#### Lists

Lists are ordered, indexed containers of objects that can be iterated over. A list can contain
objects of different types. One way to make a list is to specify its contents as expressions
separated by commas within brackets:

{% highlight python %}
mylist = [1, 2, "foo", 3.4 + 5.5, True]
{% endhighlight %}

Lists can be empty, for example `mylist = []`.

Lists are a *mutable* type. Lists have methods that allow you to change the contents of a list.
For example, the `append` method can be called to add an object to the end of a list:

{% highlight pycon %}
>>> mylist = [1, 2, 6, 8]
>>> mylist.append(7)
>>> mylist.append(10)
>>> mylist
[1, 2, 6, 8, 7, 10]
{% endhighlight %}

Try using the `pop()` method which will return the last item from the list and remove it from the
list. With `append()` and `pop()` you can use a list as a stack.

Another way to make a list is with the `list` builtin-function. It takes an iterable as an argument
and returns a list containing all the elements in that iterable. For example, to
make a list with the numbers 0, ..., 9, try `mylist = list(range(10))`.

Note that when you bind another name to a list they both refer to the same object, so modifying
the object will be apparent with either name:

{% highlight pycon %}

>>> a = [1, 2, 3]
>>> b = a
>>> a.append(4)
>>> b
[1, 2, 3, 4]
>>> a == b
True
>>> a is b
True
>>> id(a)
4409730504
>>> id(b)
4409730504
{% endhighlight %}

Notice the new `is` comparison operator. The `==` operator will return `True` if two lists contain
equal objects, but `is` will only return `True` if it is the same object (in memory) on either
side.

If I want to make a copy of a list, the simplest way is to feed a list into the `list` builtin
function which will iterate over the list and make a new one with the contents of the first:

{% highlight python %}
>>> a = [1, 2, 3]
>>> b = list(a)
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> b
[1, 2, 3]
>>> a is b
False
{% endhighlight %}

#### Tuples

Tuples are similar to lists, but they are *immutable*. Once you make a tuple, you can
never change what objects are contained in it. The beauty of this is that as a developer, you never
need to really care if you are working with the same tuple or a copy of a tuple - the results
would never be different!

A tuple is constructed like a list but using parenthesis instead of brackets:

{% highlight python %}
mytuple = (1, 2, 3, 'foo')
{% endhighlight %}

Notice that parenthesis are also used to enclose expressions. So how does the intepreter
distinguish between parenthesis around an expression and a tuple definition? It's the presence of
a comma that determines a tuple. So to make a tuple of one object, you need a trailing comma:

{% highlight pycon %}
>>> (1, )  # a tuple containing a single object 1
(1,)
>>> (1)  # this is just the integer 1
1
>>> ()  # this special case is an empty tuple
()
{% endhighlight %}

Note the special case of `()`. If you enclose nothing inside parenthesis, you have made an
empty tuple.

For both lists and tuples, you can use the `+` operator to add together multiple lists (or tuples).
Try it! Also try adding a list to a tuple and see what happens. Note that it is ok to add tuples
even though they are immutable since the result is a new tuple.

The `*` operator is also defined for multiplying a list or tuple by an integer, much like a string,
try it!

#### Sequences

Ranges, lists, and tuples are all examples of *sequence types*, see [sequences](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range).

Looking up items by position (or index)  in a sequence type is done with *subscript* notation, as follows:

{% highlight pycon %}
>>> mylist = ['foo', 'bar', 'baz', 'spam']
>>> mylist[0]
'foo'
>>> mylist[3]
'spam'
>>> mylist[-1]
'spam'
{% endhighlight %}

Notice you can use a negative number to count backwards from the end. If the index is out of
range you will raise an `IndexError`.



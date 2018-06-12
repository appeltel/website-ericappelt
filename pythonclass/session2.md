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

The `len()` builtin-function will return the length of a sequence.

#### Mutable sequences

A `list` is a mutable sequence, while strings and tuples are immutable
sequences. Mutable sequences allow additional operations.

* You can assign an object to a sequence position with an assignment
  statement with a subscript: `mylist[3] = 4`
* You can delete a position with a delete statement including a subscript:
  `del mylist[3]`. Try this and notice how the other elements shift position.
* You can insert a new element at a given position with the `insert` method,
  for example `mylist.insert(2, 15)`. Notice how this shifts element
  positions.
* The `pop` and `append` methods for list also apply to all mutable sequences.
* You can use the `extend` method to append another list (or the elements
  of any iterable) to the end of a sequence. Try extending a list with another
  list, a tuple, and then a string.

#### List Comprehensions

List comprehensions are a powerful, "pythonic" way to create a list
based on an existing iterable.

General syntax:

{% highlight python %}
mylist = ["expression" for "name" in "iterable" if "expression"]
{% endhighlight %}

One example, making a list of all the squares of odd numbers from 1 to 100.
You can do this with the `append` method and a for loop:

{% highlight python %}
mylist = []
for num in range(1, 101):
    if num % 2 == 1:
        mylist.append(num)
{% endhighlight %}

Or with a list comprehension as a single statement:

{% highlight python %}
mylist = [num**2 for num in range(1, 101) if num % 2 == 1]
{% endhighlight %}

Note that the if clause, or "filter" is optional, and you can have multiple
if clauses if desired.

* *STYLE NOTE*: List comprehensions are for _making lists_, not for general
  use as an "inline for statement". An example of generally improper use is
  `[print(line) for line in some_log_file]`
  * This will make a list in memory of repeated references to `None` while
    also printing to the screen, and then throw that list away. Just use a
    for loop!

* *STYLE NOTE*: Everything inside brackets `[]` can span multiple lines and
  still be a single statement, so it is ok to allow a list comprehension to
  use a few lines if needed. If things are really complicated, you might
  find it more readable to make a for loop.
  * The term "list incomprehension" is sometimes given to very long list
    comprehensions that are very difficult to understand.

#### Slices

Slicing can be though of as a variation on subscript notation.
One takes a _slice_ of an existing sequence and creates a new sequence
with just that slice of the contents.

* Note: slicing never results in an `IndexError`. If the slice is
  in some manner "out of range" it just results in an empty sequence.

Basic Syntax:

* `mysequence["start":"stop"]` *or* `mysequence["start":"stop":"step"]` where
  start, stop, and step are integers.

Examples:

{% highlight pycon %}
>>> seq = [0, 1, 2, 3, 4, 5, 6, 7]
>>> seq[1:5]
[1, 2, 3, 4]
>>> seq[0:6]
[0, 1, 2, 3, 4, 5]
>>> seq[:6]
[0, 1, 2, 3, 4, 5]
>>> seq[4:]
[4, 5, 6, 7]
>>> seq[:-1]
[0, 1, 2, 3, 4, 5, 6]
>>> seq[:-3]
[0, 1, 2, 3, 4]
>>> seq[1:6:2]
[1, 3, 5]
>>> seq[6:1:-2]
[6, 4, 2]
>>> seq[::-1]
[7, 6, 5, 4, 3, 2, 1, 0]
>>> seq[:]
[0, 1, 2, 3, 4, 5, 6, 7]
{% endhighlight %}

Note how you can leave out numbers to default to the first or last element.

* `seq[:]` is sometimes used to produce a copy of a sequence
* `seq[::-1]` is a handy way to produce a reversed sequence

Try more examples and see if everyone can guess what will happen. Also watch
what happens if you slice a string or a range object.

#### Sorting

Sequences can be sorted in several ways. In order to (easily) sort a
sequence, the `<` operator must be defined for comparisons between any
two elements of the sequence. There is a way to override that, but is a
more advanced topic.

For a *mutable* sequence, you can use the `sort()` method to sort the
sequence in place, meaning that you alter the sequence.

For any sequence, you can use the `sorted(...)` builtin function to create
a new sequence that is a sorted copy of the input. Try both of these
on lists and strings.

Note that the default sorting implementation in python uses an algorithm
called [Timsort](https://en.wikipedia.org/wiki/Timsort) which is a
hybrid algorithm derived from merge sort and insertion sort.

#### Swapping and target list assignments

Python has a variation on the assignment statement where you can assign
to a "target list" of several names in one statement, the general form
is:

{% highlight python %}
name, name, name = iterable_expression
{% endlighlight %}

The way it works is that the expression on the right hand side must
result in an iterable with as many items as there are names on the
left hand side of the `=`. The interpreter will iterate over the iterable
and assign each object to a name in order.

One neat trick that you can do using this is to swap the values of two
names without using an additional temporary name:

{% highlight python %}
a, b = b, a
{% endhighlight %}

The way this works is by creating a tuple on the right hand side first,
then assigning to the target list. The tuple is then discarded.

* Go over how this operation appears in memory with diagrams

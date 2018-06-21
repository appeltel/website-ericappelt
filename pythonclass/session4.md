---
layout: blogpost
title: Session 4
---

# Sets and Dictionaries

### Suggested Readings

* Automate Stuff: Chapters 8, 9
* Learning Python: Chapters 13, 14, 15

### Suggested Exercises

* Download the [Complete Works of Shakespeare](http://www.gutenberg.org/ebooks/100)
   as a single text file.
  Open the file in python, `read()` the text, and use `split()` to split it
  into words. You can then use `lower()` and `strip("'.,;:!?_-")` to get
  rid of most punctuation and case. Use this list of words for the other exercises.
* Make a set of all words that start with `z`. Determine the length of the set.
  Make a set of all words that end in z. Make a union of the two sets,
  and determine its length.
* Make a dictionary where each word is a key and the value is the number of
  times that the given word appears in the text. How often do some common
  words like "and" and "the" appear?
* Using a dictionary comprehension, make a dictionary of only those words and
  their frequency where the frequency is over 1000. How many such words are there?

---

### Session Notes

#### A litte bit of CS on lists

In the reference implementation of python, lists are *dynamic arrays*. This
means that in memory they are a contiguous array of references to python
objects. They typically have a few "extra" slots on the end for appended
objects and are resized when they run out and need more.

* Make a diagram on the board or keynote here showing the structure

This has some key performance consequences:

* Accessing list elements by index is *fast* no matter how big the list is,
  i.e. `O(1)`
* Adding/removing elements from the end is *usually fast* unless the list
  needs to be resized. When the list does need resizing, it might still be
  fast depending if the interpreter needs to move the whole list to another
  place in memory
* Adding/removing things in the middle is *slow-ish* for large lists, `O(n)`,
  as you have to shuffle all the higher-indexed elements
* Finding specific elements by value is *slow-ish* for large lists, `O(n)`
  as you have to traverse the whole array looking for it.

#### Hashing Python Objects

Most immutable objects in python can be *hashed*, that is assigned a special,
bounded integer depending on its value subject to certain rules:

* Equal objects always have equal hashes
* Unequal objects *usually* have different hashes

Try a few examples, note how lists cannot be hashed:

```
>>> hash('foo')
-5922314827231547410
>>> hash((3, 4, 'spam'))
5269746718638076334
>>> hash(39.17)
391993311566331943
>>> hash(14)
14
>>> hash(1)
1
>>> hash(2**61)
1
>>> hash([1, 2, 3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

WARNING: Python hashes are not cryptographic hashes. It is possible to
determine the likely value of an object from its hash in many cases. These
should never be used for security. Note that small integers have particularly
obvious hashes!

What are hashes good for then?

Hashes are good for assigning objects to buckets in order to quickly
find values in a collection.

#### Sets

A python *set* is a collection of objects but with many differences from
a python list:

* Sets can *only* contain hashable objects
* Sets have no inherent ordering, they are not *sequences*
* However, a set is *iterable*
* A set will only hold one object of a given value, determined by
  equality
* Sets are mutable
* It is *fast*, `O(1)ish` to find if a given value is in a set, compare to
  lists where this is slower for large lists
* They are much like mathematical sets

How to make a set:

* From a literal (using curly braces): `myset = {1, 2, 'spam'}`
* From the built in set function: `myset = set(<iterable>)`  
  * Example `myset = set([1, 1, 2, 3, 3, 4])` - this is good for filtering duplicates
* Using a set comprehension: `myset = {x**2 % 100 for x in range(50)}`
  * try doing a `len(myset)` on this.

Warning: `{}` does not create an empty set. This creates an empty dictionary (explained later).
To make an empty set use `set()`.

Membership testing:

* `<value> in <set>` --> `True/False`
* `<value> not in <set>` --> `True/False`

Do examples.

This is fast for big sets as sets are implemented as hash tables, slower for big lists

Some set methods (do examples):

* `add(...)`
* `remove(...)`
* `discard(...)`
* `update(...)`

Set operations (mathematical - do examples):

* Subset comparison `<, >, <=, >=`
* Union `myset | otherset` or `myset.union(otherset)`
* Intersection `myset & otherset` or `myset.intersection(otherset)`
* Difference `myset - otherset` or `myset.difference(otherset)`
* symmetric difference `myset ^ otherset` or `myset.symmetric_difference(otherset)`

#### Frozensets

A *frozenset* is like a set but immutable (and therefore hashable!).

Make one with the `frozenset(<iterable>)` buitin function.

#### Mapping types (dicts)

The python *dict* type is a built-in example of a mapping type. Internally, a dict works much
like an extension of a set, only each element of a dict is called a *key* and has a corresponding
*value*. The keys of a dict must be hashable, but values can be any object.

Making a dict (literal):

{% highlight python %}
mydict = {"spam": True, "eggs": False, 12: ['a', 'b', 'c']}
{% endhighlight %}

Items in a mapping type are accessed by subscript, like a sequence, but the
subscript is a key rather than strictly an integer:

```
>>> mydict = {"spam": True, "eggs": False, 12: ['a', 'b', 'c']}
>>> mydict['spam']
True
```

Membership tests check for the existence of a key in a dict. Since dicts
are hash tables, this check is *fast*:

```
>>> mydict = {"spam": True, "eggs": False, 12: ['a', 'b', 'c']}
>>> 'spam' in mydict
True
>>> 'foo' in mydict
False
```

Dicts are *mutable* so you can assign to a key (new or existing) by
subscript and use the `del` statement:

```
>>> mydict = {"spam": True, "eggs": False, 12: ['a', 'b', 'c']}
>>> mydict['spam'] = 2.5
>>> mydict['spam']
2.5
>>> 'foo' in mydict
False
>>> mydict['foo'] = 1
>>> 'foo' in mydict
True
>>> del mydict['foo']
>>> 'foo' in mydict
False
```

Trying to access a non-existent key in a dict will raise a `KeyError`. You
can use the `get` method to try to get a value from a key that may not exist
which will return `None` if the specified key does not exist, or you can
provide a default value to be returned:

```
>>> mydict = {"spam": True, "eggs": False, 12: ['a', 'b', 'c']}
>>> mydict['foo']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'foo'
>>> mydict.get('foo')
>>> mydict.get('foo', False)
False
```

#### Iterating over a dict, view objects

Mapping types are generally iterable, and will iterate over their keys

```
>>> mydict = {"spam": True, "eggs": False, 12: ['a', 'b', 'c']}
>>> for key in mydict:
...     print(key)
... 
spam
eggs
12
```

Note that there is no general guarantee to order to a dict, although in
CPython 3.6 and later dicts will maintain an order of keys.

Dict "view" objects provide iterables to *dynamically* return keys or
values or both. If a dict is updated in the process of iteration they
will be updated as well.

```
>>> mydict = {'foo': 1, 'bar': 2, 'baz': 3}
>>> for key in mydict.keys():
...     print(key)
... 
foo
bar
baz
>>> for val in mydict.values():
...     print(val)
... 
1
2
3
>>> for pair in mydict.items():
...     print(pair)
... 
('foo', 1)
('bar', 2)
('baz', 3)
```

Here's an example of the dynamic updating at work:

```
>>> mydict = {'foo': 1, 'bar': 2, 'baz': 3}
>>> for val in mydict.values():
...     mydict['baz'] += 1
...     print(val)
... 
1
2
5
```

*WARNING*: You should not add or remove keys from a dictionary during
iteration. This can cause unexpected errors:

```
>>> mydict = {'foo': 1, 'bar': 2, 'baz': 3}
>>> for key, val in mydict.items():
...     if key == 'foo':
...         mydict['a'] = 0
...     print((key, val))
... 
('foo', 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration
```

If you need to modify a dict during iteration, you should iterate over
a copy

*WARNING*: You should not add or remove keys from a dictionary during
iteration. This can cause unexpected errors:

```
>>> mydict = {'foo': 1, 'bar': 2, 'baz': 3}
>>> for key, val in mydict.items():
...     if key == 'foo':
...         mydict['a'] = 0
...     print((key, val))
... 
('foo', 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration
```

If you need to modify a dict during iteration, you should iterate over
a copy

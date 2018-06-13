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


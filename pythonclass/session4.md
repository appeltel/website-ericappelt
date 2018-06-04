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

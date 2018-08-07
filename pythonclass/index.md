---
layout: blogpost
title: ACCRE Python Course
---

# A Foundation in Python for Researchers and Scientists 

This course is a foundation in python programming geared primarily
towards scientific researchers, data scientists, and more generally
anyone seeking a more solid foundation in the core python language
and some of the avaialable tools. The course is primarily designed
for people who have some programming experience, although experience
with python is not required.

The content and focus of the course is based on my experience as
a scientist who for many years used python clumsily without a deeper
understanding of the language. It is intended to be the course that
I wish I had taken earlier on while first trying to use the language
productively.

My hope is that by completing this course one will have developed
sufficient proficiency with the language to write maintainable,
reusable, and testable code that is suitable for sharing with
colleagues. While the later part of the course will introduce some of
the basic scientific libaries and tools such as
[numpy](http://www.numpy.org/), [pandas](https://pandas.pydata.org/),
and [jupyter notebooks](http://jupyter.org/),
the main focus of the course is building a solid foundation in the
core language itself. I believe that once one has such a foundation,
an enterprising researcher will be well positioned to further
learn libraries and tools on their own.

## Course Format

The course will consist of 75 minute interactive sessions. In these,
I will present concepts and interactively explore them on the python
interpreter while course attendees follow along on their own laptops,
allowing each student to try variations on their own. It is my hope
and expectation that this exploration is frequently interrupted by
questions about the examples which we will further investigate. I will
leave ample room in the material to accommodate such investigation.

I will assign exercises to be worked on between course sessions, and
optional readings from two selected textbooks. There will be no formal
evaluations, but I hope that students will find the exercises useful and
I will make myself available to help with the exercises.

## Time and Location

The course will take place during the Vanderbilt Summer Semester from
June 5th to August 10th (2018) every Tuesday and Thursday from
9:00 to 10:15 AM.

The physical location is the main conference room in the
[ACCRE Suite](https://www.vanderbilt.edu/accre/location/) in the
Hill Center.

## Accompanying Texts

I have selected two suggested textbooks to accompany the course for students
who wish to dive further into python. One book, "Automate The Boring Stuff",
takes a lighthearted and very practical approach, and will introduce the reader
to some very useful libraries not covered in the sessions. The other,
"Learning Python", is a more traditional and thorough treatment of the language.

Although neither text follows the exact presentation of the language in the order
the course sessions introduce concepts, they are close enough that
I was able to choose selected readings that often correspond to the
material in the most recent session.

These textbooks are avaialable online for free or through Vanderbilt's Safari
subscription. If you find "Automate The Boring Stuff" particularly useful, I
encourage you to support the author by purchasing a copy if you have the means.

* [Automate the Boring Stuff](https://automatetheboringstuff.com/)
* [Learning Python](https://www.safaribooksonline.com/library/view/learning-python-5th/9781449355722/)

## Prerequisites and Getting Started

The only prerequisite to starting this course is to obtain a laptop or
other device with python 3.4 or later installed. You should be able to
(using the text editor of your choice) make a file containing the single
python statement `print("Hello World!")` and run it, for example:

{% highlight console %}
$ echo 'print("Hello World!")' > hello.py
$ python hello.py
Hello World!
{% endhighlight %}

You should also be able to run this statement from the python interpreter's
interactive REPL feature, for example:

{% highlight console %}
$ python
Python 3.6.4 (default, Mar 23 2018, 08:00:10) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print('Hello World!')
Hello World!
{% endhighlight %}

You can find download instructions for python at the
[python web site](https://www.python.org/), or you may also wish to use
the [Anaconda python distribution](https://www.anaconda.com/download/) which
includes many useful scientific libraries already.

## Course Material

Descriptions, suggested exercises, and suggested readings are given
in each session page . Where the readings correspond well to the session
content, they are marked with an asterisk. Session notes
may be posted before or after the
session. While my notes may be helpful, they are not intended as a stand-alone
replacement for attending each session.

1. [Language Basics](session1.html)
1. [Iterators and Sequences](session2.html)
1. [Strings, Bytes, and Files](session3.html)
1. [Sets and Dictionaries](session4.html)
1. [Functions](session5.html)
1. [Exceptions, Logging, and Context Managers](session6.html)
1. [Modules, Dates, OS Functions, Virtual Environments](session7.html)
1. [Packages and Unit Testing](session8.html)
1. [Classes Part I](session9.html)
1. [Classes Part II](session10.html)
1. [Iteration Protocol, Generators, Sequences](session11.html)
1. [Functional Programming, Lambdas, and Decorators](session12.html)
1. [Writing a Distributable Package](session13.html)
1. [Python Performance, Multithreading, Multiprocessing](session14.html)
1. Intro to Numpy and Pandas

# License

![CC BY-SA](license.png) This course content is licensed under a 
[Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
You may republish or adapt this material for educational purposes, as
long as proper credit is given. Our recommended credit includes the statement:
Written by, or adapted from, Eric Appelt and the Vanderbilt University
Advanced Computing Center for Research and Education (current as of .....).
If you remix, transform, or build upon the material, you must
distribute your contributions under the same license as the original.

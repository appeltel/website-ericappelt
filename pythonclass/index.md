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
for each session. Where the readings correspond well to the session content,
they are marked with an asterisk. Session notes may be posted before or after the
session. While my notes may be helpful, they are not intended as a stand-alone
replacement for attending each session.

#### Session 1: Language Basics

Suggested Readings:

* Automate Stuff: Chapters 0\*, 1\*, and 2\*
* Learning Python: Chapters 4\*, 5\*, 6\*, 7\* (especially 6)

Suggested Exercises:

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

#### Session 2: Iterators and Sequences

Suggested Readings:

* Automate Stuff: Chapters 3, 4\*
* Learning Python: Chapters 8\*, 9\*

Suggested Exercises:

* Do the "Character Picture Grid" project in Automate Stuff Chapter 4.
  Note that `print("Hello World!", end="")` will print the string `Hello World!`
  without a newline.
* Do the "Comma Code" project in Automate Stuff Chapter 4, but don't worry about
  writing a function as we haven't gone over it yet.
  Just write code to handle the example string.

#### Session 3: Strings, Bytes, and Files

Suggested Readings:

* Automate Stuff: Chapters 5, 6\*, 7
* Learning Python: Chapters 10, 11, 12

Suggested Exercises:

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

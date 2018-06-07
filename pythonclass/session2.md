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

{% highlight python %}
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

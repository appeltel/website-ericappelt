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

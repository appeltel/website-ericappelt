---
layout: blogpost 
title: Playtime in the Dunders
category: writing
---

# Playtime in the Dunders

These are materials to accompany my
[PyOhio talk](https://www.pyohio.org/2018/schedule/presentation/57/)
on improving ones python skills through having fun with the
double underscore (dunder) special python methods.

### CarKeys

The misfit class:

{% highlight python %}
import random

class CarKey:
    """
    Gets lost easily
    """
    def __hash__(self):
        return random.randint(1, 2)
{% endhighlight %}

Some ideas:

* Try making a dictionary keyed by `CarKey` objects.
  * See what happens when you assign to keys, retrieve values
* Look at sets that contain `CarKey` objects
  * Add a `CarKey` to the set multiple times.
* Try changing the `CarKey` hash to return either 1 or 9.
  * As of CPython 3.7.0, dictionaries start with eight hash
    buckets. Try adding the 1-9 `CarKey` to a dictionary. Then
    observe the change in behavior when more keys are added.
  * For the truly curious, you can see how buckets are selected
    from the hash from the CPython
    [source code comments](https://github.com/python/cpython/blob/c6dabe37e3c4d449562182b044184d1756bea037/Objects/dictobject.c#L133-L223)
    (as of this writing)


### ChurchInt

The correctly adding version:

{% highlight python %}
def square(x):
    return x*x

def yolo(s):
    return s + 'YOLO'


class ChurchInt(int):
    """
    A Church Number
    """
    def __call__(self, fun):

        def new_fun(arg):
            for idx in range(self):
                arg = fun(arg)
            return arg

        return new_fun

    def __add__(self, other):
        return ChurchInt(super().__add__(other))
{% endhighlight %}

Addition at work:

```
>>> three = ChurchInt(3)
>>> four = ChurchInt(4)
>>> seven = three + four
>>> y7 = seven(yolo)
>>> y7('spam')
'spamYOLOYOLOYOLOYOLOYOLOYOLOYOLO'
```

* Try adding other mathematical operations.
  * Once you implement multiplication you can even do
    things like `square(three)(square)(2)`!

### NotDeadYet

"Resurrecting" version of the object:

{% highlight python %}
limbo = []

class NotDeadYet:
    """
    Not quite dead
    """
    def __del__(self):
        print("I'm not dead yet!")
        limbo.append(self)
{% endhighlight %}

* Try making the object and deleting all references to it.

Add an init method with a self reference:

{% highlight python %}
    def __init__(self):
        self.ref = self
{% endhighlight %}

Now the object will need to wait on the garbage collector for
destruction due to the circular reference. You can do
`import gc; gc.collect()` to make the garbage collector run.

---
layout: blogpost
title: Session 14
---

# Python Performance, Multithreading, Multiprocessing

### Suggested Readings

* Automate Stuff: Chapter 18

### Suggested Exercises

* Take an intensive function from your research code or interests and
  run it over an array of values using both threading and multiprocessing
  as was done in the session.
* If you don't have a good example function from your research you can use
  the very slow recursive Fibonacci number function, or find another
  numeric example, such as a [primality test](https://en.wikipedia.org/wiki/Primality_test)

---

### Session Notes

#### Python performance

We start with some slides discussing python performance, memory usage, and
bytecode:

* [Session slides](slides_lesson_14.pdf)

* As with the slides try using the `dis` module to decompile and
  understand a function. Look at `fcn.__code__.co_code` to see the actual
  bytecode

#### Matrix Inversion example

* We will use a pure python Lower-Upper decomposition matrix inversion
  routine to explore multithreading and multiprocessing in python.
* The code is [here](matrix_invert.py)

Serial example:

{% highlight python %}
import datetime
import random

from matrix_invert import *


random.seed(42)

# target function to invert matrices
def invert(matrix):
    P = lup_decompose(matrix)
    return lup_invert(matrix, P)

# Generate the list of matrices
input_matrices = [generate_matrix(300) for _ in range(4)]

# Timestamp when we begin
before = datetime.datetime.utcnow()

# run the inversions
inverses = []
for matrix in input_matrices:
    inverses.append(invert(matrix))

# Add the element (50,50) of all inverses, call that our result
result = sum(M[50][50] for M in inverses)

# Calculate elapsed time
after = datetime.datetime.utcnow()
elapsed = (after - before).total_seconds()

print('Inverted 4 300x300 matrices.')
print('Sum of M^-1[50][50] is {}'.format(result))
print('Time elapsed: {0:.3f}s'.format(elapsed))
{% endhighlight %}

Now here is another attempt using threads. The python Global
Interpreter Lock (GIL) prevents us from seeing any improvement:

{% highlight python %}
import datetime
import random
import threading

from matrix_invert import *


random.seed(42)

# target function to invert matrices
def invert(matrix, output_list):
    P = lup_decompose(matrix)
    output_list.append(lup_invert(matrix, P))

# Generate the list of matrices
input_matrices = [generate_matrix(300) for _ in range(4)]

# Timestamp when we begin
before = datetime.datetime.utcnow()

# run the inversions
tasks = []
inverses = []
for matrix in input_matrices:
    task = threading.Thread(target=invert, args=(matrix, inverses))
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()

# Add the element (50,50) of all inverses, call that our result
result = sum(M[50][50] for M in inverses)

# Calculate elapsed time
after = datetime.datetime.utcnow()
elapsed = (after - before).total_seconds()

print('Inverted 4 300x300 matrices.')
print('Sum of M^-1[50][50] is {}'.format(result))
print('Time elapsed: {0:.3f}s'.format(elapsed))
{% endhighlight %}

Here is an example using multiprocessing, but this one does not
work at all as each process does not share memory, the results of
each inversion are not passed to the parent process's list:

{% highlight python %}
import datetime
import random
import multiprocessing

from matrix_invert import *


random.seed(42)

# target function to invert matrices
def invert(matrix, output_list):
    P = lup_decompose(matrix)
    output_list.append(lup_invert(matrix, P))

# Generate the list of matrices
input_matrices = [generate_matrix(300) for _ in range(4)]

# Timestamp when we begin
before = datetime.datetime.utcnow()

# run the inversions
tasks = []
inverses = []
for matrix in input_matrices:
    task = multiprocessing.Process(target=invert, args=(matrix, inverses))
    task.start()
    tasks.append(task)

for task in tasks:
    task.join()

# Add the element (50,50) of all inverses, call that our result
result = sum(M[50][50] for M in inverses)

# Calculate elapsed time
after = datetime.datetime.utcnow()
elapsed = (after - before).total_seconds()

print('Inverted 4 300x300 matrices.')
print('Sum of M^-1[50][50] is {}'.format(result))
print('Time elapsed: {0:.3f}s'.format(elapsed))
{% endhighlight %}


Here is an example using a `Queue` object to share results between
processes:

{% highlight python %}
import datetime
import random
import multiprocessing

from matrix_invert import *


random.seed(42)

# target function to invert matrices
def invert(matrix, queue):
    P = lup_decompose(matrix)
    queue.put(lup_invert(matrix, P))

# Generate the list of matrices
input_matrices = [generate_matrix(300) for _ in range(4)]

# Timestamp when we begin
before = datetime.datetime.utcnow()

# run the inversions
result_q = multiprocessing.Queue()
tasks = []
for matrix in input_matrices:
    task = multiprocessing.Process(target=invert, args=(matrix, result_q))
    task.start()

inverses = [result_q.get() for _ in range(4)]

# Add the element (50,50) of all inverses, call that our result
result = sum(M[50][50] for M in inverses)

# Calculate elapsed time
after = datetime.datetime.utcnow()
elapsed = (after - before).total_seconds()

print('Inverted 4 300x300 matrices.')
print('Sum of M^-1[50][50] is {}'.format(result))
print('Time elapsed: {0:.3f}s'.format(elapsed))
{% endhighlight %}

Note that `multithreading` also has a `Queue` class that can be used
to simplify threaded code in a similar fashion:

{% highlight python %}
import datetime
from queue import Queue
import random
import threading

from matrix_invert import *


random.seed(42)

# target function to invert matrices
def invert(matrix, queue):
    P = lup_decompose(matrix)
    queue.put(lup_invert(matrix, P))

# Generate the list of matrices
input_matrices = [generate_matrix(300) for _ in range(4)]

# Timestamp when we begin
before = datetime.datetime.utcnow()

# run the inversions
result_q = Queue()
for matrix in input_matrices:
    task = threading.Thread(target=invert, args=(matrix, result_q))
    task.start()

inverses = [result_q.get() for _ in range(4)]

# Add the element (50,50) of all inverses, call that our result
result = sum(M[50][50] for M in inverses)

# Calculate elapsed time
after = datetime.datetime.utcnow()
elapsed = (after - before).total_seconds()

print('Inverted 4 300x300 matrices.')
print('Sum of M^-1[50][50] is {}'.format(result))
print('Time elapsed: {0:.3f}s'.format(elapsed))
{% endhighlight %}

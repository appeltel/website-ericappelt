---
layout: blogpost
title: Session 15
---

# Intro to Numpy and Pandas

### Suggested Readings

* [Numpy Quickstart Tutorial](https://docs.scipy.org/doc/numpy/user/quickstart.html)
* [Pandas Tutorial and Cookbooks](https://pandas.pydata.org/pandas-docs/stable/tutorials.html)

### Suggested Exercises

* See tutorials above

---

### Session Notes

#### Numpy

Numpy provides high performance multidimensional arrays with homogenous types.

* We will go through some of the Numpy quickstart tutoral using the Anaconda3 distribution
  * Alternately, you can just `pip install numpy`, but this may take a while to compile and may not be
    fully optimized

After getting to know a little numpy, revisit the matrix example from the last session:

{% highlight python %}
import datetime
import random

import numpy as np

from matrix_invert import generate_matrix

random.seed(42)


# target function to invert matrices
def invert(matrix):
    return np.linalg.inv(matrix)

# Generate the list of matrices
input_matrices = [np.array(generate_matrix(300)) for _ in range(4)]

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

#### Pandas

Pandas offers high-performance lower-dimensional datatypes:

* `Series` - A one dimensional labeled array with homogenous type. Think of it like a typed, high-performance
  dictionary. You can create one from an appropriate dictionary
  * A `Series` is like a numpy `ndarray` and can be used in numpy functions.
  * It is dict-like

* `DataFrame` - A two dimensional labeled structure with columns of homogenous type. Think of it like a
  spreadsheet, CSV file, SQL Table, or dictionary of `Series` objects.

* Look at the [Intro to Data Structures](https://pandas.pydata.org/pandas-docs/stable/dsintro.html#dsintro) for
  more information

Do a csv read example with the following csv file, `food.csv`:

```
date,main,side,cost
2017-08-06,spam,eggs,5.6
2017-08-07,spam,apples,4.5
2017-08-08,spam,eggs,5.6
2017-08-09,ham,eggs,6.8
```

Now in the interpreter

```
>>> import pandas as pd
>>> stream = open('food.csv')
>>> df = pd.read_csv(stream)
>>> df.dtypes
date     object
main     object
side     object
cost    float64
dtype: object
>>> df.describe()
           cost
count  4.000000
mean   5.625000
std    0.939415
min    4.500000
25%    5.325000
50%    5.600000
75%    5.900000
max    6.800000
>>> df[['date']] = df[['date']].apply(pd.to_datetime)
>>> df.dtypes
date    datetime64[ns]
main            object
side            object
cost           float64
dtype: object
>>> df[['date', 'cost']]
        date  cost
0 2017-08-06   5.6
1 2017-08-07   4.5
2 2017-08-08   5.6
3 2017-08-09   6.8
>>> df[df['date'] > '2017-08-07']
        date  main  side  cost
2 2017-08-08  spam  eggs   5.6
3 2017-08-09   ham  eggs   6.8
>>> df[(df['date'] > '2017-08-07') & (df['cost'] > 6.0)]
        date main  side  cost
3 2017-08-09  ham  eggs   6.8
```

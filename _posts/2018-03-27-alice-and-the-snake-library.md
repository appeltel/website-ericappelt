---
layout: blogpost 
title: Alice and the Snake Library
category: writing
---

# Alice and the Snake Library

A children's story about the CPython Global Interpreter Lock

## Help Wanted

Alice was very smart and did well in school. One day, she saw a sign
that said, "help wanted at Snake Library". Alice was not a snake, but
she was curious, so she read the address on the sign and went to Snake
Library to ask about the job.

When she got to Snake Library the snakes were very happy to see her and
asked her to come in. They gave her some tea and cakes, and then told her
why they needed help. The snakes were very smart and good with their books,
but they did not have hands to move books around and write. They needed
a human to come and help that was smart and good with reading and writing.
The snakes were nice and fun to be around, so Alice took the job.

It turned out to be a strange job, but also exciting since Alice liked
books. The snakes had books of instructions of what to do, but these were
written in Snake. Alice didn't speak Snake, so she would read the instructions
out loud to one of the snakes, and that snake would explain to her what that
instruction meant. Usually this would involve getting a book off the shelf,
putting it on a stack, taking a book off a stack, writing something down
in a book, or putting books back on the shelf. Sometimes there would be
math, like adding or multiplying numbers, but she would need help with this
too as the numbers were written in Snake. Every now and then the instructions
would say to take a book to the post office and mail it far away, or go and
wait for a new book to arrive.

## Another human

One morning Alice came in to work and the snakes handed her a golden key.
They said that from now on she would need to use the golden key to open the
big human door and it that would lock behind her. They said that there would
be another human coming to help the snakes, and his name was Bob. 
The snakes said that it was very important that only one human be in the
library at a time, reading instructions, stacking books, and writing things
down. After some time, the snakes would tell her to leave and give Bob the
key so that he could work for a while.

Alice asked, "But why can Bob and I not both work here at once? The library
is very large, and we could each have a different snake help us read the
instructions?" One snake started to explain that they had just set things up
that way, and if Alice and Bob were both supposed to write in the same book
at the same time, everything would get garbled. Another snake said that they
could solve that problem, but yet another snake said that would slow everything
down when only Alice or Bob was working. The snakes spent the rest of the
afternoon arguing and hissing at each other. Alice decided not to ask
this question again.

As Alice and Bob took turns going into the library and working on the snake
books, Alice wondered why they hired Bob at all. It was nice having the
company of another human, but overall it just slowed things down a bit, since
only one of them could work at a time and they wasted time going in and out
of the library.

Then while Alice was in the library working, she read an instruction out loud,
and the snake said that it meant to take a certain book to the post office.
Alice left the library where Bob was waiting outside, and she handed him the
key. Bob went into the library and started working. As Alice walked down the
road to the post office, she realized that it did make sense for the snakes
to hire Bob. If it was only her working for the snakes, then no work would
get done while she walked to the post office. With two humans working, one
could follow instructions in the library while the other walked to the post.

## A lot of math

One day Alice came to work in the morning and saw not just Bob, but her
friends Chelsea, Daniel, Erica, and Ferdinand waiting outside. They said that
they had all been hired by Snake Library to help. Alice used her golden key
to go into the library while everyone else waited. Inside, she asked the
snakes if there was going to be a lot of trips to the post office. Surely
there must be a lot to take, since otherwise it wouldn't make sense to
hire so many humans, since only one could work in the library at a time.
The snakes told her, no - this week they needed to do a lot of math, and they
needed to do it fast.

She asked, "But how will all these people help with
doing math, since only one of us can be in the library at a time getting
help from a snake?". The snakes pointed at a big package labeled "Numpy".
The first task of the day was to unpack the new books and put them on the
shelf. As Alice was working on this, the snakes explained that these were
special books. The first and last few pages were written in snake, but most
of the book would be written in human. Once the snakes helped Alice get
started into one of the math problems, she would be able to take the book
outside and work on the math problems alone. Once she got to the last part,
she would have to wait to get the golden key and go back into the library.

Alice got to work on one of the books and took it outside, handing the key
to Daniel. Alice started doing the math problems written in human. Since she
didn't have to read them out loud to a snake, she could do the math
problems much faster. But there were a lot of math problems in the book!
While she was doing the problems, Daniel came out with his own math book,
then Bob, Chelsea, Ferdinand, and finally Erica. Everyone was sitting outside
doing math problems on a beautiful sunny day. When Alice got to the last
part of the book written in snake, she took the golden key and went back
into the library. She didn't even have to wait for the key since everyone
else was busy doing math problems outside.

All through the day, everyone sat outside doing math problems. Every now and
then someone would finish and go back inside to get a new book, but since
most of the time was spent outside no one had to wait very long for the
golden key. They got a lot of math done that day, and the snakes were very
happy. The End.

# Moral of the Story

The library and snakes represent the python interpreter, and the books
represent python objects and instructions. The "snake language" is the python
bytecode, which are not native instructions for the CPU but must be
processed via the interpreter. The humans represent individual execution
threads, and the golden key is the Global Interpreter Lock (GIL).

The GIL prevents any two threads from simultaneously executing python
bytecode instructions. However, when there is IO to be performed, represented
by going to the post office, a thread will release the GIL so that other
threads can execute python bytecode instructions.

The GIL doesn't prevent computation in general, just the interpretation of
_python bytecode_. High-performance numerical packages like Numpy perform
operations on large arrays of data using machine instructions, and are
generally written in C or another compiled language. While these large
computations are being performed, the thread can release the GIL since
it isn't manipulating python objects outside its array of numerical data.

So the CPython GIL isn't quite as restrictive as it might first seem. For
IO-bound network applications, threads are spending most of their time
waiting on network traffic and not executing python instructions. For
high-performance numerical work, python is a slow interpreted language
anyway, so it makes sense to rewrite the bulk of the work in C. When this
is done right, it is possible to release the GIL while performing
computational work written in compiled code.

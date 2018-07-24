---
layout: blogpost
title: Session 10
---

# Classes Part II

### Suggested Readings

* Automate Stuff: Chapter 14
* Learning Python: Chapters 29\*, 30\*, 31\*, 32\*

### Suggested Exercises

* Make a `TrackingDiceSet` subclass of our `DiceSet` class that keeps track 
  of all the values that have been rolled in a list:
  * Use `super()` when implementing `roll()` which should both return the
    value of the roll and append it to a list stored as an attribute
  * Use `@property` decorators to encode changes to number, sides, and base.
    When one of these properties is changed, append a tuple encoding the
    previous value and number of rolls that have been performed so far
    as a tuple in a list
  * Add a method to allow you to lookup the number, sides, and base that
    the `DiceSet` had for a particular roll in the history by index and
    return these properties as a tuple.
* Extend the `WeightedDiceSet` using `__add__` so that you can add two
  `WeightedDiceSet` classes with the resultant weights being
   appropriately averaged.
  * Now use the `isinstance` built-in method to allow adding
    `WeightedDiceSet` to a regular `DiceSet` by treating the regular
    `DiceSet` as having weights of 1 and returning a `WeightedDiceSet`
     with this averaged in.
  * Notice what happens when you add a `WeightedDiceSet` to a `DiceSet`
    but switch the order of the objects on either side of the `+` operator.
    You can implement the `__radd__` method of the `WeightedDiceSet` to do
    the same thing as `__add__` (or just call it) and fix this behavior
    to always use `__add__` as defined in `WeightedDiceSet` when the object
    is added to a regular `DiceSet`

---

### Session Notes

---

### Preliminary Session Notes

These are scanned, handwritten notes to be replaced with typed notes:

* [Preliminary Session Notes](Python_lesson_10.pdf)

I will keep these available until the typed and updated notes are complete.

Shapes
======

This binary lets you create and modify some predefined shapes.

There are several red herrings in this binary, that seem to not be exploitable.
However, the (probably) easiest way to exploit this binary is a type confusion in `circlesize` since the `shape_id` is parsed two times in different ways.
With this type confusion, one can set the size of a polygon to an arbitrary value and read out of bounds.
Since the flag is on the heap, this leaks the flag.

I solved this challenge after the competition was over.

## The binary

### Shape-IDs
0: Triangle
1: Square
2: Circle
3: Polygon

### Functions
* `create(shape_type)` creates a new empty shape
* `print()` calls system with some fix string (which is on the heap for whatever reason)
* `addpoint(shape_id, x, y)` (poly only)
* `getpoint(shape_id, point_id)` (poly only)
* `modpoint(shape_id, point_id, new_x, new_y)` (poly only)
* `circlesize(shape_id, new_size)` (circle only)

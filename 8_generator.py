"""
In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.

Generators are useful when we want to produce a large sequence of values,
 but we don't want to store all of them in memory at once.

When the generator function is called, it does not execute the function body immediately. Instead,
it returns a generator object that can be iterated over to produce the values.


"""


def top_ten_perfect_squares():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = top_ten_perfect_squares()   # Gives an iterator
print(type(values))

for val in values:
    print(val)


# OR
# Since its iterator.
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())
# print(values.__next__())

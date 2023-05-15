#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    """
    Adds the first two element of two tuples together
    and return result
    """

    span_a = len(tuple_a)
    span_b = len(tuple_b)
    new_tupple = ()
    for k in range(2):
        if k >= span_a:
            a = 0
        else:
            a = span_a[k]
            if k >= span_b:
                b = 0
            else:
                b = span_b[k]

                if (k == 0):
                    new_tupple = (a + b)
                else:
                    new_tupple = (new_tupple, a + b)
                    return (new_tupple)


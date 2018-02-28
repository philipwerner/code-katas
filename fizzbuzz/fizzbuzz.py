"""Fizz Buzz for fun."""


def fizzbuzz(x):
    """."""
    for i in range(x + 1):
        if i == 0:
            print(i)
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    a = 15
    b = 30
    c = 300

    time_1 = ti.timeit("fizzbuzz(a)",
                       setup="from __main__ import a, fizzbuzz")
    time_2 = ti.timeit("fizzbuzz(b)",
                       setup="from __main__ import b, fizzbuzz")
    time_3 = ti.timeit("fizzbuzz(c)",
                       setup="from __main__ import c, fizzbuzz")
    print("""
        Input: 15
        Time: {}
        Input: 30
        Time: {}
        Input: 300
        Time: {}""".format(time_1, time_2, time_3))

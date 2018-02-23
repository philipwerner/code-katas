"""Code challenge to add zeros in front of 1 to the nth."""


def add_while(x):
    """While loop version."""
    output = "1"
    counter = 0
    print(output)
    while(counter < x):
        output = "0" + output
        counter += 1
        print(output)


def add_for(x):
    """For loop version."""
    output = "1"
    print(output)
    for i in range(x):
        output = "0" + output
        print(output)


def add_if(x):
    """If method."""
    output = "1"
    while(x):
        if len(output) < 2 and len(output) > 0:
            print(output)
        elif len(output) < x + 1:
            output = "0" + output
            print(output)
        elif len(output) == x + 1:
            print(output)
            x = 0

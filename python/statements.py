"""Demonstrates peculiarities of if, for, while and other statements.
"""


#%%
def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings and numbers, but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """

    from datetime import date
    d1 = date(1942, 6, 18)
    d2 = date.today()
    d3 = date(1942, 6, 18)

    if d1 == d3:
        print(True)
    else:
        print(False)

    if id(d1) == id(d3):
        print(True)
    else:
        print(False)

    print()

    a = 1
    b = 1
    if id(a) == id(b):
        print(True)
    else:
        print(False)

    print()

    if 'Paul':
        print(True)
    else:
        print(False)
    print()

    i = int(input('Enter an int: '))
    if i > 5:
        print('\ni > 5')
    elif i > 7:
        print('\ni > 7')
    elif i > 8:
        print('\ni > 8')
    else:
        print('\ni < 5')
    print()

    return

#%%


# Test demonstrate_branching()
demonstrate_branching()

#%%


def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    - it is not necessary to iterate through all elements of an iterable
    - step in range()
    - unimportant counter (_)
    - break and continue
    - while loop
    """

    from random import seed, randint
    seed(12)
    l = []
    for i in range(100):
        l.append(randint(10, 20))
    for i in range(10, 20, 2):
        print(i, l[i])
    print()

    for _ in range(5):
        print('Paul McCartney')
    print()

    return


#%%
# Test demonstrate_loops()
demonstrate_loops()

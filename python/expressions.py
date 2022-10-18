"""Demonstrates how operators and expressions work in Python.
"""

from settings import *


#%%
def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    Arithmetic operators in Python are pretty much the same as in other programming languages.
    The integer division operator: //
    """

    print(2**3 // 3 + 5 % 2)
    return


#%%
# Test demonstrate_arithmetic_operators()
demonstrate_arithmetic_operators()

#%%


def demonstrate_relational_operators():
    """Working with relational operators.
    - simple comparisons
    - comparing dates (== vs. is)
    - comparing dates (>, <, etc. with dates)
    - None in comparisons, type(None)
    """

    print(1 == 2)
    a = 'Paul'
    b = 'Paul'
    print(a == b)
    print(a is b)
    print()

    from datetime import date
    d1 = date(1942, 6, 18)
    d2 = date.today()
    today = date.today()
    print(d1 == d2)
    print(d1 is d2)
    print(d2 == today)
    print(d2 is today)
    print()

    print(d1 > d2)
    # print(d1 > None)
    print(d1 == None)
    print(d1 is None)
    return


#%%
# Test demonstrate_relational_operators()
demonstrate_relational_operators()

#%%


def demonstrate_logical_operators():
    """Working with logical operators.
    - logical operations with True, False and None
    - logical operations with dates
        - make sure to read this: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not !!!
          (or just this: https://stackoverflow.com/questions/44612144/logical-operators-in-python)
    - logical operations with None (incl. None and int, None and date, etc.)
    - None and date vs. None > date
    """

    print((1 > 2) and (3 > 2))
    print(not (1 > 2) and (3 > 2))
    print(not (1 > 2) and None)
    print()

    from datetime import date
    d1 = date(1942, 6, 18)
    d2 = date.today()
    print(d1 and d2)
    print(None or 23)
    print()

    # print(d1 > None)
    print(d1 is None)

    return


#%%
# Test demonstrate_logical_operators()
demonstrate_logical_operators()


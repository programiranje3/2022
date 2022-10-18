"""Demonstrates working with strings in Python.
"""

import string

import settings


#%%
def demonstrate_formatting():
    """Demonstrating details of string formatting.
    - using classical formatting
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """

    print('Paul %s was born in %d.' % ('McCartney', 1942))
    print()

    print('Paul\n')
    print('C:\next')
    print(r'C:\next')
    print()

    paul = """Paul 
    McCartney"""
    print(paul)
    print()

    print('Paul ' * 3)
    print()

    print('Paul McCartney'[0:4])
    print('Paul McCartney'[:4])
    print('Paul'[4:])
    print('Paul'[4:-3])
    print()

    print('\tPaul')
    print(repr('\tPaul'))

    return


#%%
# Test demonstrate_formatting()
demonstrate_formatting()

#%%


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    print('Paul {0} was born in {1}.'.format('McCartney', 1942))
    return


#%%
# Test demonstrate_fancy_formatting()
demonstrate_fancy_formatting()

#%%


def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """

    paul = 'Paul'
    city = 'Liverpool'
    year = 1942
    print(f'{paul + " McCartney"} was born in {city} in {year}.')
    return


#%%
# Test demonstrate_fancy_formatting_with_f_strings()
demonstrate_fancy_formatting_with_f_strings()

#%%


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals()), len(), ..., strip() (lstrip(), rstrip())
    """

    print('Paul McCartney'.endswith('McCartney'))
    print('Paul McCartney'.split())
    print('Paul McCartney'.split('Paul '))
    print('Paul McCartney'.center(10, '*'))
    print('Paul McCartney'.upper())
    print('   Paul McCartney  '.rstrip(), end='')
    print('   Paul McCartney  '.lstrip())
    print('   Paul McCartney  '.strip())
    print(len('Paul McCartney'))
    return


#%%
# Test demonstrate_string_operations()
demonstrate_string_operations()

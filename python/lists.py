"""Demonstrates working with lists.
"""


#%%
def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    paul = ['Paul McCartney', True, 1942]
    mcCartney = ['Paul McCartney', True, 1942]

    print(paul)
    print()

    print(paul[1:])
    print(paul[-2:])
    print()

    print(paul == mcCartney)
    print(paul is mcCartney)
    print()

    print(paul + mcCartney)
    print()

    for i in range(len(paul)):
        print([paul[i]])
    return


#%%
# Test demonstrate_lists()
demonstrate_lists()

#%%


def demonstrate_list_methods():
    """Using
    append()
    insert()
    remove()
    pop()
    extend()
    count()
    index()
    reverse()
    len()
    ...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """

    paul = ['Paul McCartney', True, 1942]
    print(paul)

    print(paul.append('Liverpool'))
    print(paul)
    paul.remove(1942)
    print(paul)
    paul.insert(2, 1942)
    print(paul)
    paul.pop()
    print(paul)
    paul.extend(['McCartney', 'Liverpool'])
    print(paul)
    print(paul.count('McCartney'))
    print(paul.index('McCartney'))
    paul.reverse()
    print(paul)
    print()

    print('McCartney' in paul)
    print('The Beatles' not in paul)

    return


#%%
# Test demonstrate_list_methods()
demonstrate_list_methods()

#%%


def demonstrate_arrays():
    """Using array.array() to build list-based numeric arrays.
    Demonstrating that lists and arrays are different types.
    """

    from array import array
    a = array('i', [1, 2, 3, 4])
    print(type(a))
    print(a)
    for i in a:
        print(i)
    return


#%%
# Test demonstrate_arrays()
demonstrate_arrays()

#%%


def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """

    from random import seed, randint

    seed(12)

    l = []
    for _ in range(10):
        l.append(randint(1, 10))
    print(l)

    return


#%%
# Test populate_empty_list()
populate_empty_list()

#%%


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """

    paul = ['Paul McCartney', True, 1942]
    mcCartney = paul
    print(paul == mcCartney)
    print(paul is mcCartney)
    print()

    mcCartney = paul.copy()
    print(paul == mcCartney)
    print(paul is mcCartney)
    print()

    mcCartney = paul + []
    print(paul == mcCartney)
    print(paul is mcCartney)
    print()

    mcCartney = paul[:]
    print(paul == mcCartney)
    print(paul is mcCartney)
    print()

    return


#%%
# Test duplicate_list()
duplicate_list()

#%%


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    songs = ['Hey Jude', 'Eleanor Rigby', 'Let It Be', 'Penny Lane']

    first_words = [song.split()[0] for song in songs]
    print(first_words)
    first_letters = [word[0] for word in first_words]
    print(first_letters)
    result = ''.join(first_letters)
    print(result)
    result = ''.join(first_letters).lower().capitalize() + '!'
    print(result)
    result = ''.join([song.split()[0][0] for song in songs]).lower().capitalize() + '!'
    print(result)

    return


#%%
# Test demonstrate_list_comprehension()
demonstrate_list_comprehension()


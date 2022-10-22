"""Demonstrates dictionaries.
From: https://qr.ae/TWCAvj:
Python uses dictionaries all over the place:
- the variables and functions in a module - stored in a dictionary  # can be shown using globals()
- the local variables in a function - stored in a dictionary        # can be shown using locals(); see functions.py
- the implementation of a function - a dictionary
- a class is a dictionary
- an instance of a class is another dictionary
- the modules your program has imported - you guessed it - another dictionary
- even Python set objects are implemented as modified dictionaries
To paraphrase Tim Peter's 'Zen of Python': "dictionaries are great - let's do more of them".
Read more at https://qr.ae/TWCAvj.
"""


#%%
def demonstrate_dictionaries():
    """Creating and using dictionaries.
    - create a blank (empty) dictionary
    - create a non-empty dictionary
    - access dictionary values by the corresponding keys (syntax: value = d[key])
    - print a non-empty dictionary
        - print all items using the items() function
        - print one item per line
    - pprint dictionary in one column
    - add/remove items to/from a dictionary
    - update a dictionary with the items from another dictionary or from an iterable of (k, v) pairs using dict.update()
    - using the keys() and values() functions
    """

    paul = {}
    print(type(paul))
    print(paul)
    print()

    paul = {'name': 'Paul McCartney', 'city': 'Liverpool', 'year': 1942}
    print(paul)
    print()

    print(paul['name'])
    print()

    print(paul.items())
    print(list(paul.items()))
    print()

    for k, v in paul.items():
        print(k, v)
    print()
    for i in list(paul.items()):
        print(i)
    print()

    from pprint import pprint
    pprint(paul, width=1)
    print()

    paul['alive'] = True
    pprint(paul, width=1)
    print()

    bands = {'first band': 'The Beatles', 'second band': 'Wings'}
    paul.update(bands)
    pprint(paul)
    print()

    del paul['second band']
    pprint(paul)
    print()
    paul.pop('year')
    pprint(paul)
    print()

    songs = {1: 'Can\'t Buy Me Love', 2: 'The Fool on the Hill'}
    paul['songs'] = songs
    pprint(paul)
    print()

    paul.pop('songs')
    pprint(paul)
    print()

    paul.update([('deceased spouse', 'Linda')])
    pprint(paul)
    paul.pop('deceased spouse')
    pprint(paul)

    print(paul.keys())
    print(list(paul.keys()))
    print(paul.values())
    print(list(paul.values()))


#%%
# Test demonstrate_dictionaries()
demonstrate_dictionaries()


#%%
def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    - using zip()
    - using operator.itemgetter()
    - using lambda
    """

    # if by == 'k' or by == 'K':
    #     return dict(sorted(zip(d.keys(), d.values())))
    # elif by == 'v' or by == 'V':
    #     return dict(sorted(zip(d.values(), d.keys())))
    # else:
    #     return None

    # from operator import itemgetter
    #
    # if by == 'k' or by == 'K':
    #     return dict(sorted(d.items(), key=itemgetter(0)))
    # elif by == 'v' or by == 'V':
    #     return dict(sorted(d.items(), key=itemgetter(1)))
    # else:
    #     return None

    if by == 'k' or by == 'K':
        return dict(sorted(d.items(), key=lambda item: item[0]))
    elif by == 'v' or by == 'V':
        return dict(sorted(d.items(), key=lambda item: item[1]))
    else:
        return None


#%%
def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """

    from pprint import pprint

    songs = {2: 'The Long and Winding Road', 1: 'Oh, Darling', 3: 'Can\'t Buy Me Love'}
    # paul = {'name': 'Paul McCartney', 'city': 'Liverpool', 'year': 1942}
    paul = {'name': 'Paul McCartney', 'city': 'Liverpool', 'year': str(1942)}

    print(sort_dictionary(songs, by='v'))
    print(sort_dictionary(songs, by='d'))


#%%
# Test demonstrate_dict_sorting()
demonstrate_dict_sorting()


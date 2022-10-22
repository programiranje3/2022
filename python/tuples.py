"""Demonstrates tuples.
"""


#%%
def demonstrate_tuples():
    """Creating and using tuples.
    - create and print empty tuple, 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    empty_tuple = ()
    print(type(empty_tuple))
    print(empty_tuple)
    one_tuple = (1, )
    print(one_tuple)
    pair = (1, 3, )
    print(pair)
    triplet = (1, 5, 8, )
    print(triplet)
    paul = ('Paul McCartney', 'Liverpool', 1942, True)
    print(paul)
    print(paul[2])
    print()
    for i in paul:
        print(i)
    # paul[2] = 'L'
    print()


#%%
# Test demonstrate_tuples()
demonstrate_tuples()


#%%
def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    paul = 'Paul McCartney', 'Liverpool', 1942, True
    print(paul)
    name, city, year, b = paul
    print(name, city, year, b)
    print({name, city, year, b})
    print(type({name, city, year, b}))
    print()


#%%
# Test demonstrate_packing()
demonstrate_packing()


#%%
def demonstrate_zip():
    """Using the built-in zip() function with tuples and multi-counter for-loop.
    - demonstrate zip object
    - demonstrate converting a zip object to a list object
    - demonstrate that a zip object is an iterator (must be re-initialized after looping)
    """

    members = ('John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr')
    birth_years = (1940, 1942, 1943, 1940)
    birth_places = ('Liverpool', 'Liverpool', 'Liverpool', 'Liverpool', )

    theBeatles = zip(members, birth_years, birth_places)
    print(theBeatles)
    print(list(theBeatles))
    print()

    theBeatles = zip(members, birth_years, birth_places)
    print(tuple(theBeatles))
    print()

    theBeatles = zip(members, birth_years, birth_places)
    for name, year, city in theBeatles:
        print(f'{name} was born in {year} in {city}.')


#%%
# Test demonstrate_zip()
demonstrate_zip()


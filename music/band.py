"""The class representing the concept of a music group/band.
It includes a list of Musician objects (band members) and the date when the band started performing together.

The corresponding exception classes are included as well.
File I/O and JSON encoding/decoding of Band objects are demonstrated too.
"""


import pickle
from datetime import date, datetime, time
import json
import sys

from music.musician_module import Musician
from util.utility import format_date, get_project_dir, get_data_dir

from testdata.musicians import *


#%%
class Band:
    """The class describing the concept of a music group/band.
    It includes a list of Musician objects (band members)
    and the dates when the band started/stopped performing together.
    """

    # Class variables: like static fields in Java; typically defined and initialized before __init__()
    # Insert a class variable (static field), such as genres, date_pattern,...

    genres = ['rock', 'blues', 'pop', 'alternative', 'unknown']

    def __init__(self, name, *members, start=date.today(), end=date.today()):
        # pass                                            # introduce and initialize iterator counter, self.__i

        # Code to check if the band name is specified correctly (possibly raises BandNameError)

        self.name = name
        self.members = members
        self.start = start
        self.end = end
        self.__i = 0

    def __str__(self):
        n = self.name
        m = f'({", ".join([member.name for member in self.members]) if self.members else "members unknown"})'
        s = self.start.year
        e = self.end.year
        return f'{n} {m}, {s}-{e}'

    def __eq__(self, other):
        # Musician objects are unhashable, so comparing the members tuples from self and other directly does not work;
        # see https://stackoverflow.com/a/14721133/1899061, https://stackoverflow.com/a/17236824/1899061
        # return self == other if isinstance(other, Band) else False    # No! Musician objects are unhashable!
        # However, this works:
        # return self.__dict__ == other.__dict__ if isinstance(other, Band) else False

        t = isinstance(other, Band)
        n = self.name == other.name

        # # members must be compared 'both ways', because the two tuples can be of different length
        # m_diff_1 = [x for x in self.members if x not in other.members]
        # m_diff_2 = [x for x in other.members if x not in self.members]
        # m = len(m_diff_1) == len(m_diff_2) == 0

        # members must be compared 'both ways', because the two tuples can be of different length
        m = all([x in self.members for x in other.members]) and all([x in other.members for x in self.members])

        y = (self.start == other.start) and (self.end == other.end)
        return t and n and m and y

    @staticmethod
    def is_date_valid(d):
        """It is assumed that a band does not perform together since more than ~60 years ago.
        So, the valid date to denote the start of a band's career is between Jan 01, 1960, and today.
        """

        return date(1954, 7, 5) <= d <= date.today() if isinstance(d, date) else False

    def __iter__(self):
        """Once __iter__() and __next__() are implemented in a class,
        we can create an iterator object by calling the iter() built-in function on an object of the class,
        and then call the next() built-in function on that object.
        It is often sufficient to just return self in __iter__(),
        if the iterator counter such as self.__i is introduced and initialized in __init__().
        Alternatively, the iterator counter (self.__i) is introduced and initialized here.
        """

        self.__i = 0
        return self               # sufficient if the iterator counter is introduced and initialized in __init__()

    def __next__(self):
        if self.__i < len(self.members):
            next_m = self.members[self.__i]
            self.__i += 1
            return next_m
        else:
            raise StopIteration


#%%
# Check class variables
print(Band.genres)


#%%
# Test the basic methods (__init__(), __str__(),...)
theBeatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr, ],
                  start=date(1957, 7, 6), end=date(1970, 4, 10))
print(theBeatles)
beatles = Band('The Beatles', *[johnLennon, georgeHarrison, paulMcCartney, ringoStarr, Musician('Pete Best')],
               start=date(1957, 7, 6), end=date(1970, 4, 10))
print(theBeatles == beatles)
# print(set(list(theBeatles.members)) == set([johnLennon, georgeHarrison, paulMcCartney, ringoStarr]))
# print(type(theBeatles.members))
# print(set(theBeatles.members))


#%%
# Test the date validator (@staticmethod is_date_valid(<date>))
print(Band.is_date_valid(date(1957, 7, 6)))


#%%
# Test the iterator
for _ in range(len(theBeatles.members)):
    print(theBeatles.__next__().name)
# print(theBeatles.__next__().name)             # iterator exhausted, must be re-initiated
print()

# i = iter(theBeatles)
# print(i)
i = iter(theBeatles)                            # re-initiating the iterator
for _ in range(len(theBeatles.members)):
    print(next(theBeatles))
print()

# # Alternatively
# theBeatles.__iter__()
# for _ in range(len(theBeatles.members)):
#     print(theBeatles.__next__().name)
# print()

# Repeated attempt to run the iterator fails, because the iterator is exhausted


#%%
def next_member(band):
    """Generator that shows members of a band, one at a time.
    yield produces a generator object, on which we call the next() built-in function.
    A great tutorial on generators: https://realpython.com/introduction-to-python-generators/.
    """

    for member in band.members:
        input('Next: ')
        yield member
        print('Yeah!')


#%%
# Test next_member(band)
member_generator = next_member(theBeatles)
print(member_generator)
print(type(member_generator))
print()

while True:
    try:
        print(next(member_generator))
    except:
        break


#%%
# Demonstrate generator expressions
print(i**2 for i in range(4))
print(next((i**2 for i in range(4))))
print(next((i**2 for i in range(4))))
ge = (i**2 for i in range(4))
print(ge)
print(next(ge))     # 0
print(next(ge))     # 1
print(next(ge))     # 4
print(next(ge))     # 9
# print(next(ge))     # raises StopIteration


#%%
class BandEncoder(json.JSONEncoder):
    """JSON encoder for Band objects (cls= parameter in json.dumps()).
    """

    def default(self, band):
        # recommendation: always use double quotes with JSON

        pass


#%%
def band_py_to_json(band):
    """JSON encoder for Band objects (default= parameter in json.dumps()).
    """


#%%
def band_json_to_py(band_json):
    """JSON decoder for Band objects (object_hook= parameter in json.loads()).
    """


#%%
# Demonstrate JSON encoding/decoding of Band objects

# Using the json_tricks module from the json-tricks external package (https://github.com/mverleg/pyjson_tricks).
# From the package documentation:
# The JSON string resulting from applying the json_tricks.dumps() function stores the module and class name.
# The class must be importable from the same module when decoding (and should not have changed).
# If it isn't, you have to manually provide a dictionary to cls_lookup_map when loading
# in which the class name can be looked up. Note that if the class is imported, then globals() is such a dictionary
# (so try loads(json, cls_lookup_map=glboals())).
# Also note that if the class is defined in the 'top' script (that you're calling directly),
# then this isn't a module and the import part cannot be extracted. Only the class name will be stored;
# it can then only be deserialized in the same script, or if you provide cls_lookup_map.
# That's why the following warning appears when serializing Band objects in this script:
# UserWarning: class <class '__main__.Band'> seems to have been defined in the main file;
# unfortunately this means that it's module/import path is unknown,
# so you might have to provide cls_lookup_map when decoding.

# Single object

# List of objects


#%%
class BandError(Exception):
    """Base class for exceptions in this module.
    """

    pass


#%%
class BandNameError(BandError):
    """Exception raised when the name of a band is specified incorrectly.
    """


#%%
# Demonstrate exceptions

#%%
# Catching exceptions - try-except block
try:
    for i in range(5):
        print(theBeatles.members[i])
except Exception as err:
    print()
    # print(err)
    # sys.stderr.write('\n' + str(type(err)) + ': ' + err.args[0] + '\n')
    sys.stderr.write(f'\n{type(err).__name__}: {err.args[0]}\n\n')

#%%
# Catching multiple exceptions and the 'finally' clause
try:
    for i in range(4):
        print(theBeatles.members[i])
    print(theBeatles / 4)
except IndexError as err:
    print()
    sys.stderr.write(f'\n{type(err).__name__}: {err.args[0]}\n\n')
except Exception as err:
    print()
    sys.stderr.write(f'\nCaught an exception: {type(err).__name__}: {err.args[0]}\n\n')
finally:
    print('Caught an exception. Stopped any further processing.')

#%%
# Using the 'else' clause (must be after all 'except' clauses)
try:
    for i in range(4):
        print(theBeatles.members[i])
except IndexError as err:
    print()
    sys.stderr.write(f'\n{type(err).__name__}: {err.args[0]}\n\n')
else:
    print(f'\nThat\'s all.')

#%%
# Catching 'any' exception - empty 'except' clause
try:
    for i in range(5):
        print(theBeatles.members[i])
except:
    print()
    sys.stderr.write(f'\nCaught an exception\n\n')

#%%
# Catching user-defined exceptions

#%%
# Demonstrate working with files
# theBeatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
#                   start=date(1957, 7, 6), end=date(1970, 4, 10))
# theRollingStones = Band('The Rolling Stones', *[mickJagger, keithRichards, ronWood, charlieWatts],
#                         start=date(1962, 7, 12))
# pinkFloyd = Band('Pink Floyd', *[sydBarrett, davidGilmour, rogerWaters, nickMason, rickWright])
# bands = [theBeatles, theRollingStones, pinkFloyd]

#%%
# Writing to a text file - <outfile>.write(str(<obj>), <outfile>.writelines([str(<obj>)+'\n' for <obj> in <objs>])

#%%
# Demonstrate reading from a text file - <infile>.read(), <infile>.readline()

#%%
# Demonstrate writing to a binary file - pickle.dump(<obj>, <outfile>)

#%%
# Demonstrate reading from a binary file - pickle.load(<infile>)



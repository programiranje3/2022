"""The very first Python script - main.py.
"""


#%%
# Hello world: the print() built-in function and the + operator.

print('Paul McCartney')
print('Paul McCartney', 'was born in', 1942)

# print('Paul McCartney', 'was born in', 1942 + '.')
print('Paul McCartney', 'was born in', str(1942) + '.')
print('Paul McCartney wrote \'Yesterday\' in \n' + str(1965))

#%%
# The input() built-in function

# print('Paul McCartney was born in: ')
# year = input()
# print('Paul McCartney was born in: ', end='')
# year = input()
# print('Paul McCartney was born in:', year + '.')

print('Paul McCartney was born in:', int(input()))

#%%
# A simple function and function call


def year_of_birth():
    print('Paul McCartney was born in: ', end='')
    year = input()
    return year


print(year_of_birth())

#%%
# A simple loop and the range() built-in function

for i in range(5):
    print(i)
print()

i = 0
while i < 5:
    print(i)
    i += 1

#%%
# A simple list, accessing list elements, printing lists

songs = ['Oh, Darling', 'The Long and Winding Road', 'She\'s a Woman']
print(songs[2])
print(songs)
print('; '.join(songs) + '.')

#%%
# Looping through list elements - for and enumerate()

for i in range(len(songs)):
    print(songs[i])
print()

for i, song in enumerate(songs):
    print(str(i + 1) + ':', song)
print()

print(enumerate(songs))
print(list(enumerate(songs)))
print(list(enumerate(songs, start=1)))
print()

for i, song in enumerate(songs, start=1):
    print(str(i) + ':', song)

#%%
# Global variables: __name__, __file__, __doc__,...

print(__name__)
# The following line doesn't work from a notebook, from a cell in a .py file and from a .py generated from a notebook,
# just from a .py file without cells
# print(__file__)
print(__doc__)
print(globals())

#%%
# Importing from another script

from inception import year_of_birth
print(year_of_birth())

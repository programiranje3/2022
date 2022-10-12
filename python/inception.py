"""The very first module in a more structured version of the project.
"""


#%%
# Moving code from main.py

# Hello world: the print() built-in function and the + operator.

# print('Paul McCartney')
# print('Paul McCartney', 'was born in', 1942)
# ...

print('Paul McCartney')
print('Paul McCartney', 'was born in', 1942)

#%%
# Keyboard input

# print('Paul McCartney was born in: ')
# year = input()
print('Paul McCartney was born in: ', end='')
year = input()
print('Paul McCartney was born in:', year + '.')

#%%
# A simple function and function call


def year_of_birth():
    """A simple function.
    """

    print('Paul McCartney was born in: ', end='')
    year = input()
    return year


#%%
print(year_of_birth())

#%%
# Printing with ' ' and printing without '\n'

# print('Paul McCartney', 'was born in', 1942 + '.')
print('Paul McCartney', 'was born in', str(1942) + '.')
print('Paul McCartney wrote \'Yesterday\' in \n' + str(1965))

songs = ['Oh, Darling', 'The Long and Winding Road', 'She\'s a Woman']
print(songs[2])
print(songs)
print('; '.join(songs) + '.')

#%%
# Printing with classical formatting (%)

city = 'Liverpool'
year = 1942
print('Paul McCartney was born in %s, in %d ' % (city, year))

#%%
# break and continue

for i in range(5):
    if i == 2:
        break
        # continue
    print(i)

#%%
# Printing docstrings

print(year_of_birth.__doc__)

#%%
# Printing a list using enumerate()

songs = ['The Long and Winding Road', 'Let It Be', 'Rocky Racoon']
for i, song in enumerate(songs, start=1):
    print(i, song)

#%%
# Importing from Standard Library

# Date format strings
# https://docs.python.org/3/library/datetime.html?highlight=date%20format%20strings#strftime-and-strptime-format-codes

from datetime import date
d = date(1942, 6, 18)
print(d)
date_formatting_string = '%b %d, %Y'
print(d.strftime(date_formatting_string))

#%%
# Testing print(__file__)

# The following line doesn't work from a notebook, from a cell in a .py file and from a .py generated from a notebook,
# just from a .py file without cells
# print(__file__)


#%%
# Taking care of the module __name__

if __name__ == '__main__':

    pass

"""Print out all the melons in our inventory."""

#grabs the dictionary from melons.py 
from melons import melons

#define the function and pass in the data from melons.py
def print_melon(melons):
    """Print each melon with corresponding attribute information."""
#First for loop, which iterates over the outermost key value pairs in melons - the melon name is the key and the nested dictionary is the value: THE ITEMS() METHOD MAKES THE PONY GO. the key value pairs can be called anything, but melons.items() has to use the parameter name.
for melon, specs in melons.items():
    print(f'\n')
    print(melon.upper())

    #This nested for loop iterates over the nested key value pairs that are the values in the outer for loop / dictionary. THE ITEMS() METHOD MAKES THE PONY GO. spec, detail are the key, value pairs. specs somes from the outer for loop.
    for spec, detail in specs.items():
        print(f'{spec}: {detail}')
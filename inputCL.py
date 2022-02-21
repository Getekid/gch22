#!/usr/bin/env python

import sys

def flatten(lists):
   return [item for sublist in lists for item in sublist]


lists = []
for i, line in enumerate(sys.stdin):
    if i == 0:
        no_of_clients = line
        print(no_of_clients)
    if i != 0:
        lists.append((line.rstrip('\n')).split(' ')) # lists.append([(line.rstrip('\n'))].split(' ')) no need for extra list iterator
        #print(lists)

print(lists)

ingredients = flatten(lists)
print(ingredients)
#ingredients = flatten(flatten(lists))
set_ingredients = set(ingredients)
print('Ingredients are :', ingredients)
print('Ingredients, as a set, are :', set_ingredients)

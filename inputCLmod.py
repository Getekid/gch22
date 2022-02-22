#!/usr/bin/env python

import sys
from one_pizza import Client

def flatten(lists):
   return [item for sublist in lists for item in sublist]


lists = []
liked_pizza = []
disliked_pizza = []
input()
for i, line in enumerate(sys.stdin):
    if i == 0:
        no_of_clients = line
        print(no_of_clients)
    if i != 0:
        lists.append((line.rstrip('\n')).split(' '))
        
        if i%2==1:
            liked_pizza.append(lists[i - 1])
        elif i%2==0:
            disliked_pizza.append(lists[i - 1])

print('Lists before flatten() is ', lists)
ingredients = flatten(lists)
print('Lists after flatten() is ', ingredients)

print('Liked pizza is :', liked_pizza)
print('Disliked pizza is :', disliked_pizza)
# #ingredients = flatten(flatten(lists))
# set_ingredients = set(ingredients)
# print('Ingredients are :', ingredients)
# print('Ingredients, as a set, are :', set_ingredients)
    #for i, line in enumerate(file)
    #print(line, 'number of line is ', i )

#for i in lists:
#	if i%2==0
#	lists[i]

clients = []
for j in range(len(liked_pizza)):
    liked = liked_pizza[j]
    disliked = disliked_pizza[j]
    clients.append(Client(liked[1:], disliked[1:]))

print(clients)

#!/usr/bin/env python

import sys

def flatten(lists):
   return [item for sublist in lists for item in sublist]


lists = []
liked_pizza = []
disliked_pizza = []
for i, line in enumerate(sys.stdin):
    if i == 0:
        no_of_clients = line
        print(no_of_clients)
    if i != 0:
        lists.append((line.rstrip('\n')).split(' ')) # lists.append([(line.rstrip('\n'))].split(' '))
        #lists.append(line.split(' '))
        #print(lists)
        print('Lists before flatten() is ', lists)
        ingredients = flatten(lists)
        print('Lists after flatten() is ', ingredients)
        
        if i%2==1:
            for j in range(1, len(lists), 1):						#lists instead of ingredients
                liked_pizza.append(lists[i])
                print('Ingredients in pizza, \'YES\': ', liked_pizza)
        elif i%2==0:
            for j in range(1, len(lists), 1):
                disliked_pizza.append(lists[i])
                print('Ingredients in pizza, \'NO\': ', disliked_pizza)
            

print(lists)

ingredients = flatten(lists)
print(ingredients)
liked_pizza = []
for i in range(1, len(ingredients), 1):
    liked_pizza.append(ingredients[i]) 

print('Liked pizza is :',liked_pizza)
#ingredients = flatten(flatten(lists))
set_ingredients = set(ingredients)
print('Ingredients are :', ingredients)
print('Ingredients, as a set, are :', set_ingredients)
    #for i, line in enumerate(file)
    #print(line, 'number of line is ', i )

#for i in lists:
#	if i%2==0
#	lists[i] 

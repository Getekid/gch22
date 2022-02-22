from one_pizza import Client
import time

t0 = time.time()


ingredients = set()
C = input()

clients = []
for i in range(int(C)):
    liked = input().split(' ')[1:]
    for ing in liked:
        ingredients.add(ing)

    disliked = input().split(' ')[1:]
    for ing in disliked:
        ingredients.add(ing)

    clients.append(Client(liked, disliked))

# print(clients)
print(len(ingredients))

print('Time elapsed:', time.time() - t0)

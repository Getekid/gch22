class Client:
    def __init__(self, likes, dislikes=None):
        if dislikes is None:
            dislikes = []
        self.likes = likes
        self.dislikes = dislikes
        self.cost = 0

    def dislikes_pizza(self, pizza):
        """Returns True if the pizza has any of the ingredients the client dislikes, False otherwise."""
        for ing in self.dislikes:
            if ing in pizza:
                return True
        return False

    def likes_pizza(self, pizza):
        """Returns True if the client likes the given pizza, False otherwise."""
        # All ingredients the Client likes must be in.
        for ing in self.likes:
            if ing not in pizza:
                return False
        # None of the ingredients the Client dislikes should be in.
        if self.dislikes_pizza(pizza):
            return False

        # If all the above fail, return True.
        return True

    def __repr__(self):
        return 'Client likes {0} and dislikes {1} with cost {2}'.format(self.likes, self.dislikes, self.cost)


C = input()

ingredients_cost = {}
clients = []
for i in range(int(C)):
    liked = input().split(' ')[1:]
    for ing in liked:
        if ing not in ingredients_cost:
            ingredients_cost[ing] = 0

    disliked = input().split(' ')[1:]
    for ing in disliked:
        ingredients_cost[ing] = 1 if ing not in ingredients_cost else ingredients_cost[ing] + 1

    clients.append(Client(liked, disliked))

# Build a list of the added costs for each client.
# This doesn't take into account overlaps, i.e. a client that dislikes two ingredients
# will be counted twice for a client that likes both.
for client in clients:
    cost = 0
    for ing in client.likes:
        cost += ingredients_cost[ing]
    client.cost = cost

# Sort the clients according to their cost.
clients_sorted = sorted(clients, key=lambda x: x.cost)

# Take the ingredients from clients in order of lower cost and ignore the ones disliking the building pizza.
# Also keep track of the disliked ingredients of the clients we accept and ignore those who like them.
best_pizza = set()
ingredients_banned = set()
for client in clients_sorted:
    if client.dislikes_pizza(best_pizza):
        continue
    if ingredients_banned and ingredients_banned.intersection(set(client.likes)):
        continue

    for ing in client.likes:
        best_pizza.add(ing)
    for ing in client.dislikes:
        ingredients_banned.add(ing)

print(len(best_pizza), ' '.join(best_pizza))

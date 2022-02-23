import networkx as nx
# from networkx.algorithms.clique import find_cliques
from networkx.algorithms.approximation.clique import max_clique


class Client:
    def __init__(self, likes, dislikes=None):
        if dislikes is None:
            dislikes = []
        self.likes = likes
        self.dislikes = dislikes

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
        return 'Client likes {0} and dislikes {1}'.format(self.likes, self.dislikes)


G = nx.Graph()

C = input()
for i in range(int(C)):
    liked = input().split(' ')[1:]
    disliked = input().split(' ')[1:]
    G.add_node(Client(liked, disliked))

# Build the Graph edges.
# An edge between two clients exists if they can both be served with one pizza,
# i.e. nothing the one likes the other dislikes and vice-versa.
G_l = list(G)
for i in range(G.number_of_nodes()):
    client = G_l[i]
    pizza_client = client.likes
    for j in range(i + 1, G.number_of_nodes()):
        client2 = G_l[j]
        pizza_client2 = client2.likes
        if not client.dislikes_pizza(pizza_client2) and not client2.dislikes_pizza(pizza_client):
            G.add_edge(client, client2)

# Find the Max-Clique to find the largest group of clients who can be served without ingredient conflicts.

# Approximation approach.
clique_maximum = max_clique(G)

# Deterministic approach.
# clique_maximum = find_cliques(G)
# clique_maximum = []
# clique_maximum_size = 0
# for clique in list(cliques):
#     if len(clique) > clique_maximum_size:
#         clique_maximum = clique
#         clique_maximum_size = len(clique)

# Build the best pizza from the maximum clique.
best_pizza = set()
for client in clique_maximum:
    for ing in client.likes:
        best_pizza.add(ing)

print(len(best_pizza), ' '.join(best_pizza))

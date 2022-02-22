#!/usr/bin/env python

clients = []
with open('input_data/c_coarse.in.txt', 'r') as file:
    for i, line in enumerate(file):
        if i == 0:
            continue

        if i % 2 == 1:
            liked = line.rstrip('\n').split(' ')[1:]
        elif i % 2 == 0:
            disliked = line.rstrip('\n').split(' ')[1:]
            clients.append(Client(liked, disliked))

print(clients)

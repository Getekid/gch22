#!/usr/bin/env python

with open('input_data/a_an_example.in.txt', 'r') as file:
    lists = []
    for i, line in enumerate(file):
        if i == 0:
            no_of_clients = line
            print(no_of_clients)
        if i != 0:
            lists.append([(line.rstrip('\n')).split(' ')])
            #print(lists)
print (lists)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}
len_sites = len(sites)
list_keys = list(sites.keys())
list_values = list(sites.values())
for item_start in range(len_sites-1):
    for item_end in range(item_start+1, len_sites):
        distances[list_keys[item_start] + '-' + list_keys[item_end]] = (
            ((list_values[item_start][0] - list_values[item_end][0])**2) +
            ((list_values[item_start][1] - list_values[item_end][1])**2)
        ) ** 0.5

pprint(distances)
distances = {}
# TODO здесь заполнение словаря
for item_start in range(len_sites):
    distances[list_keys[item_start]] = {}
    for item_end in range(len_sites):
        if item_start != item_end:
            distances[list_keys[item_start]][list_keys[item_end]] = round(((
                ((list_values[item_start][0] - list_values[item_end][0])**2) +
                ((list_values[item_start][1] - list_values[item_end][1])**2)
            ) ** 0.5), 2)

pprint(distances)

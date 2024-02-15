from src.graph.GItem import *

import random

nItems = 10
items = dict()

for i in range(0, 10):
  new_item = GItem(i)
  items[i] = new_item


L = len(items)
'''
for i in range(0, 10):
  a = random.randint(0, L)
  b = random.randint(0, L)
  if a != b :
    dbg = str(a) + "   --->   " + str(b)
    print(dbg)
    items[a].add_c(items[b])
'''
def add(a, b):
  dbg = str(a) + "   --->   " + str(b)
  print(dbg)
  items[a].add_c(items[b])

add(0, 4)
add(0, 5)
add(1, 6)
add(2, 6)
add(3, 5)

add(4, 7)
add(4, 9)
add(5, 8)
add(5, 9)
add(6, 9)

divider = "#" * 50
for i in range(0, L):
  s = divider + " CHILD(s) " + str(i)
  print(s)
  c = items[i].get_path_top_down_c()
  for ii in c:
    items[i].print_path(ii)

for i in range(0, L):
  s = divider + " PARENT(s) " + str(i)
  print(s)
  p = items[i].get_path_top_down_p()
  for ii in p:
    items[i].print_path(ii)

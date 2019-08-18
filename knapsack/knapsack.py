#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  grid = []
  for k in range(len(items)):
    row = [0] * capacity
    grid.append(row)

  for i in range(len(items)):
    item = items[i]
    for j in range(capacity):
      grid[i][j] = {'Value': 0, 'Chosen': [], 'size': 0}
      CC = j + 1
      current_cell = grid[i][j]
      if i == 0:
        if item.size <= CC:
          current_cell['Value'] += item.value
          current_cell['Chosen'].append(item.index)
          current_cell['size'] += item.size
      else:
        previous_max = grid[i-1][j]['Value']
        current_value = item.value
        remaining_index = j - item.size
        remaining_item = grid[i-1][remaining_index]
        if current_value + remaining_item['Value'] > previous_max and item.size + remaining_item['size'] <= CC:
            current_cell['Value'] = remaining_item['Value']
            current_cell['Value'] += current_value
            current_cell['Chosen'] = remaining_item['Chosen'][:]
            current_cell['Chosen'].append(item.index)
            current_cell['size'] = remaining_item['size']
            current_cell['size'] += item.size
        elif current_value > previous_max and item.size <= CC:
          current_cell['Value'] += item.value
          current_cell['Chosen'].append(item.index)
          current_cell['size'] += item.size
        else:
            current_cell['Value'] = previous_max
            current_cell['Chosen'] = grid[i-1][j]['Chosen'][:]
            current_cell['size'] = grid[i-1][j]['size']
  final_answer = grid[-1][-1]
  final_answer.pop('size')
  return final_answer
  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
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
      if i == 0:
        if item.size <= CC:
          grid[i][j]['Value'] += item.value
          grid[i][j]['Chosen'].append(item.index)
          grid[i][j]['size'] += item.size
      else:
        previous_max = grid[i-1][j]['Value']
        current_value = item.value
        remaining_index = j - item.size
        remaining_item = grid[i-1][remaining_index]
        if remaining_index > 0:
          if current_value + remaining_item['Value'] > previous_max and item.size + remaining_item['size'] <= CC:
            grid[i][j]['Value'] = remaining_item['Value']
            grid[i][j]['Value'] += current_value
            grid[i][j]['Chosen'] = remaining_item['Chosen'][:]
            grid[i][j]['Chosen'].append(item.index)
            grid[i][j]['size'] = remaining_item['size']
            grid[i][j]['size'] += item.size
          else:
            grid[i][j]['Value'] = previous_max
            grid[i][j]['Chosen'] = grid[i-1][j]['Chosen'][:]
            grid[i][j]['size'] = grid[i-1][j]['size']
        else:
          grid[i][j]['Value'] = previous_max
          grid[i][j]['Chosen'] = grid[i-1][j]['Chosen'][:]
          grid[i][j]['size'] = grid[i-1][j]['size']
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
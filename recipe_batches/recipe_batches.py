#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  differences = []
  for key, value in recipe.items():
    if key in ingredients:
      differences.append(ingredients[key] / value)
    else:
      return 0
  dishes = min(differences)
  if dishes < 1:
    return 0
  else:
    return math.floor(dishes)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
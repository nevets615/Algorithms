#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    numBatches = 0
    enough = True

    while enough:
        for key in recipe:
            if key in ingredients:
                if recipe[key] <= ingredients[key]:
                    ingredients[key] -= recipe[key]
                else:
                    enough = False
            else:
                enough = False
        if enough:
            numBatches += 1

    return numBatches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
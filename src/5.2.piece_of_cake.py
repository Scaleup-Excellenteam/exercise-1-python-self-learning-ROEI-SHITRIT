from argparse import ArgumentError


def piece_of_cake(prices,optionals=None,**quantities):
    """
      Calculates the total price of ingredients for a recipe based on their quantities and prices.

      Args:
          prices (dict): A dictionary with ingredient names as keys and their price per 100 grams as values.
          optionals (list, optional): A list of ingredients to exclude from the calculation. Defaults to None.
          **quantities (dict): The quantities of each ingredient in grams.

      Returns:
          float: The total price for the ingredients used in the recipe.

      Example:
          #>>> get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100)
          44.0

          #>>> get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)
          54.0
      """
    sum=0
    try:
     if len(prices)==0:
         return 0
     for key,value in prices.items():
         if optionals is not None and key in optionals:
             continue

         if key in quantities:
          sum+=(quantities[key]/100)*value

     return sum

    except TypeError:
        print('TypeError')
        return
    except ArgumentError:
        print('ArgumentError')
        return

if __name__ == '__main__':
   get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100)
   get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300)

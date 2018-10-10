#import codecademylib
import pandas as pd

inventory = pd.read_csv('inventory.csv')
print(inventory.head(10))

staten_island = inventory.loc[:10]
#creates a smaller dataframe composed only of the first 10 entries
product_request = staten_island.product_description
#creates a series (column of data) that is just the descriptions from the smaller staten island dataframe

seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
#selects all rows that tell what types of seeds are available at the Brooklyn location

inventory['in_stock'] = inventory.quantity.apply(lambda x: True if x > 0 else False)
#creates a new column based on the values stored in the quantity column

inventory['total_value'] = inventory.quantity * inventory.price
#calculates the total value of the current inventory

combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)
#a lambda function that combines and formats the information in two rows to create complete product descriptions

full_description = inventory.apply(combine_lambda, axis = 1)
#uses the lambda function to add a new column with the current value of the inventory

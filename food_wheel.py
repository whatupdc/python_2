import pandas as pd
from matplotlib import pyplot as plt

restaurants = pd.read_csv('restaurants.csv')
print (restaurants.head())

#counts the number of unique types of cuisine in the restaurant dataframe
cuisine_options_count = restaurants.cuisine.nunique()
#counts the number of restaurants of each type of cuisine
cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()

#contains the values of the column cuisine from cuisine_counts
cuisines = cuisine_counts.cuisine.values
#contains the number of restaurants of each cuisine
counts = cuisine_counts.name.values
#creates a pie chart of the types of cuisines by percentage
#the chart is labeled, titled, and flattened
plt.pie(counts, autopct = '%d%%', labels = cuisines)
plt.title('FoodWheel')
plt.axis('equal')
plt.show()

orders = pd.read_csv('orders.csv')
print (orders.head())
#adds a column that shows the month of the orders
#the .split() function splits a string on a character
#the brackets after the split function return the value in the index position of the resulting split list
orders['month'] = orders.date.apply(lambda x: x.split('-')[0])
print (orders.head())

#gets the average price of the orders in each month
avg_order = orders.groupby('month').price.mean().reset_index()
#gets the standard deviation for the average price of orders in each month
std_order = orders.groupby('month').price.std().reset_index()

#creating an axis on which to plot a bar graph
ax = plt.subplot()

bar_heights = avg_order.price
bar_errors = std_order.price

#creates a bar graph
plt.bar(range(len(bar_heights)), bar_heights, yerr = bar_errors, capsize = 5)
ax.set_xticks(range(len(bar_heights)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.ylabel('Average Order Price')
plt.title('Order Amount over Time')
plt.show()

#creates a histogram of number of customers by  amount spent
customer_amount = orders.groupby('customer_id').price.sum().reset_index()
print (customer_amount.head())

plt.hist(customer_amount.price.values, range = (0,200), bins = 40)
plt.xlabel('Total Spent')
plt.ylabel('Number of Customers')
plt.title('Customer Types by Amount Spent')
plt.show()

"""_summary_
Growing a List: Plus (+)
When we want to add multiple items to a list, we can use + to combine two lists (this is also known as concatenation).

Below, we have a list of items sold at a bakery called items_sold:

items_sold = ["cake", "cookie", "bread"]
Suppose the bakery wants to start selling "biscuit" and "tart":

items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)
Would output:

['cake', 'cookie', 'bread', 'biscuit', 'tart']
In this example, we created a new variable, items_sold_new, which contained both the original items sold, and the new items. We can inspect the original items_sold and see that it did not change:

print(items_sold)
Would output:

['cake', 'cookie', 'bread']
We can only use + with other lists. If we type in this code:

my_list = [1, 2, 3]
my_list + 4
we will get the following error:

TypeError: can only concatenate list (not "int") to list
If we want to add a single element using +, we have to put it into a list with brackets ([]):

my_list + [4]
Let’s use + to practice combining two lists!

Instructions
1.
Jiho is updating a list of orders. He just received orders for "lilac" and "iris".

Create a list called new_orders that contains our new orders.

Checkpoint 2 Passed

Stuck? Get a hint
2.
Use + to create a new list called orders_combined that combines orders with new_orders.

Checkpoint 3 Passed

Stuck? Get a hint
3.
Remove the # and whitespace in front of the list broken_prices. If you run this code, you’ll get an error:

TypeError: can only concatenate list (not "int") to list
Fix the command by inserting brackets ([ and ]) so that it will run without errors.
"""

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:

new_orders = ["lilac", "iris"]
print(new_orders)

broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)

orders_combined = orders + new_orders
print(orders)
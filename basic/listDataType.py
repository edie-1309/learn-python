# list
coffees = ['Espresso', 'Latte', 'Cappuccino']
print(coffees)
# print(coffees[0])

# add item
print("## Add item")
coffees.append('Mocha')
print(coffees)
# insert item specified index
coffees.insert(1, 'Macchiato')
print(coffees)

# remove item
print("## Remove item")
coffees.remove('Espresso')
print(coffees)
# remove item specified index
coffees.pop(2)
# coffees.pop()  # remove last item
print(coffees)

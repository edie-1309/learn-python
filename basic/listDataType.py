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

# looping
# for looping
# 1
print("## Looping through items")
for coffee in coffees:
    print(coffee)
# 2
print("## Looping with index")
for i in range(len(coffees)):
    print(f"{i+1}. {coffees[i]}")
# laptop = ['acer', 'asus', 'lenovo']
# for index in range(len(laptop)):
# 	print(f"{index+1}. {laptop[index]}")
# 3
print("## Shorthand for looping")
[print(x) for x in coffees]

# while looping
laptop = ['acer', 'asus', 'lenovo']
i = 0
while i < len(laptop):
    print(f"{i+1}. {laptop[i]}")
    i = i + 1
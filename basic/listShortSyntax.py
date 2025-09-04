switchs = ['huano red', 'ktt blue', 'cherry red', 'gateron yellow', 'huano black', 'ktt white', 'huano blue', 'gateron blue']

# basic
# red_switchs = []
# for switch in switchs:
#     if 'red' in switch:
#         red_switchs.append(switch)

# with list comprehension
red_switchs = [switch for switch in switchs if 'red' in switch]
blue_switchs = [switch for switch in switchs if 'blue' in switch]

# print(red_switchs)
print('Red switches:', red_switchs)
print('Blue switches:', blue_switchs)

# while loop
# index = 0
# print('Red switches:')
# while index < len(red_switchs):
#     print(f'{index+1}. {red_switchs[index]}')
#     index += 1

# for loop
# print('Red switches:')
# for index in range(len(red_switchs)):
#     print(f'{index+1}. {red_switchs[index]}')


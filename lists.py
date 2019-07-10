fruit_list = ['apple', 'orange', 'peach', 'pear', 'plum']
print(fruit_list)
print(fruit_list[1])

fruit_list.append('strawberry')
print(fruit_list)

veg_list = ['tomato', 'cucumber']
fruit_veg_list = fruit_list + veg_list
print(fruit_veg_list)


for fruit in fruit_veg_list:
    if fruit in fruit_list:
        print(fruit, ": this is a fruit")
    else:
        print(fruit, ": this is not a fruit")

print('\nLooping for pear\n')

for fruit in fruit_list:
    print(fruit)
    if fruit == 'pear':
        print('BREAKING')
        break

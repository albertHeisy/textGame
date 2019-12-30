def pretty_print_unordered(to_print):
    for i, value in enumerate(to_print,1):
        print('{}.{}'.format(str(i),str(value))) # str() to force item to a string / in print it could throw err if non-str encountered




# Enter your three favourite food in list (inventory)
fv_food =[]
more_items = True
while more_items:
    user_input = input('Enter something you like: ')
    if user_input == '':
        more_items = False
    else:
        fv_food.append(user_input)

print('Here are all the things you like!')
pretty_print_unordered(fv_food)


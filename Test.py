# print middle item in the list

planets = ['Mercury', 'Venus', 'Earth', 'Sun', 'Pluton']
print('Middle: ',planets[int(len(planets)/2)])

# Tuples

def get_date():
    return (10,22,2015)

month, day, year = get_date()
print(month)

date = get_date()
print(date)

month, date = get_date()
print(month)

print('test from cli')

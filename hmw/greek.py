## Use % to print every third word in the list

list = ['alpha','beta','gamma','delta','epsilon','zeta','eta']

for i, letter in enumerate(list,1):
    if i % 3 == 0:
        print(letter)
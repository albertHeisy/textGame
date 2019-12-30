def kosa(a,b):
    return a+b

def main():
    sum = 0
    while True:
        try:
            a = float(input('Enter a: '))
            b = float(input('Enter b: '))
            if a == 0 and b == 0:
                break
            print('Sum of {} and {} is {}'.format(a, b, kosa(a, b)))
            sum += kosa(a,b)
            print('Sum of sums: ',sum)
        except:
            print('You didn\'t enter a number.')
            


main()

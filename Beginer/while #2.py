min = None
max = None

while True:
    inp = input('Enter the number: ')
    if inp == 'done':
        break
    try:
        num = float(inp)
    except:
        print('Invalid data')
        continue
    if min is None and max is None:
        min = num
        max = num
    elif num < min:
        min = num
    elif num > max:
        max = num

def done(max, min):
    print('Maximum is ', max)
    print('Minimum is ', min)

done(max, min)
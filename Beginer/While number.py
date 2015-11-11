largest = None
smallest = None

def done(largest, smallest):
    print('Maximum is', int(largest))
    print('Minimum is', int(smallest))

while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    try:
        num = float(inp)
    except:
        print('Invalid data')
        continue
    if smallest is None and largest is None:
        smallest = num
        largest = num
    elif num > largest:
        largest = num
    elif num < smallest:
        smallest = num

done(largest, smallest)







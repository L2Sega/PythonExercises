ran = float(input())

if ran >= 0.0 and ran <= 1.0:
    if ran >= 0.9:
        print('A')
    elif ran >= 0.8:
        print('B')
    elif ran >= 0.7:
        print('C')
    elif ran >= 0.6:
        print('D')
    else:
        print('F')
else:
    print('Error message')
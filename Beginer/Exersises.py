try:
    hrs = float(input())
    rate = float(input())
    extra = hrs - 40.0

except:
    print('Error, please enter numeric input')
    quit()

# print(hrs, rate)
if hrs <= 40.0:
    pay = hrs * rate
else:
    pay = (40 * rate) + (extra * (rate * 1.5))
print(pay)
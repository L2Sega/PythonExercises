def computepay(hours, rate):
    extra = hours - 40
    pay = (40 * rate) + (extra * (rate * 1.5))
    return pay

hours = float(input())
rate = float(input())

print(computepay(hours, rate))
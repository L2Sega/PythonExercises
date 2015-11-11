def computepay(h,r):
    extra = h - 40
    if h == 40:
        pay = h * r
    else:
        pay = (40 * r) + (extra * (r * 1.5))
    return pay

h = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))

print("Pay", computepay(h, r))

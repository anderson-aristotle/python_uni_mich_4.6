def computepay(h,r):
    if h > 40:
        return (h-40)*r*1.5 + 40*r
    else:
        return h*r

hrs = input("Enter Hours:")
h = float(hrs)
rt = input("Enter Rate:")
r = float(rt)

p = computepay(h,r)
print("Pay",p)
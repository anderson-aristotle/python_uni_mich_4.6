def computepay(h,r):
    if h > 40:
        return (h-40)*r*1.5 + 40*r
    else:
        return h*r
    return 42.37

hrs = input("Enter Hours:")
p = computepay(10,20)
print("Pay",p)
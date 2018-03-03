hrs = input('Hours Worked: ')
rates = input('Rate: ')
h = float(hrs)
r = float(rates)
def computepay(h, r):
    if h <= 40:
        return h * r
    else:
        return (40 * r) + ((h - 40) * r * 1.5)

p = computepay(h, r)
print(p)

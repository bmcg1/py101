hrs = input('Enter Hours:')
rt = input('Enter hourly pay:')
h = float(hrs)
r = float(rt)
a = 1
if h <= 40:
    a = h * r
elif h > 40:
    a = (40 * r) + ((h - 40) * r * 1.5) 
print(a)

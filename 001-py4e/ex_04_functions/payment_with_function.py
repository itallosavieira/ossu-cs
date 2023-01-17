regular_hours = 40

def computepay(h, r):
    if h > regular_hours:
        extra_hours = h % regular_hours
        bonus_rate = r * 1.5
        pay = (regular_hours * r) + (extra_hours * bonus_rate)
        return pay
    else:
        pay = hours * rate
        return pay

hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

p = computepay(hours, rate)
print("Pay", p)
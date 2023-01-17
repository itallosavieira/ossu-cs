regular_hours = 40
hours = float(input('Entern hours: '))
rate = float(input('Entern rate: '))


if hours > regular_hours:
    extra_hours = hours % regular_hours
    bonus_rate = rate * 1.5
    pay = (regular_hours * rate) + (extra_hours * bonus_rate)

else:
    pay = hours * rate

print(round(pay, 2))
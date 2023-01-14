try:
    hours = float(input('Entern hours: '))
    rate = float(input('Entern rate: '))
    bonus_rate = rate * 1.5

    if hours > 40:
        pay = round(hours * bonus_rate, 2)
    else:
        pay = round(hours * rate, 2)

    print(pay)
    
except:
    print('Error, please enter numeric input')


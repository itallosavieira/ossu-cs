total = 0
count = 0 
average = 0
inputed_value = None

while True :
    inputed_value = input('Enter a number: ')

    if inputed_value == 'done' :
            break

    try :
        total = total + int(inputed_value)
        count = count + 1
    except :
        print('bad data')

if count or total :
    average = total / count

print(total, count, average)
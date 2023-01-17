smallest = None
biggest = None
inputed_value = None

while True :
    inputed_value = input('Enter a number: ')

    if inputed_value == 'done' :
            break

    try :
        if smallest == None or int(inputed_value) < smallest :
            smallest = int(inputed_value)
        
        if biggest == None or int(inputed_value) > biggest :
            biggest = int(inputed_value)

    except :
        print('Invalid input')

print('Maximum is', biggest)
print('Minimum is', smallest)
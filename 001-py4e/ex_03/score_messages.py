try:
    score = float(input('Enter Score: '))

    if (score <= 1.0):
        if (score >= 0.90):
            print('A')
        elif (score >= 0.80 ):
            print('B')
        elif (score >= 0.70):
            print('C')
        elif (score >= 0.6 ):
            print('D')
        elif (score < 0.6):
            print('F')
        else:
            print('Bad score')

except:
    print('Bad score')
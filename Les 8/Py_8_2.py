

while True:
    invoerString = input('Geef een string van vier letters:')
    lengteString = len(invoerString)
    print(invoerString, 'heeft', str(lengteString), 'letters')

    if lengteString == 4:
        print('Inlezen van correcte string:', invoerString, 'is geslaagd')
        break
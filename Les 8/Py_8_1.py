cijferLijst = []

while True:
    cijferInvoer = eval(input('Geef een getal:'))
    cijferLijst.append(cijferInvoer)

    if cijferInvoer == 0:
        items = len(cijferLijst)
        totalSom = sum(cijferLijst)
        break



print('Er zijn', str(items - 1), 'getallen ingevoerd, de som is:', str(totalSom))
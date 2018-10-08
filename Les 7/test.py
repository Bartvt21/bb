invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
emptyList = []
eindWaarde = []


def waarde(invoerWaarde):
    'Haalt het gemiddelde, totale waarde, kleinste getal, gemiddelde en het grootste getal uit de lijst: invoer en print deze.'

    getallenLijst = invoerWaarde.split('-')

    aantalGetallen = int(0)

    for i in getallenLijst:
        aantalGetallen += 1
        emptyList.append(int(i))
        emptyList.sort()


    gemiddelde = sum(emptyList) / aantalGetallen
    somwaarde = sum(emptyList)
    minWaarde = min(emptyList)
    maxWaarde = max(emptyList)


    print('Gesorteerde list van ints:', emptyList, '\nGrootste getal', maxWaarde, 'en kleinste getal:', minWaarde, '\nAantal getallen:', aantalGetallen, 'en som van de getallen:', somwaarde,'gemiddelde is:', gemiddelde )


print(waarde(invoer))

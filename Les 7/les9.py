

invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
emptyList = []
eindWaarde = []

def waarde(invoerWaarde):
    'Haalt het gemiddelde, totale waarde, kleinste getal, gemiddelde en het grootste getal uit de lijst: invoer en print deze.'

    getallenLijst = invoerWaarde.split('-')

    for i in getallenLijst:
        aantalGetallen = int(i)
        emptyList.append(aantalGetallen)
        emptyList.sort()


    return getallenLijst

print(waarde(invoer))
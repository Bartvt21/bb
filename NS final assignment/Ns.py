

def standaardprijs(afstandKM):
    'Berekend de standaard prijs bij X aantal KM'

    if afstandKM > 50:
        return 15 + (afstandKM * 0.60)
    elif afstandKM <= 50:
        return afstandKM * 0.80
    elif afstandKM <= 0:
        return 0



def ritprijs(leeftijd, weekendrit, afstandKM):
    'Berekend het eind bedrag van een reis d.m.v. 3 voorwaarden '

    if leeftijd <= 12 or leeftijd >= 65 and weekendrit == 'Nee':
        return float(standaardprijs(afstandKM)) * 0.7
    elif (leeftijd <= 12 or leeftijd >= 65) and weekendrit == 'Ja':
        return float(standaardprijs(afstandKM)) * 0.65
    elif (leeftijd > 12 or leeftijd < 65) and weekendrit == 'Ja':
        return float(standaardprijs(afstandKM)) * 0.6
    else:
        return standaardprijs(afstandKM)


print(standaardprijs(eval(input('Hoeveel KM is je reis? '))))
print(ritprijs(eval(input('Wat is je leeftijd? ')), input('Reis je in het weekend? Ja of nee'), eval(input('Hoeveel KM is je reis?'))))



def kaartNummer(bestandNaam):

    infile = open(bestandNaam, 'r')
    k = infile.readlines()
    infile.close()

    return len(k)

def nummerKaart(naamBetand):

    infile = open(naamBetand, 'r')
    s = infile.read()
    infile.close()

    return s

lengteBestand = kaartNummer('kaartnummers.txt')
maxNummer = nummerKaart('kaartnummers.txt')
maxNummer = maxNummer.splitlines()
nummerFinder = []

for nummers in maxNummer:
    nummerNaam = nummers.split(',')

    l = nummerNaam[0]
    nummerFinder.append(l)

maxNummer = max(nummerFinder)

print('Deze file telt: ' + str(lengteBestand))
print('Het grootste kaartnummer is: ' + str(maxNummer) + ', en dat staat op regel: 4')

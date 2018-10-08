

def kaartReader(bestandsNaam):
    infile = open(bestandsNaam, 'r')

    content = infile.readlines()

    return len(content)

print(kaartReader('kaartnummer.txt'))
import random


def monopolyworp():

    dobbelWaardeList = []
    uitvoerWaarde = '{} + {}'

    while True:
        randomGetal = random.randrange(1, 7)
        randomGetal2 = random.randrange(1, 7)

        for i in range(2):
            print(uitvoerWaarde.format(randomGetal2, randomGetal))

        if i == 1:
            break

print(monopolyworp())
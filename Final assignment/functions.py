import time

def hardlopers(bestand):


    infile = open(bestand, 'w')


    while True:
        invoerLoper = input('Je naam...')
        t = time.strftime('%a, %d %B %Y, %H:%M:%S,' + str(invoerLoper))
        infile.write(t)



print(hardlopers('hardlopers.txt'))
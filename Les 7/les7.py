



def convert(celsius):
    fahrenHeit = celsius * 1.8 + 32

    return fahrenHeit

def table():

    for i in range(-30, 50, 10):
        fahrenHeit = convert(i)

        print('{0:5} {1:3}'.format(fahrenHeit, i))

    return ''


print('{0:1} {1:1}'.format('F','C'))
print(table())

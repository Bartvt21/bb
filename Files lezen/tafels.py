

studentenCijfers = [[6, 7, 5], [8, 7, 9], [4, 6, 3]]



def gemiddelde_per_student(studentencijfers):

    gemiddeldeUitkomst = ''

    for i in studentencijfers:

        cijferTot = sum(i)
        aantalNummers = len(i)

        gemiddeldeStudent = cijferTot / aantalNummers
        gemiddeldeUitkomst = gemiddeldeUitkomst + 'gemiddelde per student is: ' + str(gemiddeldeStudent) + '\n'

    return gemiddeldeUitkomst

def studentTotalCount(studentencijfers):
    eindcijfer = int()
    studentCount = len(studentencijfers)

    for i in studentencijfers:

        cijferTot = sum(i)
        aantalNummers = len(i)

        gemiddeldeStudent = cijferTot / aantalNummers
        eindcijfer += gemiddeldeStudent

    eindGemiddelde = eindcijfer / studentCount

    return 'Gemiddelde is: ' + str(eindGemiddelde)

print(gemiddelde_per_student(studentenCijfers))
print(studentTotalCount(studentenCijfers))
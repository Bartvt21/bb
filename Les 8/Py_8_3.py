
cijfersStudenten = {

    'Piet': [6, 9, 4, 5, 6, 7, 8, 6,],
    'Jos': [1, 5, 9, 10, 7, 4, 5, 7],
    'Maarten': [9, 7, 5, 6, 10, 2, 1]

}

for name in cijfersStudenten:
    for number in cijfersStudenten[name]:
        if number > 8:
            print(name, 'heeft een:', float(number))

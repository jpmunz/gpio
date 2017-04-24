import csv
import matplotlib.pyplot as pyplot

MAX_DURATION = 120
x = []
y = []
first = True

with open('receiver_result.csv', 'rb') as csvfile:

    reader = csv.reader(csvfile, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for row in reader:
        if first:
            first = False
            continue

        x.append(row[0])
        y.append(row[1])


    pyplot.plot(x, y)
    pyplot.axis([0, MAX_DURATION, -1, 2])
    pyplot.show()

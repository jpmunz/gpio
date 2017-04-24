import csv
from datetime import datetime
import matplotlib.pyplot as pyplot
from GPIOLibrary import GPIOProcessor
import time

GP = GPIOProcessor()

MAX_DURATION = 120
received = [[], []]

try:
    receiverPin = GP.getPin33()
    receiverPin.out()
    start = datetime.now()
    running_time = 0

    while running_time < MAX_DURATION:
        time_delta = datetime.now() - start
        received[0].append(time_delta)
        received[1].append(receiverPin.getValue())
        running_time = time_delta.seconds

    for i in range(len(received[0])):
        received[0][i] = received[0][i].seconds + received[0][i].microseconds/1000000.0


    with open('receiver_result.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['time', 'signal'])
        for i in range(len(received[0])):
            writer.writerow([received[0][i], received[1][i]])

    # No display on dragonboard
    #pyplot.plot(received[0], received[1])
    #pyplot.axis([0, MAX_DURATION, -1, 2])
    #pyplot.show

finally:
    GP.cleanup()

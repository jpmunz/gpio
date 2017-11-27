import csv
from datetime import datetime
import matplotlib.pyplot as pyplot
from GPIOLibrary import GPIOProcessor
import time

GP = GPIOProcessor()

# https://www.youtube.com/watch?v=B86nqDRskVU

DELAY = 0.001

WAVE_SEQUENCE = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]

FULL_STEP_SEQUENCE = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
]


try:
    steps_made = 0

    pins = [
        GP.getPin31(),
        GP.getPin32(),
        GP.getPin33(),
        GP.getPin34(),
    ]

    for p in pins:
        p.out()


    right = GP.getPin27()
    right.input()
    left = GP.getPin26()
    left.input()
    reset = GP.getPin24()
    reset.input()

    sequence = FULL_STEP_SEQUENCE
    i = 0
    direction = 0
    resetting = False

    while True:
        time.sleep(DELAY)

        for p in pins:
            p.low()

        if resetting:
            if steps_made == 0:
                resetting = False
                continue
            elif steps_made < 0:
                direction = 1
            else:
                direction = -1
        else:
            if reset.getValue():
                resetting = True
                continue
            if not (right.getValue() or left.getValue()):
                continue
            elif right.getValue():
                direction = 1
            elif left.getValue():
                direction = -1

        pattern = sequence[i]

        for j, p in enumerate(pins):
            if pattern[j]:
                p.high()

        steps_made += direction

        i = (i + direction) % len(sequence)
finally:
    GP.cleanup()

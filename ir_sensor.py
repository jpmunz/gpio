from GPIOLibrary import GPIOProcessor
import time

GP = GPIOProcessor()

try:
    pin = GP.getPin33()
    pin.input()

    while True:

        timeout = time.time() + 5
        count = 0
        count2 = 0
        while True:
            if  pin.getValue() == 0:
                count += 1
            if  pin.getValue() == 1:
                count2 += 1
            if time.time() > timeout:
                break
        print "saw " + str(count) + " zeros"
        print "saw " + str(count2) + " ones"

finally:
    GP.cleanup()

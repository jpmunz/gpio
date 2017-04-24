from GPIOLibrary import GPIOProcessor
import time

GP = GPIOProcessor()

try:

    receiverPin = GP.getPin33()
    senderPin = GP.getPin34()

    receiverPin.out()
    senderPin.input()


    for i in range(0,10):
        Pin34.high()
        time.sleep(0.5)
        Pin34.low()
        time.sleep(0.5)

finally:
    GP.cleanup()

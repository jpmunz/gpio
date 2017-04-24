from GPIOLibrary import GPIOProcessor
import time

GP = GPIOProcessor()



def blink(amount, delay):
    try:
        pin = GP.getPin(7)
        pin.out()

        for i in range(0,amount):
            pin.high()
            time.sleep(delay)
            pin.low()
            time.sleep(delay)
    finally:
        GP.cleanup()

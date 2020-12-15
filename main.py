import driver
from machine import Pin
import time
from micropython import const

_sleep_seconds = const(5)
_step_speed_in_ms = const(2)  # The larger, the slower RPM.Either FULL_STEP or HALF_STEP

if __name__ == '__main__':
    '''
    IN1 -->  D5:14
    IN2 -->  D6:12
    IN3 -->  D7:13
    IN4 -->  D8:15
    '''
    motor = driver.create(Pin(14, Pin.OUT), Pin(12, Pin.OUT), Pin(13, Pin.OUT), Pin(15, Pin.OUT),
                          delay=_step_speed_in_ms)
    motor.step(100)
    motor.step(100, -1)
    motor.angle(180)
    motor.angle(360, -1)

    while True:
        motor.step(100)
        time.sleep(_sleep_seconds)
        motor.step(100, -1)
        time.sleep(_sleep_seconds)

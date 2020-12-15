import driver
from machine import Pin
import time
from micropython import const

_sleep_seconds = const(300)
_step_speed_in_ms = const(2)  # The larger, the slower RPM.Either FULL_STEP or HALF_STEP
_sweep_steps = const(30)

if __name__ == '__main__':
    '''
    IN1 -->  D8:15
    IN2 -->  D7:13
    IN3 -->  D6:12
    IN4 -->  D5:14
    '''
    motor = driver.create(Pin(15, Pin.OUT), Pin(13, Pin.OUT), Pin(12, Pin.OUT), Pin(14, Pin.OUT),
                          delay=_step_speed_in_ms)

    while True:
        motor.step(_sweep_steps)
        time.sleep(_sleep_seconds)
        motor.step(_sweep_steps, -1)
        time.sleep(_sleep_seconds)

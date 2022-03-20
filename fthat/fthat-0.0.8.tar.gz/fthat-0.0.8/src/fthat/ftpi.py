# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 -- Michael Schaar
# All rights reserved.
#
# License: BSD License
#

import gpiozero
import os

# Set environment variables
#os.environ['GPIOZERO_PIN_FACTORY'] = 'pigpio'
#os.environ['PIGPIO_ADDR'] = 'ft-pi4.local'

INPUT_MODE_SWITCH = 'switch'
_VALID_INPUT_MODES = (INPUT_MODE_SWITCH)

MOTOR_OFF = 'off'
MOTOR_LEFT = 'left'
MOTOR_RIGHT = 'right'
MOTOR_BRAKE = 'brake'

_VALID_MOTOR_DIRECTIONS = (MOTOR_LEFT, MOTOR_RIGHT, MOTOR_BRAKE, MOTOR_OFF)

M1_BIN1 = 5
M1_BIN2 = 6
M1_PWM1 = 13
M2_AIN1 = 23
M2_AIN2 = 22
M2_PWM0 = 18
Mx_STBY = 19

_VALID_MOTOR_OUTPUTS = (M1_BIN1, M1_BIN2, M1_PWM1, M2_AIN1, M2_AIN2, M2_PWM0, Mx_STBY)

M1 = 'M1'
M2 = 'M2'

_VALID_MOTOR_NAMES = (M1, M2)

# ft HAT usage of GPIO pins on the Raspberry Pi
I1 = 12
I2 = 16
I3 = 20
I4 = 21

_VALID_INPUTS = (I1, I2, I3, I4)

I2C_EXT_SDA = 2
I2C_EXT_SCL = 3
I2C_INT_SDA = 0
I2C_INT_SCL = 1

TXD0 = 14
RXD0 = 15

COUNTER_EDGE_NONE = 'none'
COUNTER_EDGE_RISING = 'rising'
COUNTER_EDGE_FALLING = 'falling'
COUNTER_EDGE_ANY = 'any'

_VALID_COUNTER_MODES = (COUNTER_EDGE_NONE, COUNTER_EDGE_RISING,
                        COUNTER_EDGE_FALLING, COUNTER_EDGE_ANY)

OFF = 0
HIGH = 1
LOW = 2

MIN = OFF
MAX = 1.0

class Singleton_meta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton_meta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Ft_Hat_Input(gpiozero.Button):
    def __init__(self, port, *args, **kwargs):
        if port in _VALID_INPUTS:
            try:
                super().__init__(port, *args, **kwargs)
            except gpiozero.GPIOPinInUse:
                self.close()
                super().__init__(port, *args, **kwargs)
            finally:
                self.__port = port
        else:
            raise ValueError('Invalid port number "{0}", use {1}'.format(port, _VALID_INPUTS))
    
    @property
    def port(self):
        return self.__port

class BaseFTTxpiHat(metaclass = Singleton_meta):
    def __init__(self):
        for _ in _VALID_INPUTS:
            self.input_set_mode(_)
#         try:
#             # Default Mx_STBY is off
#             self.Mx_STBY = gpiozero.OutputDevice(Mx_STBY)
#         except gpiozero.GPIOPinInUse:
#             raise gpiozero.GPIOPinInUse
#         #self.M1 = gpiozero.Motor(forward=M1_BIN1, backward=M1_BIN2, enable=M1_PWM1)

    def __enter__(self):
        return self
    
    def __del__(self):
        self.Mx_STBY.close()
         
    def output_set(self, port, mode, pwm=None):
        pass

    def input_get(self, port):
        pass

    def input_set_mode(self, port, *args, **kwargs):
        if port == I1:
            self.I1 = Ft_Hat_Input(port, *args, **kwargs)
        elif port == I2:
            self.I2 = Ft_Hat_Input(port, *args, **kwargs)
        elif port == I3:
            self.I3 = Ft_Hat_Input(port, *args, **kwargs)
        elif port == I4:
            self.I4 = Ft_Hat_Input(port, *args, **kwargs)
        else:
            raise ValueError('Invalid port number "{0}", use {1}'.format(port, _VALID_INPUTS))

    def counter_set_mode(self, port, mode):
        pass

    def counter_get(self, port):
        pass

    def counter_clear(self, port):
        pass

    def counter_get_state(self, port):
        pass

    def ultrasonic_get(self):
        pass

    def ultrasonic_enable(self, enable):
        pass

    def motor_set(self, motor, mode, pwm=MAX):
        pass
#         """\
#         Sets the provided motor port into the given state.
# 
#         :param motor: Port name, i.e. 'M1'. The port name is case-insensitive.
#         :param mode: 'off',  'left', 'right', or 'brake' (case-insensitive), see constants
#                      ``ftpi.MOTOR_OFF``, ``ftpi.MOTOR_LEFT``, ``ftpi.MOTOR_RIGHT``,
#                      and ``ftpi.MOTOR_BRAKE``.
#         :param pwm: Pulse-width modulation value. If ``None`` the max. PWM value will be used.
#         """
#         if mode.lower() not in _VALID_MOTOR_DIRECTIONS:
#             raise ValueError('Invalid motor mode "{0}", use {1}'.format(mode, _VALID_MOTOR_DIRECTIONS))
#         if motor.lower() not in _VALID_MOTOR_NAMES:
#             raise ValueError('Invalid motor mode "{0}", use {1}'.format(mode, _VALID_MOTOR_NAMES))
#         if motor.lower() == M1:
#             self.M1 = gpiozero.Motor(M1_BIN1, M1_BIN2, enable=Mx_STBY)
#         else:
#             self.M2 = gpiozero.Motor(M2_AIN1, M2_AIN2, enable=Mx_STBY)

    def motor_counter(self, port, mode, pwm, counter):
        pass

    def motor_counter_active(self, port):
        pass

    def motor_counter_set_break(self, port, enable):
        pass

    def led_set(self, enable):
        pass

#!/usr/bin/python

import usb.core
import usb.util
import sys
import getopt
import time


class Luxafor:
    def __init__(self):
        # 66    blauw
        # 67    zeeblauw
        # 71    groen
        # 77    purple
        # 82    rood
        # 87    wit
        # 89    geel
        # 79    no-color
        self.colors = {'blue': 66,
                       'seablue': 67,
                       'green': 71,
                       'purple': 77,
                       'red': 82,
                       'white': 87,
                       'yellow': 89,
                       'no-color': 79
                       }
        # find our device
        self.dev = usb.core.find(idVendor=0x04d8, idProduct=0xf372)

        # was it found?
        if self.dev is None:
            raise ValueError('Device not found')

        # Linux kernel sets up a device driver for USB device, which you have
        # to detach. Otherwise trying to interact with the device gives a
        # 'Resource Busy' error.
        try:
            self.dev.detach_kernel_driver(0)
        except Exception as e:
            pass

        self.dev.set_configuration()
        self.dev.write(1, [0, 0])

    def flash(self, color, speed=0.5, loops=2):
        """
        flashes the light in `color` at an interval defined by the `speed` for `loop` times

        color -- str: Which color should the light be
        speed --  int : how lang should the led be on/off: default 0.5
        loop   -- int: how many times should it blink: default 2
        """
        loop = 0

        for _ in range(loops):
            # print(dev)
            self.dev.write(1, [0, 79])
            time.sleep(speed)
            self.dev.write(1, [0,  self.colors[color]])
            time.sleep(speed)

            self.dev.write(1, [0, 79])
        return;

    def off(self):
        '''
            Turn the led off
        '''
        self.dev.write(1, [0, 79])
        return

    def set_clr_by_name(self,color):
        '''
            Show the color (by string)
        '''
        self.dev.write(1, [0, self.colors[color]])
        return;

    def set_clr_by_number(self, color):
        '''
            Show the color (by int value)
        '''
        self.dev.write(1, [0, color])
        return;
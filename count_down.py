#!/usr/bin/env python
from src.lux_cls  import Luxafor
from datetime import datetime as dt, timedelta as td
import time

class Alarm:
    def __init__(self, color, time, blink=True):
        self.color = color
        self.blink = blink
        self.time = time


class Timer:
    def __init__(self,total=60,alarms=[]):
        self.lux = Luxafor()
        self.total=total
        self.alarms = alarms
        if len(alarms) == 0:
            self.alarms.append(Alarm('yellow',10,True))
            self.alarms.append(Alarm('red',5,True))
        self.reset()

    def reset(self):
        self.starttime = dt.now()
        self.endtime = self.starttime + td(seconds=self.total)
        self.state = 0

    def start(self):
        now = dt.now()
        self.lux.set_clr_by_name('green')
        while(now <=  self.endtime ):
            now = dt.now()
            for i in range(0,len(self.alarms)):
                alarm = self.alarms[i]
                if now >= (self.endtime - td(seconds=alarm.time)) and self.state <= i+1:
                    self.state = i+1
                    if alarm.blink:
                        self.lux.flash(alarm.color)
                    else:
                        self.lux.set_clr_by_name(alarm.color)
                        time.sleep(.5)
                elif self.state == 0:
                    time.sleep(.5)
        self.lux.set_clr_by_name('red')

    def stop(self):
        self.lux.set_clr_by_name('no-color')

if __name__ == "__main__":
    alerts=[]
    alerts.append(Alarm('blue', 90, False))
    alerts.append(Alarm('green', 60, False))
    alerts.append(Alarm('yellow', 30, False))
    alerts.append(Alarm('yellow', 15, True))
    alerts.append(Alarm('red', 5, True))
    timer = Timer(90, alerts)
    try:
        action = "A"
        while action is "A" or action is "a":
            timer.reset()
            timer.start()
            action = input("[A]gain or [S]top: ")
    finally:
        timer.stop()
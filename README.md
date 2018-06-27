# Introduction
## How it got started
Someone donated a luxafor flag to play around with.

## Steps
First thing to do was find out how to communicate with it on a linux box.  
For usb communication PyUSB is used.  
Next a small program was written which tried all possible values between 0 and 255 to find out which colors the lux supported.  


# How to get the usb device connect/accessible for ordinary users
'''
$> sud su -  
$> cd /etc/udev/rules.d/  
$>  vim 99-hidraw-permissions.rules  

  
add:  
SUBSYSTEM=="usb", ATTRS{idVendor}=="04d8", ATTRS{idProduct}=="f372", MODE="0666"
'''

# luxafor flag
Supported colors:  
'blue': 66  
'seablue': 67  
'green': 71  
'purple': 77  
'red': 82  
'white': 87  
'yellow': 89  
'no-color': 79  
  
# lux_cls
Main lux class.  It instantiates the device and writes the necesarry instructions.  
  
supports:  
Flashing and continues light.  
Turn it of again.  

# Countdown
The count down program takes a duration and list of alerts.

It determines the time now and runs for the number of seconds request. 

e.g.  
```python
alerts.append(Alarm('blue', 90, False))
alerts.append(Alarm('green', 60, False))
alerts.append(Alarm('yellow', 30, False))
alerts.append(Alarm('yellow', 15, True))
alerts.append(Alarm('red', 5, True))
timer = Timer(90, alerts)
```
creates a timer which runs for 90 seconds.  
it starts continues blue  
after 30 (end-60) seconds it shows continues green  
after 60 (end-30) seconds it shows continues yellow
after 75 (end-15) seconds it flashes yellow
after 85 (end-5)  seconds it flashes red
End it finishes by showing continues red.
  
# gui-lux
Is a simple user interface with buttons, which makes the lux show a particular color.


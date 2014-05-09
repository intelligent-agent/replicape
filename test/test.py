#!/usr/bin/python

import time
import os, os.path
import sys

sys.stdout = sys.stderr

TTY_NORET="/dev/pts/7"
TTY_RET="/dev/pts/5"

def wait_for_pipes():
    while not os.path.exists(TTY_NORET):
        time.sleep(0.1)
    while not os.path.exists(TTY_RET):
        time.sleep(0.1)

def send(msg):
    f = os.open(TTY_NORET, os.O_RDWR)
    os.write(f, msg+"\n")
    os.close(f)

def send_receive(msg):
    f = os.open(TTY_RET, os.O_RDWR)
    os.write(f, msg+"\n")
    ret = readline_custom(f)
    os.close(f)
    return ret
    
def readline_custom(f):
    message = ""
    while True:
        cur_char = os.read(f, 1)
        if (cur_char == '\n' or cur_char == ""):
            return message;
        message = message + cur_char

def write_eeprom():    
    print "Writing EEPROM"
    os.system("cat /usr/src/Replicape/test/Replicape_0A4A.eeprom > /sys/bus/i2c/drivers/at24/1-0054/eeprom")
    print "Done"

def test_steppers():
    print "testing steppers"
    send("G91")
    send("G1 X1 F30")
    send("G1 X-1 F30")
    send("G1 Y1 F30")
    send("G1 Y-1 F30")
    send("G1 Z1 F30")
    send("G1 Z-1 F30")
    send("G1 E1 F30")
    send("G1 E-1 F30")
    send("G1 H1 F30")
    send("G1 H-1 F30")
    print "Done"

def enable_mosfets():
    print "enabling all mosfets"
    send("M140 S200")
    send("M104 P0 S200")
    send("M104 P1 S200")
    send("M106 P0 S255")
    send("M106 P1 S255")
    send("M106 P2 S255")
    print "Done"

def test_thermistors():
    print "testing thermistors"
    print send_receive("M105")
    print "Done"

def disable_mosfet(val):
    if val == "X1":
        send("M106 P0 S0")
    if val == "Y1":
        send("M106 P1 S0")
    if val == "Z1":
        send("M106 P2 S0")
    if val == "X2":
        send("M104 P0 S0")
    if val == "Y2":
        send("M140 S0")
    if val == "Z2":
        send("M104 P1 S0")

def test_endstops():
    print "testing endstops. Push each of the switches"
    ok = { "Y2": 0, "Y1": 0, "X2": 0, "X1": 0, "Z1": 0, "Z2": 0 }
    while True:
        ret = send_receive("M119")
        for endstop in ok:
            if not ok[endstop]:
                pos = ret.find(endstop)
                val = ret[pos+4]
                if int(val):
                    print endstop+" is OK"
                    ok[endstop] = 1
                    disable_mosfet(endstop)
                    if not 0 in ok.values():
                        print "All OK"
                        return



wait_for_pipes()
write_eeprom()
enable_mosfets()
test_endstops()
test_steppers()
test_thermistors()


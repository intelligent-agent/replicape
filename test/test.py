#!/usr/bin/python

import time
import os, os.path
import sys

sys.stdout = sys.stderr

TTY_NORET="/dev/testing_1"
TTY_RET="/dev/toggle_1"

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
    os.system("cat /usr/src/replicape/test/Replicape_0A4A.eeprom > /sys/bus/i2c/drivers/at24/1-0054/eeprom")
    print "Done"


def test_steppers():
    print "testing steppers"
    send("G91")
    send_receive("M350 X0 Y0 Z0 E0 H0") # Microstepping
    send("G1 X4 Y4 Z4 E4 H4 F100")

    send_receive("M350 X1 Y1 Z1 E1 H1")
    send("G1 X10 Y10 Z10 E10 H10 F1000")

    send_receive("M350 X2 Y2 Z2 E2 H2")
    send("G1 X10 Y10 Z10 E10 H10 F1000")

    send_receive("M350 X3 Y3 Z3 E3 H3")
    send("G1 X10 Y10 Z10 E10 H10 F1000")

    send_receive("M350 X4 Y4 Z4 E4 H4")
    send("G1 X10 Y10 Z10 E10 H10 F1000")

    send_receive("M350 X5 Y5 Z5 E5 H5")
    send("G1 X10 Y10 Z10 E10 H10 F1000")

    send_receive("M350 X0 Y0 Z0 E0 H0")
    send("G1 X-4 Y-4 Z-4 E-4 H-4 F100")

    send_receive("M400") # Wait until done

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
    ret = send_receive("M105")
    pos = ret.find("T:")
    pos2 = ret.find("B:")
    t0 = float(ret[pos+2:pos2])
    pos = ret.find("B:")
    pos2 = ret.find("T1:")
    t1 = float(ret[pos+2:pos2])
    pos = ret.find("T1:")
    pos2 = ret.find("\n")
    t2 = float(ret[pos+3:])
    
    ok = {"t0": 0, "t1": 0, "t2": 0}
    if abs(t0-100) < 4:
        ok["t0"] = 1
    if abs(t1-100) < 4:
        ok["t1"] = 1
    if abs(t2-100) < 4:
        ok["t2"] = 1          

    if not 0 in ok.values(): # All OK
        enable_mosfets()    
    else: 
        print "Error in thermistors. Returned '"+ret+"'"
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
time.sleep(1)
test_steppers()
test_thermistors()

print "testing done!"
   


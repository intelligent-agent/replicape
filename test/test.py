#!/usr/bin/python

import time
import os, os.path
import sys
import re

#sys.stdout = sys.stderr
sys.stdout = open('/dev/tty1', 'w')

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

def send_receive(msg, match = None):
    f = os.open(TTY_RET, os.O_RDWR)
    os.write(f, msg+"\n")
    ret = readline_custom(f)
    if match is not None: 
        while ret != match:
            ret = readline_custom(f)
            #print "ret: "+ret
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
    os.system("cat /usr/src/replicape/test/Replicape_0B3A.eeprom > /sys/bus/i2c/devices/2-0054/at24-1/nvmem")
    print "Done"


def test_steppers():
    print "testing steppers"
    send_receive("G91")
    for i in range(9):
        send_receive("M350 X{} Y{} Z{} E{} H{}".format(i, i, i, i, i)) # Microstepping
        send_receive("G1 X10 Y10 Z10 E10 H10 F6000")
        send_receive("G1 X-10 Y-10 Z-10 E-10 H-10 F6000") 
        send_receive("M400") # Wait until done
    send_receive("M18")
    print "Done"

def enable_mosfets():
    print "enabling all mosfets"
    send_receive("M140 S200")
    send_receive("M104 P0 S200")
    send_receive("M104 P1 S200")
    send_receive("M106 P0 S255")
    send_receive("M106 P1 S255")
    send_receive("M106 P2 S255")
    send_receive("M106 P3 S255")
    print "Done"

def test_thermistors():
    print "testing thermistors"

    ret = send_receive("M105")

    temps = re.findall("[0|1|B]\:(\d+)", ret)
    temps = [abs(26-float(t)) for t in temps]

    ok = {"t0": 0, "t1": 0, "t2": 0}
    if temps[0] < 4:
        ok["t0"] = 1
    if temps[1] < 4:
        ok["t1"] = 1
    if temps[2] < 4:
        ok["t2"] = 1          

    if not 0 in ok.values(): # All OK
        disable_mosfets()    
    else: 
        print "Error in thermistors. Returned '"+ret+"'"
    print "Done"

def disable_mosfets():
    print "Disabing mosfets"
    send_receive("M106 P0 S0")
    send_receive("M106 P1 S0")
    send_receive("M106 P2 S0")
    send_receive("M106 P3 S0")
    send_receive("M104 P0 S0")
    send_receive("M140 S0")
    send_receive("M104 P1 S0")

def home_all():
    print "Homing all"
    send_receive("M350 X0 Y0 Z0 E0 H0")
    send_receive("G28", "Homing done.")
    print "Homing done"

wait_for_pipes()
write_eeprom()
enable_mosfets()
home_all()
test_steppers()
test_thermistors()

print "testing done!"
   


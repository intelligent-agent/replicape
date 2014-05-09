# Makefile for flashing the eeprom of the Replicape

all:
	#node ./eeprom.js -w replicape_00A3.json
	node ./eeprom.js -w replicape_0A4A.json

install:
	cat Replicape.eeprom > /sys/bus/i2c/drivers/at24/1-0054/eeprom


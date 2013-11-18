

RPATH=/opt/Replicape
REMOTE=root@10.24.2.90
#REMOTE=root@192.168.7.2
DPATH=Dist/dist_`date +"%y_%m_%d"`/Replicape
DNAME=Replicape_rev_A4-`date +"%y_%m_%d"`.tgz

.PHONY : eeprom dt dist

eeprom:
	scp eeprom/replicape_*.json eeprom/bone.js eeprom/eeprom.js eeprom/Makefile $(REMOTE):$(RPATH)/eeprom
	ssh $(REMOTE) 'cd /opt/Replicape/eeprom; make'

dt: 
	scp Device_tree/* $(REMOTE):$(RPATH)/device_tree/

dist: 
	mkdir -p $(DPATH)
	mkdir -p $(DPATH)/device_tree
	mkdir -p $(DPATH)/eeprom
	cp Dist/Makefile $(DPATH)/
	cp Device_tree/* $(DPATH)/device_tree/
	cp eeprom/eeprom.js eeprom/bone.js eeprom/replicape_*.json eeprom/Makefile $(DPATH)/eeprom/
	cd $(DPATH)/../ && tar -cvzpf ../$(DNAME) . && cd ..
	scp Dist/$(DNAME) replicape@scp.domeneshop.no:www/distros/
	

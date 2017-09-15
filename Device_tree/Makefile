# Compile the overlay and copy the files to the right dirs



all:
	dtc -O dtb -o BB-BONE-REPLICAP-00A1.dtbo -b 0 -@ 3.12/BB-BONE-REPLICAP-00A1.dts
	dtc -O dtb -o BB-BONE-REPLICAP-00A2.dtbo -b 0 -@ 3.12/BB-BONE-REPLICAP-00A2.dts
	dtc -O dtb -o BB-BONE-REPLICAP-00A3.dtbo -b 0 -@ 3.12/BB-BONE-REPLICAP-00A3.dts
	dtc -O dtb -o BB-BONE-REPLICAP-00A4.dtbo -b 0 -@ 3.12/BB-BONE-REPLICAP-00A4.dts
	dtc -O dtb -o BB-BONE-REPLICAP-0A4A.dtbo -b 0 -@ 3.12/BB-BONE-REPLICAP-0A4A.dts
	dtc -O dtb -o BB-BONE-REACH-00A0.dtbo -b 0 -@ 3.12/BB-BONE-REACH-00A0.dts

install:
	cp BB-BONE-REPLICAP* /lib/firmware/

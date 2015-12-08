    :::python
     _____           __
    | ___ \         | (_)
    | |_/ /___ _ __ | |_  ___ __ _ _ __   ___
    |    // _ \  _ \| | |/ __/ _  |  _ \ / _ \
    | |\ \  __/ |_) | | | (_| (_| | |_) |  __/
    \_| \_\___| .__/|_|_|\___\__,_| .__/ \___|
             | |                 | |
             |_|                 |_|

Replicape is a 3D printer cape for BeagleBone.  

### Features: ###

* 5 stepper motors (Trinamic TMC2100) (X, Y, Z, E, H)  
* 3 high power MOSFETs (PWM controlled) for 2 extruders and 1 HPB.  (12..24V)  
* 4 medium power MOSFETs (PWM controlled) for up to 4 fans/LED strips.  (12V)  
* 3 analog input ports for thermistors. noise-filtered inputs and option for shielding  
* 6 inputs for end stops (X, Y, Z).  
* 1 bus for Dallas 1W temperature sensor for monitoring the cold end. Up to 10 sensors can be added to the bus.  
* 2 servo outputs.  
* 1 inductive sensor input.  
* Programmable current limits on steppers motor drivers (SMD). No need to manually adjust a pot meter.  
* Microstepping individually programmable for each SMD from 1 to 256.  
* All steppers are controlled by the Programmable Realtime Unit (PRU) for hard real time operation.  
* Compatible with [Manga Screen](https://bitbucket.org/intelligentagent/manga-screen)  
* Single 12 to 24V PSU, fans are still 12V.  
* Compatible with BeagleBone and BeagleBone Black (probably also green and blue).  
* Open source hardware and software.  
* Software written in Python for maintainability and hackability.  
  
This is the repository for the hardware, the "firmware" (Redeem) has a [separate repository](https://bitbucket.org/intelligentagent/redeem)

### What is in here? ###

* This repository contains the files needed to reproduce the PCB and continue development.
* The latest revision is B3

### I want one! How much is it, and where can I get it? ###

It's $99 and you can [buy it in the store](http://www.thing-printer.com/product/replicape)

### I want to build my own board. How do I do that? ###

* Download the BOM and order the parts from Digi-key
* Send the GERBER files to a PCB manufacturer
* Get a reflow oven
* Populate the board

### I want a different version of this, who do I talk to? ###

Talk to Elias <elias at iagent dot no> 

### I have a Replicape, how do I wire it? ###
Look at the wiki page: [http://wiki.thing-printer.com](http://wiki.thing-printer.com)

### I want to read about the latest development of this board. Where can I do that? ###
The thing-prnter blog is a good place: [http://www.thing-printer.com/blog/](http://www.thing-printer.com/blog/)

### Who has contributed to this project? ###

* Elias Bakken
* Dirk Eichel
* Stoneshop
* Bent Furevik


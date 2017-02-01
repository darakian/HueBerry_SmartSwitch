hueBerry: Setup instructions for Developers
=============
### *"Bare-metal" install instructions for dev-kit*

[![hueBerry Mess!](https://github.com/fiveseven808/HueBerry_SmartSwitch/blob/dev/hueBerry%20Photos/B%20reel/IMG_20160812_165047.jpg?raw=true)](https://youtu.be/YTvbsL82ZcM?t=1m3s "hueBerry Mess!")



## Getting Started: Updated 1/29/2017
Getting started with the hueBerry from a bare-metal pi is fairly simple. Here, I will attempt to guide you from start to finish! 

**Requirements:**

  * Raspberry Pi (I used a Zero)
  * Adafruit_SSD1306 library
  * pigpio library
  * SSD1306 compatible display (128x64 resolution)
  * Rotary encoder switch thing 
  * Full BOM located [here](https://docs.google.com/spreadsheets/d/18q5wE9IcbJ1D823ktt4ZN7Fp1JHZutR4hCld2env4vI/edit?usp=sharing)

**Do you meet the dev-kit minimum requirements?** Do you have a display, encoder, pi, and network connection? If so, you may continue! Otherwise, go back and get those components. 
	
## Bare-Metal Instructions:

* [Install the latest Raspbian distribution](https://www.raspberrypi.org/documentation/installation/installing-images/)
* Wire up the I2C display and rotary encoder (wiring diagrams coming soon)
* [Install the Adafruit_SSD1306 library](https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black/usage)
```bash
sudo apt-get update
sudo apt-get install build-essential python-dev python-pip
sudo pip install RPi.GPIO
sudo apt-get install python-imaging python-smbus
sudo apt-get install git
git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
cd Adafruit_Python_SSD1306
sudo python setup.py install
```
* [Install and run pigpiod](http://abyz.co.uk/rpi/pigpio/download.html)
```bash
rm master.zip
sudo rm -rf pigpio-master
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make -j4
sudo make install
sudo pigpiod 
```
* You may want to add `sudo pigpiod` to your startup file (I used /etc/rc.local)
* Modify your `/boot/config.txt` file to enable I2c and speed up the bus
```
# Uncomment some or all of these to enable the optional hardware interfaces
dtparam=i2c_arm=on
dtparam=i2c_baudrate=400000
#dtparam=i2s=on
dtparam=spi=off
``` 
* *Optional* Disable GUI (to speed up boot?) and lower GPU mem to 8mb
```
gpu_mem=8
start_x=0
``` 
* *Optional* Overclock your SD card bus to get faster boot speeds
```
dtparam=sd_overclock=100
```
* Clone hueBerry git dev branch then run the main program
```
cd ~
git clone -b dev https://github.com/fiveseven808/HueBerry_SmartSwitch.git
cd HueBerry_SmartSwitch

sudo python hueberry.py
```
* Follow instructions on the screen to pair your hueBerry and bridge
 1. On first run, it should ask you to pair with your Philips hue Bridge.
 1. Follow the onscreen instructions
* Enjoy! 
 * *If the above instructions do not work, please contact the maintainer to correct this accordingly*

 
	
**License:** 

[Creative Commons Attribution-NonCommercial 4.0 International ](https://creativecommons.org/licenses/by-nc/4.0/)  
This is an open source beta program supplied with no guarantee.
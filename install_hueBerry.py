"""
Python installer for hueberry. Probably not the best thing in the world...
"""
import sys
import os
import shutil
#import imp
import subprocess
import shlex

def myrun(cmd):
    """from http://blog.kagesenshi.org/2008/02/teeing-python-subprocesspopen-output.html
    """
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = p.stdout.readline()
        stdout.append(line)
        print line,
        if line == '' and p.poll() != None:
            break
    return ''.join(stdout)

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print output.strip()
    rc = process.poll()
    return rc

class bcolors:
    PRPL = '\033[95m'
    BLU = '\033[94m'
    GRN = '\033[92m'
    YLO = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

temp = os.popen("cat /etc/os-release | grep raspbian").read()
#print temp
result_array = temp.split('\n')
num_groups = len(result_array) - 1

#print num_groups

if(num_groups != 4):
    print(bcolors.RED+"This OS is not Raspbian. It does not meet the directory structure requirements of this installer. Exiting"+bcolors.ENDC)
    sys.exit()
else:
    print(bcolors.GRN+"Looks like you're running Rasbian! Good start!"+bcolors.ENDC)   
#shutil.copy(pythondaemon.py,/home/pi/pythondaemon.py)

print(bcolors.BOLD+"Checking required modules. Please wait..."+bcolors.ENDC)
req_modules = ['pigpio','authenticate','Adafruit_SSD1306','RPi','rotary_encoder','wat']
n2install = []
for x in req_modules:
    try:
        #imp.find_module(x)
        #import Adafruit_SSD1306
        new_module = __import__(x)
        found = True
    except ImportError:
        print("    " + bcolors.YLO + str(x) + bcolors.ENDC + bcolors.RED + " module not found. Please install this before continuing!"+bcolors.ENDC)
        n2install.append(x)
print("\r")
#p = subprocess.Popen('htop')
#p.wait()
        
if len(n2install) > 0:
    #something wrong with this function... can't initiate apt-get update for some reason
    print("Looks like we have some requirements! Updating system repo!\n")
    #p = subprocess.Popen("sudo apt-get update")
    #p.wait()
    #cout = os.popen("apt-get update").read()
    #print cout
    myrun("apt-get -q update")
    #myrun("apt-get -y -V -q dist-upgrade")
    print("finished\r")
    
#print "test finished"
#sys.exit()

baremetal = 0
for x in n2install:
    if x == 'pigpio':
        print("Installing " +str(x))
        myrun("rm master.zip && sudo rm -rf pigpio-master && wget https://github.com/joan2937/pigpio/archive/master.zip && unzip master.zip &&  pigpio-master/make -j4 && sudo pigpio-master/make install && sudo pigpiod ")
        print("Done installing " +str(x))
    if x == 'authenticate':
        print("wtf, the " +str(x)+" module should be in the same directory. update re-clone the repo or somethihng")
        baremetal = baremetal + 1
    if x == 'Adafruit_SSD1306':
        print("Installing " +str(x))
        myrun("sudo apt-get -y install build-essential python-dev python-pip && sudo pip install RPi.GPIO && sudo apt-get -y install python-imaging python-smbus && sudo apt-get install -y git && git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git && sudo Adafruit_Python_SSD1306/python setup.py install")
        print("Done installing " +str(x))
    if x =='RPi':
        print("wtf, the " +str(x)+" module should be part of the most recent Raspberry Pi distribution.\nAre you even running this on a Pi?")
        print("installing anyway. lel")
        myrun("sudo pip install RPi.GPIO")
    if x == 'rotary_encoder':
        print("wtf, the " +str(x)+" module should be in the same directory. update re-clone the repo or somethihng")
        #myrun("echo ididathing && echo doing another thing && echo doing a third thing").read()
        baremetal = baremetal + 1

#print baremetal    
if baremetal > 0:
    print("\n\n\n" + bcolors.BOLD + "Downloading dev branch of hueBerry" + bcolors.ENDC)
    myrun("git clone -b dev https://github.com/fiveseven808/HueBerry_SmartSwitch.git")
    print("Cloned Repo lol")
    

finalreadme = """ 
\rHow to run:
    Ensure that I2c is enabled and that the display and rotary encoder are wired up properly
    [Optional] Increase I2c bus
    [Optional] Disable X and decrease GPU mem to minimum 
    [Optional] Overclock SD card
    Then run the following commands:
    
    cd HueBerry_SmartSwitch
    sudo pigpiod (if not PiGPIOd is not running already)
    sudo python hueberry.py [&]

&           Sets the program to run in the background 
            (You can see more debug messages if you omit this)
            
Enjoy! 
"""
print(finalreadme)

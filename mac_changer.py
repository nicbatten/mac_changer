#!/usr/bin/env python

import subprocess

interface = "wlan0"
new_mac="00:11:22:33:44:77"

print("[+] changing MAC address for " + interface + " to " + new_mac)

#subprocess.call("ifconfig eth0 down", shell=True)
#subprocess.call("ifconfig eth0 hw ether 11:22:33:44:55:66", shell=True)
#subprocess.call("ifconfig eth0 up", shell=True)

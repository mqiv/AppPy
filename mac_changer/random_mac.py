#!/usr/bin/env python

import random
import subprocess

# функция рандома mac
def random_mac():
    return "%02x:%02x:%02x:%02x:%02x:%02x"% (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
# new_mac = random_mac()
print(random_mac())

interface = "docker0"

def change_mac(interface, new_mac):
    # print("Mac changing", interface, "to", new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

change_mac(new_mac, interface)


# def randomMAC():
# 	mac = [ 0x00, 0x16, 0x3e,
# 		random.randint(0x00, 0x7f),
# 		random.randint(0x00, 0xff),
# 		random.randint(0x00, 0xff) ]
# 	return ':'.join(map(lambda x: "%02x" % x, mac))
#
# print randomMAC()
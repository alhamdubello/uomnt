from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint


devices = list() #I am trying to create a list of devices

#Get devices on the network
#We will use a for loop to create a dummy device list

for index in range(1, 101):
    device = dict() #this is an empty device dict
#Device Name
#we create an empty dictionary to insert hostname
    device["name"] = (
                      choice(["R1", "R2", "R3", "R4", "R5", "R6", "R7"]) 
                      + choice(["-CORE-", "-DIST-", "-ACCESS-"]) 
                      + choice(string.ascii_letters)
    )


#Naming of Vendor, OS, OS version

    device["vendor"] = choice(["Cisco", "Juniper", "Cumulus", "Arista"])
    if device["vendor"] == "Cisco":
        device["os"] = choice(["IOS", "IOS-XE", "IOS-XR", "Nexus"])
        device["os version"] = choice(["12.4", "16.1", "17.0", "20.1", "8.1"])
    elif device["vendor"] == "Juniper":
        device["os"] = "Junos"
        device["os version"] = choice(["18.1R1", "15.4R3", "20.3R1", "17.8R4"])
    elif device["vendor"] == "Cumulus":
        device["os"] = "cumulus"
        device["os version"] = choice(["2.5", "3.7","4.1","4.2"])
    elif device["vendor"] == "Arista":
        device["os"] = "eos"
        device["os version"] = choice(["4.1", "4.12","2.5", "3.4"])

#Setting of Management IP address
    device["Management IP"] = "10.0.0." + str(index)

#print devices on the network
    print("\n__________________ROUTER___")
    print()
    for key, value in device.items():
        print(f"{key:>16s} : {value}")
    devices.append(device)


##print in a Tabulated form
print("\n__IN__LIST_FORM")
pprint(devices)

print("\n___IN_TABULATED__FORM__")
sorted_devices = sorted(devices, key=itemgetter("vendor", "os", "os version"))
print(tabulate(sorted_devices, headers="keys"))


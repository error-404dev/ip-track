#! /usr/bin/python

import requests
import os

ip = input("\033[1;32m Enter ip address [+] ")
response = requests.get("http://ip-api.com/json/" + ip )

data = response.json()


print("\t [+] IP \t\t", data["query"])
print("\t [+] Country \t\t", data["country"])
print("\t [+] Country Code \t", data["countryCode"])
print("\t [+] Reg \t\t", data["region"])
print("\t [+] Reg Name \t\t", data["regionName"])
print("\t [+] City \t\t", data["city"])
print("\t [+] Zip \t\t", data["zip"])
print("\t [+] Lat \t\t", data["lat"])
print("\t [+] Lon \t\t", data["lon"])
print("\t [+] Timezone \t\t", data["timezone"])
print("\t [+] Isp \t\t", data["isp"])
print("\t [+] Org \t\t", data["org"])
print("\t [+] As \t\t", data["as"])
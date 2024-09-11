import requests

ipAddress = requests.get("https://api.ipify.org?format=json")
#ipV6 = requests.get("https://api64.ipify.org?format=json")

print (ipAddress.json ())

ipAddressInfo = requests.get (f"http://ip-api.com/json/{ipAddress.json ()['ip']}")

print (ipAddressInfo.json ())
import urllib3
import SonicAPIClass
from AddressObjectClass import AddressObjectClass
from ServiceObjectClass import ServiceObjectClass
urllib3.disable_warnings()
import time
from getpass import getpass

# Examples for Address Object List
# The available operations are UPDATE, ADD, DELETE
# The available Address Objects types are HOST, RANGE, NETWORK, FQDN
# Don't forget to add a comma at the end of each line, except the last one
# ["UPDATE", AddressObjectIPv4.AddressObjectIPv4(aoName="test1", aoZone="LAN", aoType="host", aoIPaddress="200.200.200.233")]
# ["ADD", AddressObjectIPv4.AddressObjectIPv4(aoName="test2", aoZone="LAN", aoType="range", aoIPaddressStart="200.200.200.233, aoIPaddressEnd="200.200.200.233")]
# ["DELETE", AddressObjectIPv4.AddressObjectIPv4(aoName="test3", aoZone="LAN", aoType="network", aoSubnet="100.100.100.0", aoMask="255.255.255.0")]
# ["UPDATE", AddressObjectIPv4.AddressObjectIPv4(aoName="test4", aoZone="LAN", aoType="fqdn", aoDomain="api.google.com")]


aoList = [
    ["UPDATE", AddressObjectClass(aoName="ao-test1", aoZone="LAN", aoType="host", aoIPaddress="200.200.200.111")],
    ["ADD", AddressObjectClass(aoName="ao-test2", aoZone="LAN", aoType="range", aoIPaddressStart="200.200.200.100", aoIPaddressEnd="200.200.200.200")],
    ["UPDATE", AddressObjectClass(aoName="ao-test3", aoZone="LAN", aoType="fqdn", aoDomain="api.google.com")]
]

# Examples for Service Object List
# The available operations are UPDATE, ADD, DELETE
# The available Service Objects types are TCP, UDP
# Don't forget to add a comma at the end of each line, except the last one
# ["ADD", ServiceObjectClass(soName="so-test1", soType="tcp", soPortStart=8121, soPortEnd=8121)],
# ["UPDATE", ServiceObjectClass(soName="so-test2", soType="udp", soPortStart=4433, soPortEnd=4433)],
# ["DELETE", ServiceObjectClass(soName="so-test3", soType="tcp", soPortStart=8080, soPortEnd=8080)]
soList = [
    ["ADD", ServiceObjectClass(soName="so-test1", soType="tcp", soPortStart=8121, soPortEnd=8121)],
    ["UPDATE", ServiceObjectClass(soName="so-test2", soType="udp", soPortStart=4433, soPortEnd=4433)],
    ["DELETE", ServiceObjectClass(soName="so-test3", soType="tcp", soPortStart=8080, soPortEnd=8080)]
]

HTTPstatusCodes = {
    "200": "OK",
    "400": "Bad Request",
    "401": "Not Authorized",
    "403": "Forbidden",
    "404": "Not Found",
    "405": "Method Not Allowed",
    "406": "Not Acceptable",
    "413": "Request body too large",
    "414": "Request URL too long",
    "500": "Internal Server Error",
    "503": "No resources"
}

ipAddress = '99.99.99.99'
portNumber = 443
userName = None
userPass = None

def getFirewallParams():
    global userName
    userName = input("Please enter the user name: ")
    global userPass
    userPass = getpass("Please enter your password: ")

# Authentication based on "RFC-2617 HTTP Basic Authentication"
# This authentication method needs to be enabled on the firewall
# The respective interface associated to the IP address also needs to have HTTPS user access enabled
def authentication(firewall):
    authTry = 3

    while authTry > 0:
        authStatus = firewall.authenticate()
        if authStatus != 200:
            print("API authorization failed. Trying again in 5 secs!")
            authTry -= 1
            time.sleep(5)
        else:
            authTry = 0

    print("API authorization:  ", end="")
    print("Status " + str(authStatus) + " " + HTTPstatusCodes[str(authStatus)])
    if authStatus != 200:
        print("Exiting program.")
        exit()

# This is a required step
def startFirewallManagement(firewall):
    startTry = 3
    while startTry > 0:
        mngStatus = firewall.startManagement()
        if mngStatus != 200:
            print("Starting firewall management failed with \"Status " + str(mngStatus) + " " +  HTTPstatusCodes[str(mngStatus)] + "\". Trying again in 5 secs!")
            startTry -= 1
            time.sleep(5)
        else:
            startTry = 0

    print("Starting firewall management: ", end="")
    print("Status " + str(mngStatus) + " " + HTTPstatusCodes[str(mngStatus)])
    if mngStatus != 200:
        print("Exiting program.")
        logoutUser(firewall)
        exit()

# This is required to be able to make changes on the firewall
def changeConfigMode(firewall):
    changeTry = 3
    while changeTry > 0:
        configStatus = firewall.configMode()
        if configStatus != 200:
            print("Changing to Config Mode failed with \"Status " + str(configStatus) + " " + HTTPstatusCodes[str(configStatus)] + "\". Trying again in 5 secs!")
            changeTry -= 1
            time.sleep(5)
        else:
            changeTry = 0

    print("Changing to Config Mode: ", end="")
    print("Status " + str(configStatus) + " " + HTTPstatusCodes[str(configStatus)])
    print(" ")
    if configStatus != 200:
        print("Exiting program.")
        logoutUser(firewall)
        exit()

def processAddressObjectList(firewall):
    for i in aoList:
        if i[0].upper() == "ADD":
            if i[1].getType() == "fqdn":
                if firewall.getFQDNAddressObjectByName(i[1].getName()) == 200:
                    print("Address Object already exist with name \"" + i[1].getName() + "\". Cannot ADD.\n")
                else:
                    print("ADD operation for Address Object name \"" + i[1].getName() + "\": ", end="")
                    postStatus = firewall.postFQDNAddressObjects(i[1].getJSON())
                    print("Status " + str(postStatus) + " " + HTTPstatusCodes[str(postStatus)])
                    commitChanges(firewall)
            else:
                if firewall.getIPv4AddressObjectByName(i[1].getName()) == 200:
                    print("Address Object already exist with name \"" + i[1].getName() + "\". Cannot ADD.\n")
                else:
                    print("ADD operation for Address Object name \"" + i[1].getName() + "\": ", end="")
                    postStatus = firewall.postIPv4AddressObjects(i[1].getJSON())
                    print("Status " + str(postStatus) + " " + HTTPstatusCodes[str(postStatus)])
                    commitChanges(firewall)
        elif i[0].upper() == "DELETE":
            if i[1].getType() == "fqdn":
                if firewall.getFQDNAddressObjectByName(i[1].getName()) == 200:
                    print("DELETE operation for Address Object name \"" + i[1].getName() + "\": ", end="")
                    deleteStatus = firewall.deleteFQDNAddressObjectByName(i[1].getName())
                    print(deleteStatus)
                    commitChanges(firewall)
                else:
                    print("Address Object with name \"" + i[1].getName() + "\" does not exist. Cannot DELETE!")
            else:
                if firewall.getIPv4AddressObjectByName(i[1].getName()) == 200:
                    print("DELETE operation for Address Object name \"" + i[1].getName() + "\": ", end="")
                    deleteStatus = firewall.deleteIPv4AddressObjectByName(i[1].getName())
                    print(deleteStatus)
                    commitChanges(firewall)
                else:
                    print("Address Object with name \"" + i[1].getName() + "\" does not exist. Cannot DELETE!")
        elif i[0].upper() == "UPDATE":
            if i[1].getType() == "fqdn":
                if firewall.getFQDNAddressObjectByName(i[1].getName()) == 200:
                    print("UPDATE operation for Address Object name \"" + i[1].getName() + "\": ", end="")
                    updateStatus = firewall.updateFQDNAddressObjectByName(i[1].getName(), i[1].getJSON())
                    print("Status " + str(updateStatus) + " " + HTTPstatusCodes[str(updateStatus)])
                    commitChanges(firewall)
                else:
                    print("Address Object with name \"" + i[1].getName() + "\" does not exist. Cannot UPDATE!")
            else:
                if firewall.getIPv4AddressObjectByName(i[1].getName()) == 200:
                    print("UPDATE operation for Address Object name \"" + i[1].getName() + "\": ", end="")
                    updateStatus = firewall.updateIPv4AddressObjectByName(i[1].getName(), i[1].getJSON())
                    print("Status " + str(updateStatus) + " " + HTTPstatusCodes[str(updateStatus)])
                    commitChanges(firewall)
                else:
                    print("Address Object with name \"" + i[1].getName() + "\" does not exist. Cannot UPDATE!")

def processServiceObjectList(firewall):
    for i in soList:
        if i[0].upper() == "ADD":
            if firewall.getServiceObjectByName(i[1].getName()) == 200:
                print("Service Object already exist with name \"" + i[1].getName() + "\". Cannot ADD!\n")
            else:
                print("ADD operation for Service Object name \"" + i[1].getName() + "\": ", end="")
                print(i[1].getJSON())
                postStatus = firewall.postServiceObjects(i[1].getJSON())
                print("Status " + str(postStatus) + " " + HTTPstatusCodes[str(postStatus)])
                commitChanges(firewall)
        elif i[0].upper() == "DELETE":
            if firewall.getServiceObjectByName(i[1].getName()) == 200:
                print("DELETE operation for Service Object name \"" + i[1].getName() + "\": ", end="")
                deleteStatus = firewall.deleteServiceObjectByName(i[1].getName())
                print(deleteStatus)
                commitChanges(firewall)
            else:
                print("Service Object with name \"" + i[1].getName() + "\" does not exist. Cannot DELETE!")
        elif i[0].upper() == "UPDATE":
            if firewall.getServiceObjectByName(i[1].getName()) == 200:
                print("UPDATE operation for Service Object name \"" + i[1].getName() + "\": ", end="")
                updateStatus = firewall.updateServiceObjectByName(i[1].getName(), i[1].getJSON())
                print("Status " + str(updateStatus) + " " + HTTPstatusCodes[str(updateStatus)])
                commitChanges(firewall)
            else:
                print("Service Object with name \"" + i[1].getName() + "\" does not exist. Cannot UPDATE!")

def commitChanges(firewall):
    print("Commit Changes: ", end="")
    commitStatusJSON = firewall.commitChanges()
    status = commitStatusJSON['status']['success']
    message = commitStatusJSON['status']['info'][0]['message']
    commitStatus = str(status) + ", " + str(message)
    print(commitStatus + "\n")
    if status == False:
        print("Exiting program.")
        exit()

def logoutUser(firewall):
    print("\nLogging out from the firewall: ", end="")
    logoutStatus = firewall.logoutUser(userName)
    print("Status " + str(logoutStatus) + " " + HTTPstatusCodes[str(logoutStatus)])

def main():

    getFirewallParams()
    firewall = SonicAPIClass.SonicAPIClass(ipAddress, portNumber, userName, userPass)
    authentication(firewall)
    startFirewallManagement(firewall)
    changeConfigMode(firewall)

    processAddressObjectList(firewall)
    processServiceObjectList(firewall)

    logoutUser(firewall)

if __name__ == "__main__":
    main()

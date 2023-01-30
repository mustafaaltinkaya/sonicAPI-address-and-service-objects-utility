from collections import OrderedDict
import requests

class SonicAPIClass:
    def __init__(self, hostIP, port, username, password):
        self.baseurl = 'https://' + hostIP + ":" + str(port) + "/api/sonicos/"
        self.authinfo = (username, password)
        self.headers = OrderedDict([
            ('Accept', 'application/json'),
            ('Content-Type', 'application/json'),
            ('Accept-Encoding', 'application/json'),
            ('Charset', 'UTF-8')])

    def authenticate(self):
        endpoint = 'auth'
        url = self.baseurl + endpoint
        try:
            r = requests.post(url, auth=self.authinfo, headers=self.headers, verify=False)
            return r.status_code
        except requests.exceptions.RequestException as err:
            raise SystemExit(err)

    def startManagement(self):
        endpoint = "start-management"
        url = self.baseurl + endpoint
        r = requests.post(url, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def configMode(self):
        endpoint = "config-mode"
        url = self.baseurl + endpoint
        r = requests.post(url, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def postIPv4AddressObjects(self, addressObjects):
        endpoint = 'address-objects/ipv4'
        url = self.baseurl + endpoint
        r = requests.post(url, json=addressObjects, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def postFQDNAddressObjects(self, addressObjects):
        endpoint = 'address-objects/fqdn'
        url = self.baseurl + endpoint
        r = requests.post(url, json=addressObjects, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def postServiceObjects(self, serviceObjects):
        endpoint = 'service-objects'
        url = self.baseurl + endpoint
        r = requests.post(url, json=serviceObjects, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def getIPv4AddressObjects(self):
        endpoint = 'address-objects/ipv4'
        url = self.baseurl + endpoint
        r = requests.get(url, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def getIPv4AddressObjectByName(self, aoName):
        endpoint = "address-objects/ipv4/name/" + aoName
        url = self.baseurl + endpoint
        r = requests.get(url, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def getFQDNAddressObjectByName(self, aoName):
        endpoint = 'address-objects/fqdn/name/' + aoName
        url = self.baseurl + endpoint
        r = requests.get(url, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def getServiceObjectByName(self, soName):
        endpoint = "service-objects/name/" + soName
        url = self.baseurl + endpoint
        r = requests.get(url, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def deleteIPv4AddressObjectByName(self, aoName):
        endpoint = "address-objects/ipv4/name/" + aoName
        url = self.baseurl + endpoint
        r = requests.delete(url, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def deleteFQDNAddressObjectByName(self, aoName):
        endpoint = 'address-objects/fqdn/name/' + aoName
        url = self.baseurl + endpoint
        r = requests.delete(url, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def deleteServiceObjectByName(self, soName):
        endpoint = "service-objects/name/" + soName
        url = self.baseurl + endpoint
        r = requests.delete(url, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def updateIPv4AddressObjectByName(self, aoName, aoJSON):
        endpoint = "address-objects/ipv4/name/" + aoName
        url = self.baseurl + endpoint
        r = requests.patch(url, json=aoJSON, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def updateFQDNAddressObjectByName(self, aoName, aoJSON):
        endpoint = 'address-objects/fqdn/name/' + aoName
        url = self.baseurl + endpoint
        r = requests.patch(url, json=aoJSON, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def updateServiceObjectByName(self, soName, soJSON):
        endpoint = "service-objects/name/" + soName
        url = self.baseurl + endpoint
        r = requests.patch(url, json=soJSON, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def logoutUser(self, uName):
        endpoint = "user/session/name/" + uName
        url = self.baseurl + endpoint
        r = requests.delete(url, auth=self.authinfo, headers=self.headers, verify=False)
        return r.status_code

    def commitChanges(self):
        endpoint = "config/pending"
        url = self.baseurl + endpoint
        r = requests.post(url, auth=self.authinfo, headers=self.headers, verify=False)
        return r.json()
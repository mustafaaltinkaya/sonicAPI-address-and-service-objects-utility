

class AddressObjectClass:

    def __init__(self, aoName, aoZone, aoType, aoIPaddress=None, aoIPaddressStart=None, aoIPaddressEnd=None,
                 aoSubnet=None, aoMask=None, aoDomain=None):

        self.name = aoName
        self.zone = aoZone
        self.type = aoType          # host, range, network
        self.IPaddress = aoIPaddress
        self.IPaddressStart = aoIPaddressStart
        self.IPaddressEnd = aoIPaddressEnd
        self.subnet = aoSubnet
        self.mask = aoMask
        self.domain = aoDomain

    def setName(self, aoName):
        self.name = aoName

    def setZone(self, aoZone):
        self.zone = aoZone

    def setType(self, aoType):
        self.type = aoType

    def setIPaddress(self, aoIPaddress):
        self.IPaddress = aoIPaddress

    def setIPaddressStart(self, aoIPaddressStart):
        self.IPaddressStart = aoIPaddressStart

    def setIPaddressEnd(self, aoIPaddressEnd):
        self.IPaddressEnd = aoIPaddressEnd

    def setSubnet(self, aoSubnet):
        self.subnet = aoSubnet

    def setMask(self, aoMask):
        self.mask = aoMask

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getJSON(self):
        if self.type == "host":
            self.ao = {
                "address_objects": [
                    {
                        "ipv4": {
                            "name": self.name,
                            "zone": self.zone,
                            "host": {
                                "ip": self.IPaddress
                            }
                        }
                    }
                ]
            }
            return self.ao
        elif (self.type == "range"):
            self.ao = {
                "address_objects": [
                    {
                        "ipv4": {
                            "name": self.name,
                            "zone": self.zone,
                            "range": {
                                "begin": self.IPaddressStart,
                                "end": self.IPaddressEnd
                            }
                        }
                    }
                ]
            }
            return self.ao
        elif (self.type == "network"):
            self.ao = {
                "address_objects": [
                    {
                        "ipv4": {
                            "name": self.name,
                            "zone": self.zone,
                            "network": {
                                "subnet": self.subnet,
                                "mask": self.mask
                            }
                        }
                    }
                ]
            }
            return self.ao
        elif (self.type == "fqdn"):
            self.ao = {
                "address_objects": [
                    {
                        "fqdn": {
                            "name": self.name,
                            "domain": self.domain,
                            "zone": self.zone
                        }
                    }
                ]
            }
            return self.ao
        else:
            return "Error: Unknown type"

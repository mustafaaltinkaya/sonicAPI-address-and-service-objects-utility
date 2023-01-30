class ServiceObjectClass:


    def __init__(self, soName, soType, soPortStart=None, soPortEnd=None):
        self.name = soName
        self.type = soType
        self.portStart = soPortStart
        self.portEnd = soPortEnd

    def setName(self, soName):
        self.name = soName

    def setType(self, soType):
        self.type = soType

    def setPortStart(self, soPortStart):
        self.portStart = soPortStart

    def setPortEnd(self, soPortEnd):
        self.portEnd = soPortEnd

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getPortStart(self):
        return self.portStart

    def getPortEnd(self):
        return self.portEnd

    def getJSON(self):
        if self.type == "tcp":
            self.so = {
                "service_objects": [
                    {
                        "name": self.name,
                        "tcp": {
                            "begin": self.portStart,
                            "end": self.portEnd
                        }
                    }
                ]
            }
            return self.so
        elif self.type == "udp":
            self.so = {
                "service_objects": [
                    {
                        "name": self.name,
                        "udp": {
                            "begin": self.portStart,
                            "end": self.portEnd
                        }
                    }
                ]
            }
            return self.so
        else:
            return "Error: Unknown type"
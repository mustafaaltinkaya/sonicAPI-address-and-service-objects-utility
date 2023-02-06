# Date: February 2023
# Author: Mustafa Altinkaya

# SonicWall firewalls have API endpoints, providing the ability to configure the firewall via third party tools (eg. cURL, Postman) or custom applications.
# This utility is compatible with SonicOS 7.x 
# It facilitates to ADD, UPDATE, DELETE Address Objects and Service Objects

# Examples for Address Object List
# The available operations are UPDATE, ADD, DELETE
# The available Address Objects types are HOST, RANGE, NETWORK, FQDN
# Don't forget to add a comma at the end of each line, except the last one
# ["UPDATE", AddressObjectIPv4.AddressObjectIPv4(aoName="test1", aoZone="LAN", aoType="host", aoIPaddress="200.200.200.233")]
# ["ADD", AddressObjectIPv4.AddressObjectIPv4(aoName="test2", aoZone="LAN", aoType="range", aoIPaddressStart="200.200.200.233, aoIPaddressEnd="200.200.200.233")]
# ["DELETE", AddressObjectIPv4.AddressObjectIPv4(aoName="test3", aoZone="LAN", aoType="network", aoSubnet="100.100.100.0", aoMask="255.255.255.0")]
# ["UPDATE", AddressObjectIPv4.AddressObjectIPv4(aoName="test4", aoZone="LAN", aoType="fqdn", aoDomain="api.google.com")]

#Example Address Object List
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

#Example Service Object List
soList = [
    ["ADD", ServiceObjectClass(soName="so-test1", soType="tcp", soPortStart=8121, soPortEnd=8121)],
    ["UPDATE", ServiceObjectClass(soName="so-test2", soType="udp", soPortStart=4433, soPortEnd=4433)],
    ["DELETE", ServiceObjectClass(soName="so-test3", soType="tcp", soPortStart=8080, soPortEnd=8080)]
]

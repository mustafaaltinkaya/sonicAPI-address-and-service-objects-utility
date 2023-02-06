Date: February 2023

Author: Mustafa Altinkaya

- SonicWall firewalls have API endpoints, providing the ability to configure the firewall via third party tools (eg. cURL, Postman) or custom applications.

- This utility is compatible with SonicOS 7.x 

- It facilitates to ADD, UPDATE, DELETE Address Objects and Service Objects

**Address Objects**

- The available operations are UPDATE, ADD, DELETE

- The available Address Objects types are HOST, RANGE, NETWORK, FQDN

- Don't forget to add a comma at the end of each line, except the last one

aoList = [

    ["UPDATE", AddressObjectClass(aoName="ao-test1", aoZone="LAN", aoType="host", aoIPaddress="200.200.200.111")],
    
    ["ADD", AddressObjectClass(aoName="ao-test2", aoZone="LAN", aoType="range", aoIPaddressStart="200.200.200.100", aoIPaddressEnd="200.200.200.200")],
    
    ["DELETE", AddressObjectClass(aoName="ao-test3", aoZone="LAN", aoType="fqdn", aoDomain="api.google.com")]
    
]

**Service Objects**

- The available operations are UPDATE, ADD, DELETE

- The available Service Objects types are TCP, UDP

- Don't forget to add a comma at the end of each line, except the last one

soList = [

    ["ADD", ServiceObjectClass(soName="so-test1", soType="tcp", soPortStart=8121, soPortEnd=8121)],
    
    ["UPDATE", ServiceObjectClass(soName="so-test2", soType="udp", soPortStart=4433, soPortEnd=4433)],
    
    ["DELETE", ServiceObjectClass(soName="so-test3", soType="tcp", soPortStart=8080, soPortEnd=8080)]
    
]

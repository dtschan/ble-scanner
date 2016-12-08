#!/usr/bin/env python

#from __future__ import print_function

import sys

from gattlib import GATTRequester
from time import sleep
from struct import pack
from struct import unpack
from binascii import hexlify

ADDRESS = sys.argv[1]

# Source: https://www.bluetooth.com/specifications/gatt/services
UUID_SERVICE_DECL = "00002800-0000-1000-8000-00805f9b34fb"
UUID_CHARACTERISTIC_DECL = "00002803-0000-1000-8000-00805f9b34fb"
UUID_CHARACTERISTIC_USER_DESC = "00002901-0000-1000-8000-00805f9b34fb"

# Source: https://www.bluetooth.com/specifications/gatt/characteristics
UUID_CHARACTERISTICS = {
    "00002a00-0000-1000-8000-00805f9b34fb": {"prefix": "Device name:"},
    "00002a01-0000-1000-8000-00805f9b34fb": {"prefix": "Appearance:", "fmt": "<H"},
    "00002a04-0000-1000-8000-00805f9b34fb": {"prefix": "Peripheral preferred connection parameters:", "fmt": "<HHHH"},
    "00002a05-0000-1000-8000-00805f9b34fb": {"prefix": "Service changed:"},
    "00002a19-0000-1000-8000-00805f9b34fb": {"prefix": "Battery level:", "fmt": "<B", "suffix": "%"},
    "00002a26-0000-1000-8000-00805f9b34fb": {"prefix": "Firmware revision:"},
    "00002a28-0000-1000-8000-00805f9b34fb": {"prefix": "Software revision:"},
    "00002a29-0000-1000-8000-00805f9b34fb": {"prefix": "Manufacturer:"},
}

req = GATTRequester(ADDRESS, False)

req.connect(True)

class Characteristic:
    def __init__(self, handle, value_handle, uuid, properties):
        self.handle = handle
        self.value_handle = value_handle
        self.uuid = uuid
        self.properties = properties
        self.descriptors = {}

    def addDescriptor(self, descriptor):
        self.descriptors[descriptor['uuid']] = descriptor

    def __str__(self):
        result = [hex(self.value_handle)]
        name_desc = self.descriptors.get(UUID_CHARACTERISTIC_USER_DESC)
        if name_desc:
            result.append(req.read_by_handle(name_desc['handle'])[0])
        
        char_info = UUID_CHARACTERISTICS.get(self.uuid)            
        if char_info != None:
            prefix = char_info.get('prefix')
            fmt = char_info.get('fmt')
            suffix = char_info.get('suffix')
            value = ""
            try:
                value = req.read_by_handle(self.value_handle)[0]
            except Exception as e:
                value = "<" + str(e) + ">"
            if prefix:
                result.append(prefix)
            if fmt:
                value = unpack(fmt, value)
                if len(value) == 1:
                    value = value[0]
            result.append(str(value))
            if suffix:
                result.append(suffix)
        
        return " ".join(result)

characteristics = {}

chars = req.discover_characteristics()
for char in chars:
  characteristics[char['handle']] = Characteristic(**char)

descs = req.discover_descriptors()
for desc in descs:
    uuid = desc['uuid']    
    if uuid == UUID_SERVICE_DECL:
        pass
    elif uuid == UUID_CHARACTERISTIC_DECL:
        handle = desc['handle']
    else:
        characteristics[handle].addDescriptor(desc) 

for handle, char in characteristics.iteritems():   
    print(str(char))

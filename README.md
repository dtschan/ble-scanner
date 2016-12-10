# ble-scanner
Scans characteristics of Bluetooth Low Energy devices.

Tested on CentOS 7.

## Installation

1. Clone this repository:

        git clone https://github.com/dtschan/ble-scanner
        cd ble-scanner

1. Install prerequisites of [pygattlib](https://github.com/matthewelse/pygattlib) as listed in its [DEPENDS](https://github.com/matthewelse/pygattlib/blob/master/DEPENDS) file.
2. Install prerequisites of ble-scanner:

        sudo pip install -r requirements.txt

## Usage

1. Discover the mac address of the Bluetooth Low Energy device you want to scan:

        sudo hcitool lescan
    
   Example output:
           
        LE Scan ...        
        00:00:5E:00:53:42 (unknown)
        00:00:5E:00:53:42 LPF2 Smart Hub 2 I/O

2. Run ble-scanner with the discovered MAC Address:

        sudo ./ble-scanner.py MAC_ADDRESS

   e.g.:

        sudo ./ble-scanner.py 00:00:5E:00:53:42

### Example output

    GATT Characteristics of BLE Device 00:00:5E:00:53:42

    HANDLE UUID                                 PROP     DESCRIPTION
    0x0003 00002a00-0000-1000-8000-00805f9b34fb -r------ Device name: LPF2 Smart Hub 2 I/O
    0x0005 00002a01-0000-1000-8000-00805f9b34fb -r------ Appearance: 0
    0x0007 00002a04-0000-1000-8000-00805f9b34fb -r------ Peripheral preferred connection parameters: (80, 160, 0, 1000)
    0x000a 00002a05-0000-1000-8000-00805f9b34fb -----i-- Service changed: <Characteristic value/descriptor operation failed: Attribute can't be read>
    0x000e 00001524-1212-efde-1523-785feabcd123 -r-w---- Name Char
    0x0011 00001526-1212-efde-1523-785feabcd123 -r--n--- Button Char
    0x0015 00001527-1212-efde-1523-785feabcd123 ----n--- Port Type Char
    0x0019 00001528-1212-efde-1523-785feabcd123 -r--n--- Low Voltage alert
    0x001d 00001529-1212-efde-1523-785feabcd123 -r--n--- High Current alert
    0x0021 0000152a-1212-efde-1523-785feabcd123 -r--n--- Low Signal alert
    0x0025 0000152b-1212-efde-1523-785feabcd123 ---w---- Turn off device
    0x0028 0000152c-1212-efde-1523-785feabcd123 -r-w---- Vcc port control
    0x002b 0000152d-1212-efde-1523-785feabcd123 -r------ Battery type Indicator
    0x002e 0000152e-1212-efde-1523-785feabcd123 ---w---- Disconnect Char
    0x0032 00001560-1212-efde-1523-785feabcd123 -r--n--- Sensor Value
    0x0036 00001561-1212-efde-1523-785feabcd123 ----n--- Value format
    0x003a 00001563-1212-efde-1523-785feabcd123 --Ww---- Input Command
    0x003d 00001565-1212-efde-1523-785feabcd123 --Ww---- Output Command
    0x0041 00002a26-0000-1000-8000-00805f9b34fb -r------ Firmware revision: 1.0.09.0000
    0x0043 00002a28-0000-1000-8000-00805f9b34fb -r------ Software revision: 2.0.00.0000
    0x0045 00002a29-0000-1000-8000-00805f9b34fb -r------ Manufacturer: LEGO System A/S
    0x0048 00002a19-0000-1000-8000-00805f9b34fb -r--n--- Battery level: 100 %

    b: broadcast    r: read        W: write without response         w: write
    n: notify       i: indicate    a: authenticated signed writes    e: extended properties

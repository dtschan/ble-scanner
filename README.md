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

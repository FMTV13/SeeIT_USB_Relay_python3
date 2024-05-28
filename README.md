# Seeit USB Relay4/8 Python script
## Usage
```
python3 ./command_relay.py /dev/ttyUSB[x] <start|relaynum|off> [relaynum]* ....
```

Tested on: Ubuntu 20.04.6 LTS 4.19.16-1 (2024-05-28) x86_64 GNU/Linux

## Find serial interface
```
$ dmesg | grep pl230
[16759.173496] pl2303 3-1.7:1.0: pl2303 converter detected
[16759.174960] usb 3-1.7: pl2303 converter now attached to ttyUSB2
```
On Linux, for relay the driver pl230 is used.

```
[21792.620472] usb 3-1.7: new full-speed USB device number 13 using xhci_hcd
[21792.721294] usb 3-1.7: New USB device found, idVendor=067b, idProduct=2303, bcdDevice= 3.00
[21792.721302] usb 3-1.7: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[21792.721307] usb 3-1.7: Product: USB-Serial Controller
[21792.721311] usb 3-1.7: Manufacturer: Prolific Technology Inc.
[21792.729822] pl2303 3-1.7:1.0: pl2303 converter detected
[21792.731098] usb 3-1.7: pl2303 converter now attached to ttyUSB2
```

## Commands
```
$ python3 ./command_relay.py /dev/ttyUSB2 start     # First thing to do when board is attached
$ python3 ./command_relay.py /dev/ttyUSB2 1         # Activate only relay 1
$ python3 ./command_relay.py /dev/ttyUSB2 1 4       # Activate relay 1 and 4
$ python3 ./command_relay.py /dev/ttyUSB2 off       # Set all relays off
```

## Example session
```
$ python3 ./command_relay.py /dev/ttyUSB2 1
0: relay is on, 1: relay is off.
Least significant bit is smallest index
(4 channel USB relay positions: 0b[4 3 2 1])
0b11111110
```

## Links
(https://www.seeit.fr/produits.php?r2=41)
(https://produktinfo.conrad.com/datenblaetter/75000-99999/097621-an-01-ml-4_KANALIGE_RELAISKARTE_MICROUSB_en_fr.pdf)
(https://docplayer.fr/102030549-Usb-relay04-usb-relay08.html)

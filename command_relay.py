#!/usr/bin/env python
import serial
import time
import sys
import os
import struct

# board commands
GET_BOARD_ID='P'
SET_CMD_MODE='Q'

# Board ID to channel mapping
board = {}
board['ad'] = 2
board['ab'] = 4
board['ac'] = 8

# serial interface


def print_usage():
    print("Usage: " + sys.argv[0] + " /dev/ttyUSB[x] <start|relaynum|off> [relaynum]* ....")
    print("(relaynumber starts with 1. Any number of relay numbers can be passed.\n"
                "relnum = 'start' to startup device and get board id. relnum = 'off' to reset device.)")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print_usage()
        exit(-1);

    dev=sys.argv[1]
    relnum=sys.argv[2]
    if not dev or not relnum:
        print_usage()
        exit(-1);

    fd=serial.Serial(dev, 9600)

    if relnum == 'start':
        fd.write(str.encode(GET_BOARD_ID))
        time.sleep(1)

        bid=os.read(fd.fileno(), 1)

        if bid:
            print("Board id: " + str(bid.hex()))
            print("Board has " + str(board[bid.hex()]) + " channels.")
            fd.write(str.encode(SET_CMD_MODE))
            time.sleep(1)
        exit(0)

    if relnum == 'off':
        value=0xFF
    else:
        value=0xFF
        for rnum in sys.argv[2:]:
            value &= ~(1<<(int(rnum,16)-1))

    print("0: relay is on, 1: relay is off. \nLeast significant bit is smallest index\n"
        "(4 channel USB relay positions: 0b[4 3 2 1])")
    print(bin(value))
    assert(fd.write(struct.pack('B', value)) == 1)

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
    print("Usage: " + sys.argv[0] + " /dev/ttyUSB[x] <start|on|off> [relay number]* ....")
    print("(Any number of relay numbers lower than 1 or higher than 8 will be ignored.\n"
                "command = 'start' to startup device and get board id.\n"
                "command = 'on' to enable the relay.)"
                "command = 'off' to disable the relay.)")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print_usage()
        exit(-1);

    dev=sys.argv[1]
    command=sys.argv[2]

    if not dev or not command:
        print_usage()
        exit(-1);

    fd=serial.Serial(dev, 9600)

    if command == 'start':
        fd.write(str.encode(GET_BOARD_ID))
        time.sleep(1)

        bid=os.read(fd.fileno(), 1)
    
        if bid:
            print("Board id: " + str(bid.hex()))
            print("Board has " + str(board[bid.hex()]) + " channels.")
            fd.write(str.encode(SET_CMD_MODE))
            time.sleep(1)
        exit(0)

    elif command == 'off':
        value=0x00
        for rnum in sys.argv[3:]:
            if int(rnum)>0 and int(rnum)<9:
                value |= (1<<(int(rnum,16)-1))
        if value==0x00:
            value = 0xFF
    elif command == 'on':
        value=0xFF
        for rnum in sys.argv[3:]:
            if int(rnum)>0 and int(rnum)<9:
                value &= ~(1<<(int(rnum,16)-1))
        if value==0xFF:
            value = 0x00

    print("0: relay is on, 1: relay is off. \nLeast significant bit is smallest index\n"
        "(channel USB relay positions: 0b[8 7 6 5 4 3 2 1])")
    print(format(value, '#010b'))
    assert(fd.write(struct.pack('B', value)) == 1)

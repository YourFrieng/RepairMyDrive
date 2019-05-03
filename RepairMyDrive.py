#!/usr/bin/env python3
import os


#start hdparm for an override this blocks
def makeMagic(drive,filename):
    for line in open(filename, 'r'):
        result = int(line)
        os.system( "hdparm --repair-sector %s --yes-i-know-what-i-am-doing %s"  %(result, drive))



TXTname = input('Write name of file or path with numbers of your badblocks: ')
drivePath = input('Write path for your defective drive: ')

makeMagic(drivePath,TXTname)
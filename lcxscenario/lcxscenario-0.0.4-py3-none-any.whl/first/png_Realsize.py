import os
import binascii
import struct

crcbp = open("00000000.png", "rb").read()    #打开图片
for i in range(2000):
    for j in range(2000):
        data = crcbp[12:16] + \
            struct.pack('>i', i)+struct.pack('>i', j)+crcbp[24:29]
        crc32 = binascii.crc32(data) & 0xffffffff
        if(crc32 == 0x59f1d4be):    #图片当前CRC 需要在前面加0x
            print(i, j)
            print('hex:', hex(i), hex(j))

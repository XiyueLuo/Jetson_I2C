import io
import sys
import fcntl
import time
import copy
import string
# from AtlasI2C import (
# 	 AtlasI2C
# )

def write(file_write, cmd):
    '''
    appends the null character and sends the string over I2C
    '''
    cmd += "\00"
    file_write.write(cmd.encode('latin-1'))

bus = 1
file_read = io.open(file="/dev/i2c-{}".format(bus), 
                                 mode="rb", 
                                 buffering=0)
file_write = io.open(file="/dev/i2c-{}".format(bus),
                                  mode="wb", 
                                  buffering=0)
addr = 102
I2C_SLAVE = 0x703
fcntl.ioctl(file_read, I2C_SLAVE, addr)
fcntl.ioctl(file_write, I2C_SLAVE, addr)
write(file_write, "I")
time.sleep(0.3)
num_of_bytes = 31
raw_data = file_read.read(num_of_bytes)
print(raw_data)

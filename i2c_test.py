import ctypes
import pylibi2c
import string

# Open i2c device @/dev/i2c-1, addr 066.
i2c = pylibi2c.I2CDevice('/dev/i2c-1', 0x66)

# Open i2c device @/dev/i2c-1, addr 0x66, 16bits internal address
i2c = pylibi2c.I2CDevice('/dev/i2c-1', 0x66, iaddr_bytes=0)

# Set delay
i2c.delay = 10

# # Set page_bytes
i2c.page_bytes = 16

# # Set flags
i2c.flags = pylibi2c.I2C_M_IGNORE_NAK

## Python3
buf = bytes(256)

# Write data to i2c, buf must be read-only type
# size = i2c.write(0x0, buf)

# From i2c 0x0(internal address) read 256 bytes data, using ioctl_read.
#data = i2c.ioctl_read(0x0, 256)
data = i2c.read(0x0, 256)
print(data)
#print(str(''.join(data)))
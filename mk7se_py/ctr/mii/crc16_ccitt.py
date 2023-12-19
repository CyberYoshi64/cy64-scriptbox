"""
# CRC-16/XMODEM (from Wii)
"""

class CRC16:
	result = 0
	def __init__(self, data=None):
		if data: self.append(data)
	
	def append(self, data):
		"""Adapted from https://www.3dbrew.org/wiki/Mii#Checksum"""
		crc = self.result
		
		for char in data:
			for b in range(7,-1,-1):
				crc = \
					((crc << 1) | ((char >> b) & 1)) \
					^ (0x1021 if crc & 0x8000 else 0)
		
		self.result = crc & 0xFFFF
		return self
	
	def digest(self):
		crc = self.result
		for _ in range(16): crc = (crc << 1) ^ (0x1021 if crc & 0x8000 else 0)
		return crc & 0xFFFF

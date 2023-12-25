"""
## FaceCrypt

Sources: jaames
"""

from Crypto.Cipher import AES

NONCE_OFF = 0xC
NONCE_LEN = 8
TAG_LEN = 0x10

key = bytes([0x59, 0xFC, 0x81, 0x7E, 0x64, 0x46, 0xEA, 0x61, 0x90, 0x34, 0x7B, 0x20, 0xE9, 0xBD, 0xCE, 0x52])

def decrypt(buffer):
    """From https://gist.github.com/jaames/96ce8daa11b61b758b6b0227b55f9f78"""
    nonce = buffer[:NONCE_LEN]
    cipher = AES.new(key, AES.MODE_CCM, nonce + bytes([0]*4), mac_len=TAG_LEN)
    content = cipher.decrypt(buffer[NONCE_LEN:0x70])
    return content[:NONCE_OFF] + nonce + content[NONCE_OFF:]

def encrypt(cfsd):
    nonce = cfsd[NONCE_OFF : NONCE_OFF+NONCE_LEN]
    cipher = AES.new(key, AES.MODE_CCM, nonce + bytes([0]*4), mac_len=TAG_LEN)
    content, tag = cipher.encrypt_and_digest(cfsd[:NONCE_OFF] + cfsd[NONCE_OFF+NONCE_LEN:] + bytes([0]*NONCE_LEN))
    return nonce + content[:-NONCE_LEN] + tag

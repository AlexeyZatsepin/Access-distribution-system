import chilkat
import sys

from setuptools._backport.hashlib._sha512 import sha512


def get_crypt(base):
    crypt = chilkat.CkCrypt2()
    success = crypt.UnlockComponent("Unlocked")
    if not success:
        print(crypt.lastErrorText())
        sys.exit()
    crypt.put_CryptAlgorithm("aes")
    crypt.put_CipherMode("cbc")
    crypt.put_KeyLength(256)
    crypt.put_PaddingScheme(3)
    crypt.put_EncodingMode("hex")
    ivHex = "000102030405060708090A0B0C0D0E0F"
    crypt.SetEncodedIV(ivHex, "salt")
    keyHex = "000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F"
    crypt.SetEncodedKey(keyHex, base)
    return crypt

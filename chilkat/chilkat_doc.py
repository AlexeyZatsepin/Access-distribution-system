import sys
import chilkat

crypt = chilkat.CkCrypt2()
success = crypt.UnlockComponent("Anything for 30-day trial")
if not success:
    print(crypt.lastErrorText())
    sys.exit()

#  AES is also known as Rijndael. symmetric algorithm block ciphering
crypt.put_CryptAlgorithm("aes")

#  CipherMode may be "ecb", "cbc", "ofb", "cfb", "gcm", etc.
#  Note: Check the online reference documentation to see the Chilkat versions
#  when certain cipher modes were introduced.
crypt.put_CipherMode("cbc")

#  KeyLength may be 128, 192, 256
crypt.put_KeyLength(256)

#  The padding scheme determines the contents of the bytes
#  that are added to pad the result to a multiple of the
#  encryption algorithm's block size.  AES has a block
#  size of 16 bytes, so encrypted output is always
#  a multiple of 16.
crypt.put_PaddingScheme(0)

#  EncodingMode specifies the encoding of the output for
#  encryption, and the input for decryption.
#  It may be "hex", "url", "base64", or "quoted-printable".
crypt.put_EncodingMode("hex")
#  initialization vector = IV
#  An initialization vector is required if using CBC mode.
#  ECB mode does not use an IV.
#  The length of the IV is equal to the algorithm's block size.
#  It is NOT equal to the length of the key.
ivHex = "000102030405060708090A0B0C0D0E0F"
crypt.SetEncodedIV(ivHex, "salt")

#  The secret key must equal the size of the key.  For
#  256-bit encryption, the binary secret key is 32 bytes.
#  For 128-bit encryption, the binary secret key is 16 bytes.
keyHex = "000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F"
crypt.SetEncodedKey(keyHex, "salt")

#  Encrypt a string...
#  The input string is 44 ANSI characters (i.e. 44 bytes), so
#  the output should be 48 bytes (a multiple of 16).
#  Because the output is a hex string, it should
#  be 96 characters long (2 chars per byte).
encStr = crypt.encryptStringENC("The quick brown fox jumps over the lazy dog.")
print(encStr)

#  Now decrypt:
decStr = crypt.decryptStringENC(encStr)
print(decStr)

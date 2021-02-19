from DecryptData import *
from DatabaseConnect import *
def getall():
    listall = getLoginInfo()
    for info in listall:
        decryptpass = decrypt_password(info[2])
        print(info[0], info[1], decryptpass)
if __name__ == "__main__":
    getall()
    rmdb()
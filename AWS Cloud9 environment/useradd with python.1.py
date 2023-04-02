import os
def newm():
    confirm="N"
    while confirm != "Y":
        username = input("enter username you want")
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
    os.system("sudo adduser " + username)
newm()
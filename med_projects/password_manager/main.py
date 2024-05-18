from cryptography.fernet import Fernet

'''def write_key():
    key=Fernet.generate_key()
    with open('key.key','wb') as f:
        f.write(key)
write_key()'''

def load_key():
    file= open("key.key","rb")
    key =file.read()
    file.close()
    return key

def add():
    name=input("Account Name\n")
    pwd=input("Account Password\n")
    with open('passwords.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
                

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw = data.split("|")
            '''print(user, passw)'''
            print("user:",user, "| password:" , fer.decrypt(passw.encode()).decode())

pwd=input("WHAT IS THE MASTER PASSWORD\n").strip().lower()
key =load_key()
fer=Fernet(key)
                
if pwd =="pwd":
    while True:
        mode =input("would you like to aad a new password or view existing ones (view,add) or press q to quit ?").strip().lower()
        if mode == "q":
            break
        if mode == "view":
            view()
        elif mode == "add":
            add()




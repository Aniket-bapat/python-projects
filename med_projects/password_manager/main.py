from cryptography.fernet import Fernet

answer = input('To create a new master key press 1\nPress 2 to manage your passwords.\n') 
while True:
    match answer:
        case '1':
            pwd=input('Create a new master key.')

            def write_key():
                key=Fernet.generate_key()+pwd.encode()
                with open('key.key','wb') as f:
                    f.write(key)
            write_key()
            break
        case '2':
            print('You have chosen to manage your passwords.')
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
            code = key.decode()
            li=(code.split("="))
            fer=Fernet(key)

            if pwd==li[1]:
                print("ACCESS GRANTED")
                while True:
                    mode =input("would you like to aad a new password or view existing ones (view,add) or press q to quit ?").strip().lower()
                    if mode == "q":
                        break
                    if mode == "view":
                        view()
                    elif mode == "add":
                        add()      

            else:
                print("ACCESS DENIED")
                break
        case _:
            print('You have entered an invalid option.')
            break

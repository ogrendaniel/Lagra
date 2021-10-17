
def login(users):
    x=0
    user=input("User: ")
    password=input("Password: ")
    while x==0:
        if user in users and password == users[user]:
            x=1
            return user
        else:
            print("Invalid username or password")
            options2 = {"r":"Try again", "q":"Quit"}
            k=menu("What do you want to do?", "My choice: ", options2)
            if k =="r":
                print()
                user=input("User: ")
                password=input("Password: ")
            elif k== "q":
                return None
             

def menu(title,prompt,options):
    print(title)
    for x in options:
        print (f"{x}: {options[x]}")
    option = input("Action")
    x=0
    while x==0:
        if option in options:
            x=1
        else:
            option = input("Action")
   
    return option


users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
user = login(users)


    

    
    
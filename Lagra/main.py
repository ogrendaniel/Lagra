def add(prompt,strings):
    newItem=input(prompt)
    strings.append(newItem)
    return None

def view(description,strings):
    print (description)
    print()
    n=1
    for x in strings:
        print (f"{n}) {x}")
        n=n+1
    
    return None

def menu(title,prompt,options):
    print(title)
    print()
    for x in options:
        print (f"{x}: {options[x]}")
    print()
    option = input("Action: ")
    x=0
    while x==0:
        if option in options:
            x=1
        else:
            option = input("Action: ")
   
    return option

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
            
def user_actions(user,items):
    print(f"Welcome {user}!")
    view("These are your items",items)
    print()
    options = {"a":"Add item", "l":"List items", "q":"Log out"}
    option= menu("Select an action","Option",options)
    while option!="q":
        if option=="a":
            add("Add item: ",items)
            option= menu("Select an action","Option",options)
            view("These are your items",items)
        elif option == "l":
            view("These are your items",items)
            option= menu("Select an action","Option",options)
        else:
            print("Enter a valid answer!")
            option= menu("Select an action","Option",options)
            
    print(f"Goodbye {user}, your items: {items}")
    return items

def main():
    users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
    data  = {"nisse":["luva", "vante"],  "stina":[], "bosse":["gräs", "mjölk"]}
    while True:
        option=menu("Select an action","Action",{"l":"Log in", "q": "quit"})
        if option == "l":
            user=login(users)
            if user ==None:
                option=menu("Select an action","Action",{"l":"Log in", "q": "quit"})
            else:
                user_actions(user,data[user])
                option=menu("Select an action","Action",{"l":"Log in", "q": "quit"})
        elif option == "q":
            option=menu("Select an action","Action",{"l":"Log in", "q": "quit"})
            
        else:
            print("Enter l or q!")
            option=menu("Select an action","Action",{"l":"Log in", "q": "quit"})
       
            
                    
        
        
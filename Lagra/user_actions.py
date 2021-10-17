#Test
user1 = "nisse"
user2 = "bosse"

items1 = ["luva", "vante"]
items2 = ["hammare", "skruv", "spik"]
#Slut test
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
    option = input("Action")
    x=0
    while x==0:
        if option in options:
            x=1
        else:
            option = input("Action")
   
    return option

def user_actions(user,items):
    print(f"Welcome {user}!")
    view("These are your items",items)
    print()
    options = {"a":"Add item", "l":"List items", "q":"Log out"}
    option= menu("Select an action","Option",options)
    while option!="q":
        if option=="a":
            add("Add item",items)
            option= menu("Select an action","Option",options)
        elif option == "l":
            view("These are your items",items)
            option= menu("Select an action","Option",options)
        else:
            print("Enter a valid answer!")
            option= menu("Select an action","Option",options)
            
    print(f"Goodbye {user}, your items: {items}")
        
    

def menu(title,prompt,options):
    print(title)
    for x in options:
        print (x)
    option = input("Action")
    x=0
    while x==0:
        if option in options:
            x=1
        else:
            option = input("Action")
   
    return option
            
options1 = {"a":"Add item", "l":"List items", "q":"Log out"}
opt1 = menu("Select an action", "Action: ", options1)
print(f"You selected action {opt1}) {options1[opt1]}")
print()

options2 = {"r":"Try again", "q":"Quit"}
opt2 = menu("What do you want to do?", "My choice: ", options2)
print(f"You selected option {opt2}) {options2[opt2]}")

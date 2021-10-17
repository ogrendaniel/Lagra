ducks = ["Huey", "Dewey", "Louise"]
names = ["nisse", "stina", "bosse", "mimmi"]
strings=[]
users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}
data = {"nisse":["luva", "vante"], "bosse":["spik", "skruv", "hammare"], "stina":["tidsmaskin"]}
options = {"a":"Add item", "l":"List items", "q":"Log out"}
n=5

print("Select an action")
print()
for x in options:
    print (f"{x}) {options[x]}")
    
option=input("Option: ")
x=0
while x==0:
    if option =="a":
        print("You selected option a) Add item")
        x=1
    elif option == "l":
        print ("You selected option l) List items")
        x=1
    elif option == "q":
        print("You selected option q) Log  out")
        x=1
    else:
        option=input("Option: ")

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

print("Användare:")
print()
for x in users:
    print(x)

print("Användare och lösenord")
print()
for x in users:
    print(f"{x}) {users[x]}")
    
print("Användare och deras data:")
print()
for x in data:
    print(f"{x}) {data[x]}")
visaAnvändare= input("Slå upp användare: ")
if visaAnvändare in data:
    print(f"Data lagrat för {visaAnvändare}: {data[visaAnvändare]}")
else:
    print(f"Användaren {visaAnvändare} finns inte")
    
    
    
print(n)
for x in range (n):
    add("Lägg till en sträng",strings)
antalSträngar= f"Du har matat in följande {n} strängar"
view(antalSträngar,strings)
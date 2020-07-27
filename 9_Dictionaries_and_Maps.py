global contacts

def searchContact(name):
    if name in contacts.keys():
        print(f'{name}={contacts[name]}')
        return
    else:
        print('Not found')
        return

num = int(input())
contacts = {}
names = []

for i in range(0, num):
    contact = list(input().split(" "))
    contacts.update({contact[0] : contact[1]})

for i in range(0, num):
    names.append(input())
    list(map(searchContact, names))
    names.clear()
    
    

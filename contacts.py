import json

contacts = []

def LoadContacts():    
    with open('prog1-10-0810/contacts.json', 'r', encoding='UTF8') as file:        
        data = json.load(file)
        global contacts
        contacts = data['contacts_list']    

def PrintContacts():
    for contact in contacts:
        print(f"{contact['name']} {contact['surname']} {contact['number']} {contact['email']}")

def AddContact():
    name = input('Enter name: ')
    surname = input('Enter surname: ')
    number = input('Enter number: ')
    email = input('Enter email: ')

    contact = {
        'name': name, 
        'surname': surname, 
        'number': number,
        'email': email
    }

    contacts.append(contact)

def DeleteContact():
    name = input('Enter name: ')    
    found = False

    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            found = True
            break

    if found:
        print(f"Contact {name} has been deleted.")
    else:
        print(f"Contact {name} not found.")

def SaveContacts():
    with open('prog1-10-0810/contacts.json', 'w', encoding='UTF8') as file:
        contacts_dict = {'contacts_list': contacts}
        json.dump(contacts_dict, file, indent=4)

LoadContacts()
while(True):
    response = input('A-add new, D-delete, P-print, E-exit: ')
    if response == 'A':        
        AddContact()
        SaveContacts()
    elif response == 'P':
        PrintContacts()
    elif response == 'D':
        DeleteContact()
        SaveContacts()
    elif response == 'E':
        print('Bye bye!')
        break

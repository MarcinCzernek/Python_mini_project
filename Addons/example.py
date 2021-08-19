import pickle

MENU = """SELECT AN OPTION
------------------
1. ADD NEW CONTACT
2. LIST CONTACTS 
3. REMOVE CONTACTS 
4. LOAD FROM FILE 
5. SAVE TO FILE 
6. QUIT 
"""

def main():
    contacts = []
    option = 0
    file = "address.dat"

    while True:
        print(MENU)
        option = input("")
        try:
            option = int(option)
        except:
            print("Invalid input!")
            continue
        if option == 1:
            contacts.append(get_contact_input())
        elif option == 2:
            print_contact_info(contacts)
        elif option == 3:
            name = input("Enter name of contact to remove: ")
            remove_contact(name, contacts)
        elif option == 4:
            contacts = load_data(file)
        elif option == 5:
            save_data(contacts, file)
        elif option == 6:
            break
        else:
            print("Invalid input!")


def save_data(contacts, file):
    savefile = open(file, 'wb')
    pickle.dump(contacts, savefile)
    savefile.close()
    print("Saved to file...")

def load_data(file):
    loadfile = open(file, 'rb')
    book = pickle.load(loadfile)
    loadfile.close()
    print("File loaded...")
    return book


def remove_contact(to_remove, contacts):
    for contact in contacts:
        if contact['name'] == to_remove:
             contacts.remove(contact)


def print_contact_info(contacts):
    for contact in contacts:
        print(contact['name'])
        print(contact['addr'])
        print(contact['city'] + ',' + contact['state'], contact['zip'])
        print('phone :', contact['phone'])
        print()


def get_contact_input():
    name = input("Name: " )
    addr = input("Street: ")
    city = input("City: ")
    state = input("State: ")
    zipcode = input("ZIP: " )
    phone = input("Phone: ")
    return {'name': name, 'addr':addr, 'city':city,
            'state':state, 'zip':zipcode, 'phone':phone}

if __name__ == "__main__.":
    main()
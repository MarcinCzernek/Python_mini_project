import pickle

class ContactControl:
    __contactsList = []
    file = "file.txt"

    #dodaj kontakt
    def addContact (self, name, address, email, phone):
        self.__contactsList.append(Contact(name, address, email, phone))

    #lista kontaktów
    def listContacts(self):
        if not self.__contactsList:
            print("No contacts found")
        for contact in self.__contactsList:
            contact.prettyPrint()

    #usuń wszystkie kontakty
    def deleteAllContacts(self):
        self.__contactsList = []

   #usuń kontakt
    def deleteContact(self, name, address, email, phone):
        for contact in self.__contactsList:
            if contact.name == name and contact.address == address and contact.email == email and contact.phone == phone:
                self.__contactsList.remove(contact)
                return True
            return False

    #wyszukaj kontakty
    def searchContacts(self, name, address, email, phone):
        for contact in self.__contactsList:
            if name in contact.name and address in contact.address and email in contact.email and phone in contact.phone:
                contact.prettyPrint()

   #zapisz kontakt do pliku
    def save_data(self):
        savefile = open('file.txt', 'wb')
        pickle.dump(self.__contactsList, savefile)
        savefile.close()
        print("Saved to file...")

    #wczytaj kontakty z pliku
    def load_data(self):
        load_file = open('file.txt', 'rb')
        text = load_file.read().decode(errors='replace')
        print(text)
        print("File loaded...")

#klasa reprezentujaca kontakt
class Contact:
    name = None
    Address = None
    Email = None
    Phone = None

    def __init__(self, name, address, email, phone):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone

    #wyświetlenie danych  kontaktu
    def prettyPrint(self):
        print("""
            Name: %s,
            Address: %s,
            Email: %s,
            Phone: %s""" % (self.name, self.address, self.email, self.phone))


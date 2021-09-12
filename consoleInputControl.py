import datetime
import time

import contactControl
from verify_email import verify_email

class ConsoleInputControl:
    "Ta statyczna klasa zarządza wejściem"
    contactControl = None
    file = "file.txt"


    def __init__(self):
        self.contactControl = contactControl.ContactControl()

    "Metoda pobierająca od użytkownika dane do nowego kontaktu"
    def __getContactFromUser(self):
        print("Enter the name of this contact")
        name = input()
        print("Enter the address of this contact")
        address = input()
        print("Enter the email of this contact")
        email = input()
        print("Enter the phone number of this contact")
        phone = input()
        return (name, address, email, phone)

    #Funkcja dodająca nowy kontakt do kontaktów
    def __addContactToContacts(self):
        name, address, email, phone = self.__getContactFromUser()
        contact = self.contactControl.addContact(name, address, email, phone)

    # Sprawdzenie czy podany email istnieje
    def message(self, text, end="\n"):
        print(f">>>{text}",end=end)

    #Weryfikuje email
    def __verifyEmail(self):
      self.message("Email address:",end="")
      mail = input()
      if mail in["", None]:
          self.message("Please enter email address")
          exit()

      if verify_email(mail):
          self.message(f"Email {mail} exists!")
      else:
          self.message(f"Email {mail} not exists!")

#Funkcja wyświetlająca aktualną datę i czas.
    def __seeDate(self):
        x = datetime.datetime.now()
        print(f"Today is {x}")
        time.sleep(4)

    def __load_data3(self,file):
        try:
            with open(self.file, encoding='utf-8') as file:
                print(file.read())
        except FileNotFoundError:
            print("That file was not found")

    #Usuwanie kontaktu z listy kontaktów.
    def __deleteContactFromContacts(self):
        name, address, email, phone = self.__getContactFromUser()
        if self.contactControl.deleteContact(
          name, address, email, phone ):
            print("Sucessfully removed contact!")
        else:
            print("Failed to find contact, please try again")


    #Tworzenie operacji wyszukiwania według konkretnej informacji w kontakcie (np. po nazwie kontaktu lub adresie)
    def __createSearch(self):
        done = False
        name = ""
        address = ""
        email = ""
        phone = ""


        while not done:
            print(""" What info do you want to search on?
                   name
                   address
                   email
                   phone?
                   """)
            respond = input()
            if respond.lower() == "name":
                print("Please give the name of this contact")
                name = input()
            else:
                if respond.lower() == "address":
                    print("Please give the address of this contact")
                    address = input()
                else:
                    if respond.lower() == "email":
                        print("Please give the email address of this contact")
                        email = input()
                    else:
                        if respond.lower() == "phone":
                             print("Please give the phone number of this contact")
                             phone = input()
                        else:
                            print("Please enter a valid input")
            print("Do you want to enter more info (y/n)?")
            done = input() == "n"
        self.contactControl.searchContacts(name, address, email, phone)

    #zarządzanie odpowiedziami uzytkownika
    def __parse(self, respond, file="file.txt"):
        if respond.lower() == "list":
            self.contactControl.listContacts()
            return True
        if respond.lower() == "add":
            self.__addContactToContacts()
            return True
        if respond.lower() == "delete":
            self.__deleteContactFromContacts()
            return True
        if respond.lower() == "delete all":
            self.contactControl.deleteAllContacts()
            print("Sucessfully deleted all contacts")
            return True
        if respond.lower() == "search":
            self.__createSearch()
            return True
        if respond.lower() == "verify":
            self.__verifyEmail()
            return True
        if respond.lower() == "save":
            self.contactControl.save_data()
            return True
        if respond.lower() == "load":
            self.contactControl.load_data()
            return True
        if respond.lower() == "time":
            self.__seeDate()
            return True
        if respond.lower() == "close":
            print("See you next time!")
            return False

#Funkcja z menu głównym aplikacji
    def run(self):
        running = True
        welcome = "Welcome to your favorite address book"
        mainMenu = """What do you want to do? Type command.
        ---------------------------------------
        | List        | Lists all users
        | Add         | Adds an user
        | Delete      | Deletes an user
        | Delete all  | Removes all users
        | Search      | Search or a user
        | Verify      | Verify email address
        | Save        | Save information to file
        | Load        | Load information from file
        | Time        | View actual date and time
        | Close       | Closes the address book"""
        print(welcome)
        while running:
            print(mainMenu)
            respond = input()
            running = self.__parse(respond)








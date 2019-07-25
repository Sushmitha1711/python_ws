from contact import contact

class contactBook:
    contacts=[]

    def addcontact():
        name=input("enter the name:")
        email=input("enter the email:")
        mobile=input("enter the mobile:")
        contactBook.contacts.append(contact(name,email,mobile))

    @staticmethod
    def searchcontact():
        name=input("enter the name to delete:")
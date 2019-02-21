class ContactList(list):
    def search(self,name):
        '''Return all contacts that contain the search value
        in their name'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contact = []
    def __init__(self,name,email):
        self.name = name
        self.email = email
        Contact.all_contact.append(self)

class Supplier(Contact):
    def order(self,order):
        print("If this were a real system we would send " "{} order to {}".format(order,self.name))

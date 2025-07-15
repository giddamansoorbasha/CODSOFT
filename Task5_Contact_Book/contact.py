class ContactBook:

    def __init__(self):
        self.contacts = {}

    def add(self):
        try:
            name = input("Enter The Name: ").strip().lower()
            while True:
                phone = input("Enter The Phone Number: ").strip()
                if not phone.isdigit():
                    print("Please, Enter Only Digits!")
                else:
                    break
            email = input("Enter The Email: ").strip()
            address = input("Enter The Address: ")
            self.contacts[name] = {"phone": phone,"email": email,"address": address}
            return "Added Successfully!"
        except Exception as e:
            print(f"Error : {e}")

    def search(self):
        try:
            name_or_phone = input("Enter The Name Or Phone: ").strip().lower()
            if name_or_phone.isdigit():
                for name,info in self.contacts.items():
                    if name_or_phone in info['phone']:
                        return (f"{name.title()} : {info}")
                return "Contact Not Found."
            elif name_or_phone in self.contacts:
                if name_or_phone in self.contacts.keys():
                    return f"{name_or_phone} : {self.contacts[name_or_phone]}"
            else:
                return "Contact Not Found."
        except Exception as e:
            print(f"Error : {e}")

    def update(self):
        try:
            choice = input("Want To Update Name/Phone/Email/Address: ").strip().lower()
            name = input("Enter The Name Of The Contact To Update: ").strip().lower()
            if name in self.contacts.keys():
                if choice == 'name':
                    new_name = input("Enter The New Name: ").strip().lower()
                    self.contacts[new_name] = self.contacts.pop(name)
                    return "Updated Successfully!"
                elif choice == 'phone':
                    new_phone = input("Enter The New Phone Number: ")
                    self.contacts[name]['phone'] = new_phone
                    return "Updated Successfully!"
                elif choice == 'email':
                    new_email = input("Enter The New Email: ")
                    self.contacts[name]['email'] = new_email
                    return "Updated Successfully!"
                elif choice == 'address':
                    new_address = input("Enter The New Address: ")
                    self.contacts[name]['address'] = new_address
                    return "Updated Successfully!"
                else:
                    print("Invalid Input!")
            else:
                return f"{name} Not Found In Contacts"
        except Exception as e:
            print(f"Error : {e}")
            
    def delete(self):
        try:
            name = input("Enter The Name Of The Contact To Delete: ").strip().lower()
            if name in self.contacts.keys():
                del_contact = self.contacts.pop(name)
                print("Deleted Successfully!")
                return name,del_contact
            else:
                return f"{name} Not Found In Contacts"
        except Exception as e:
            print(f"Error : {e}")

    def view(self):
        try:
            if not self.contacts:
                print("No contacts found.")
                return
            print("\n-----Contact List-----\n")
            for name,info in self.contacts.items():
                print(f"{name.title()} ---> {info['phone']}, {info['email']}, {info['address']}")
        except Exception as e:
            print(f"Error : {e}")

def main():
    try:
        book = ContactBook()
        while True:
            print("\n-----Welcome To ContactBook-----")
            choice = input("\n1) Add Contact\n2) Search Contact\n3) Update Contact\n4) Delete Contact\n5) View Contacts\n6) Exit\n\nEnter the Choice : ")
            if int(choice)==1:
                book.add()
            elif int(choice)==2:
                result = book.search()
                if result:
                    print(result)
            elif int(choice)==3:
                book.update()
            elif int(choice)==4:
                print(f"Deleted Contact : {book.delete()}")
            elif int(choice)==5:
                book.view()
            elif int(choice)==6:
                print("Thank You, Bye!")
                break
            else:
                print("Invalid Input")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

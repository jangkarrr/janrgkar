dictContactsJDD = {}  

def displayMenuJDD():
    print("\nContact Book")  
    print("1. Add a new contact")  
    print("2. View all contacts")  
    print("3. Update a contact's phone number")  
    print("4. Delete a contact")  
    print("5. Exit")  

def createContactJDD():
    strNameJDD = input("Enter contact name: ")  
    if strNameJDD in dictContactsJDD:  
        print("This contact already exists.")  
    else:
        strPhoneJDD = input("Enter phone number: ")  
        dictContactsJDD[strNameJDD] = strPhoneJDD  
        print(f"Contact '{strNameJDD}' added successfully.")  

def readContactsJDD():
    if not dictContactsJDD:  
        print("No contacts found.")  
    else:
        print("\nYour Contacts:")  
        for strNameJDD, strPhoneJDD in dictContactsJDD.items():
            print(f"Name: {strNameJDD}, Phone: {strPhoneJDD}")  

def updateContactJDD():
    strNameJDD = input("Enter the contact name to update: ")  
    if strNameJDD in dictContactsJDD:  
        strNewPhoneJDD = input(f"Enter new phone number for {strNameJDD}: ")  
        dictContactsJDD[strNameJDD] = strNewPhoneJDD  
        print(f"Phone number for '{strNameJDD}' updated successfully.")  
    else:
        print(f"Contact '{strNameJDD}' not found.")  

def deleteContactJDD():
    strNameJDD = input("Enter the contact name to delete: ")  
    if strNameJDD in dictContactsJDD:  
        del dictContactsJDD[strNameJDD]  
        print(f"Contact '{strNameJDD}' deleted successfully.")  
    else:
        print(f"Contact '{strNameJDD}' not found.")  

while True:
    displayMenuJDD()  
    choiceJDD = input("Enter your choice (1-5): ")  

    if choiceJDD == '1':
        createContactJDD()  
    elif choiceJDD == '2':
        readContactsJDD()  
    elif choiceJDD == '3':
        updateContactJDD()  
    elif choiceJDD == '4':
        deleteContactJDD()  
    elif choiceJDD == '5':
        print("Exiting Contact Book.")  
        break  
    else:
        print("Invalid choice. Please try again.")
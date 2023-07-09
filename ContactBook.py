#Dialpad using python

#import the libraries
import os
import csv
import datetime

#define a function for Title
def title():
    UpperLine = "---------------------------------"
    title = "Contact Management System"
    LowerLine = "----------------------------------"
    
    print(UpperLine.center(130))
    print(title.center(130))
    print(LowerLine.center(130))

#Create a class and define all the functions which we are using in if loop below
class contact_functions:
    contact_fields = ["Name","Number"]
    contact_database = "contact.csv"
    contact_data = [] #to store the temporary data.

    #defining create function 
    def create(self):
        os.system('cls')
        title()
        print("        create contact: ")
        print("        --------------")
        print("")

        for fields in self.contact_fields:
            contact_details = input("    Enter " + fields + ":")
            print("")
            self.contact_data.append(contact_details)

        #adding date and time
        Date = datetime.datetime.today()
        d = Date.strftime("%B %d %Y")
        self.contact_data.append(d)

        with open(self.contact_database,'a') as file:
            write = csv.writer(file)
            write.writerows([self.contact_data])

        self.contact_data = []
        print("")
        print("contact created..!!".center(128))


    #defining view function
    #writing view() function to see created contacts
    def view(self):
      os.system('cls')
      title()
      print("Contacts:".center(10))
      print("---------".center(10))
      print("")
      count = 0
      with open(self.contact_database, 'r') as file:
       read = csv.reader(file)
       for data1 in read:
         if len(data1) > 0:
            count = count + 1
       print("Total Contacts: ", count)
       print("")

      with open(self.contact_database, 'r') as file:
       read = csv.reader(file)
       if os.path.getsize(self.contact_database)==0: print("Contact Book is empty, Please create contacts".center(129))
       else:
         for fields in self.contact_fields:
            print('{0:<10}'.format(fields).center(10), end="\t\t")
         print('{0:<10}'.format("Date"))
         print('{:<10}\t\t{:<10}\t\t{:<10}'.format('----','---------','----'))
         print("")
         
         for data in read:
            
            for item in data:
                 print( '{:<10}'.format(item).center(10), end="\t\t")  
            print("")
      print("\n")
      input("\t Press enter key to continue..".center(120))
      os.system('cls')
      
    #Define Search() function
    def search(self):
        os.system('cls')
        title()

        print("Search Contacts: ".center(10))
        print("-----------------".center(10))
        print("")

        self.contact_match = 'false'
        search_value = input("Enter Name for Search: ")
        print("")

        for fields in self.contact_fields:
            print('{0:<10}'.format(fields).center(10),end = "\t\t")
        print('{0:<10}'.format("Date"))
        print('{:<10}\t\t{:<10}\t\t{:<10}'.format('-----','-----------','----'))    
        print("")

        with open(self.contact_database , 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if search_value == data[0]:
                        self.contact_match = 'true'
                        print('{:<10}\t\t{:<10}\t\t{:<10}'.format(data[0],data[1],data[2]).center(10))

        if self.contact_match == 'false':
            print("")
            print("No contact Found named " + search_value +" ".center(128))
        print("")   

    #Define Delete() function
    def delete(self) :
        os.system('cls')
        title()

        print("Delete Contacts: ".center(10))
        print("-----------------".center(10))
        print("")

        self.contact_match = 'false'
        delete_value = input("Enter Name : ")
        update_list = []

        with open(self.contact_database , 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if delete_value != data[0]:
                        update_list.append(data)
                    else:
                        self.contact_match = 'true'  

        if self.contact_match == 'true':
            with open(self.contact_database, 'w') as file:
                write = csv.writer(file)
                write.writerows(update_list)
                print("")
                print("contact is deleted successfully".center(128))
                print("")

        if self.contact_match == 'false':
            print("")
            print(" No contact found named " +delete_value)
            print("")
    
    
    #edit 
    def edit():
        os.system('cls')
        title()

        print("Edit Contacts: ".center(10))
        print("-----------------".center(10))
        print("")

        
#creating object of the class
contact_class = contact_functions()


#clear the console and creating a Menu page
os.system('cls')
title() 

while True:
    print("1. Search Contact".center(128))
    print("2. view all contacts".center(128))
    print("3. create new contact".center(128))
    print("4. Delete contact".center(128))
    print("5. Exit".center(128))
    print("--------------------------------".center(128))
    option = int(input("Choose your option : ".center(128)))




#Using if condition for perform specific operation by calling their function. 

    #call the search() function for search the contact.
    if option == 1:
        while True:
            contact_class.search()
            print("")
            ans = input("Do you want to Searchy Another contact?[Y/N]: ")

            if ans == 'y' or ans == 'Y':
                continue
            else :
                break

        os.system('cls')
        title()    
    
    #call the view() function for view the contact.
    if option == 2:
        
        contact_class.view()
        os.system('cls')
        title()
        

    #call the create() function  to craete a contact. 
    if option == 3:
        while True:
            contact_class.create()
            ans = input("Do you want to create Another contact?[Y/N]: ")

            if ans == 'y' or ans == 'Y':
                continue
            else :
                break

        os.system('cls')
        title()    


    #call the delete() function for delete the contact
    if option == 4:
        while True:
            contact_class.delete()
            ans = input("Do you want to Delete Another contact?[Y/N]: ")

            if ans == 'y' or ans == 'Y':
                continue
            else :
                break

        os.system('cls')
        title()
      

    if option == 5:
        os.system('cls')
        exit()
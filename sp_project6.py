# ==============================================================================
# Contacts Class Objects List
# PROJECT NUMBER: 6
# DUE DATE: Tuesday 12/05/2019
# PLATFORM: Windows OS / Python 3
# 
# SUMMARY
#
# Create a Contact class that can hold information and perform operations with
# contact objects.  The basic idea here is that on a mobile phone, you typically
# have a contacts list or address book. The Contact class must have the
# following private data members. Note that this table provides just the basic
# "word" names, you will have to use correct Python syntax to make these private
# members in your program.
# Demonstrate the class by writing an application for it using main and other
# functions. Note that your application will include functions other than main,
# which are not part of the class, but are needed to modularize your application. 
#
# INPUT
#
# The only input is from the data file. You may assume the file data is
# completely correct and you do not have to do any error checking on file
# contents. You may assume that the number of contacts specified in the file is
# an integer between 1 and 5.   
#
# OUTPUT
#
# As usual: introduction, echoprinted input, closing termination message,
# error messages as needed, and any informative messages the user may need
# or want to see.
# Elements described in this write-up
# Follow the course style guidelines 
#
# ASSUMPTIONS
#
# We assume that input data is valid and correctly entered.
# The program is guaranteed to work.
# ==============================================================================
class Contact:
    #method and also default outputs
    def __init__(self, name = "unavailable", address = "unavailable", phone = "unavailable", age = 0, types = "NONE"):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__age = age
        self.__types = types
        
    #setters for variables
    def set_name(self, name):
        set.__name = name

    def set_address(self, address):
        set.__address = address

    def set_phone(self, phone):
        set.__phone = phone

    def set_age(self, age):
        set.__age = age

    def set_types(self, types):
        set.__types = types
    
    #getters for variables
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_age(self):
        return self.__age
    
    def get_types(self):
        return self.types
    
    #Python language's standard usage private string
    def __str__(self):
        return_string = "Name: " + self.__name + "\n" + "Address: " + self.__address + "\n" +"Age: " + str(self.__age) + "\n" + "Phone: " + self.__phone + "\n" + "Relations: " + self.__types + "\n"
        return return_string

def main():
    #constant for file
    FILENAME = ("contacts.txt")
    
    my_list = []

    for i in range(0, 5):
        my_list.append(Contact())
        print (my_list[i])
        
    #reads file and has an error display message if file doesnt open
    file_found = False
    try:
        read_file = open(FILENAME, 'r')
        file_found = True
    except IOError:
        print("file not found")
    #if file does not open program ends
    if (file_found == False):
        exit()
        
    contactNum = int(read_file.readline().rstrip("\n"))
    #reads each variable line
    for i in range(0, contactNum):
        name = read_file.readline().rstrip("\n")
        address = read_file.readline().rstrip("\n")
        age = int(read_file.readline().rstrip("\n"))
        phone = read_file.readline().rstrip("\n")
        types = read_file.readline().rstrip("\n")
        my_list [i] = Contact(name, address, phone, age, types)
    #for loop for output
    for contact in my_list:
        if (contact.get_name() != "unavailable"):
            print(contact)
 

main()


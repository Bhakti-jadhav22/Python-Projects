import os
from pathlib import Path

# This function is used to show all existing files and folders under current directory
def readfileandfolder():
    path = Path('')   #it return the current directory to path variable
    items = list(path.rglob('*'))  #it returns the list of all the files and folders under the current directory to variable items
    for i , items in enumerate(items, start=1):  #enumerate is used to list the index number and items separately
        print(f"{i} : {items}")


# This function is used to Create a file
def createfile():
    try:
        readfileandfolder()
        name = input("Enter the file name which you want to create: ")
        p = Path(name) #to include created file in path 
        if not p.exists():
            f1 = open(p,'w')
            data = input("Write whatever you want to write in this file: ")
            f1.write(data)
            f1.close()
            print("File Created Successfully!!")
        else:
            print("This file already exists")

    except Exception as err:
        print(f"An erroe occured {err}")


# This function is used to Read a file
def readfile():
    try:
        readfileandfolder()
        name = input("Enter the file name which you want to read: ")
        p = Path(name) #to include created file in path 
        if p.exists() and p.is_file():
            f1 = open(p,'r')
            print(f1.read())
            f1.close()
        else:
            print("Entered file doesn't exist")
    
    except Exception as err:
        print(f"An arror occured {err}")


# This function is used to Update the file   
def updatefile():
    try:
        readfileandfolder()
        name = input("Enter the file name in which you want to make changes: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Enter 1 if you want change the name of the file")
            print("Enter 2 if you want to overwrite in file")
            print("Enter 3 if you want to append some content in file")

            response = int(input("Enter your choice: "))
            if response == 1:
                name1 = input("Enter the new name of the file: ")
                p1 = Path(name1)
                p.rename(p1)
            elif response == 2:
                with open(p,'w') as f1:   #Anothe way of opening a file no need to close the file for this syntax
                    data = input("Enter the data which you want to overwrite: ")
                    f1.write(data)
            elif response == 3:
                f1 = open(p,'a')
                data = input("Enter the data which you want to append: ")
                f1.write(" "+data) 
                f1.close()
            print("File Updated Successfully!!")
        else:
            print("Entered file doesn't exist")

    except Exception as err:
        print(f"An arror occured {err}")


# This function is used to Dalete the file
def deletefile():
    try:
        readfileandfolder()
        name = input("Enter the file name which you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File Deleted Successfully!!")
        else:
            print("Entered file doesn't exist")
    
    except Exception as err:
        print(f"An arror occured {err}")


print("Enter 1 for file creating")
print("Enter 2 for file reading")
print("Enter 3 for file updating")
print("Enter 4 for file deleting")

choice = int(input("Enter Your Choice: "))

if choice == 1:
    createfile()
elif choice == 2:
    readfile()
elif choice == 3:
    updatefile()
elif choice == 4:
    deletefile()
            


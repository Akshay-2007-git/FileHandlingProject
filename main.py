# CRUD Operation File-Handling Project 
from pathlib import Path

path=Path("mega_project-file")

def readfileandfolder():
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def createFile():
    readfileandfolder()
    try:
        name=input("Please tell your file name : ")
        p=path / name
        if not p.exists():
            with open(p,"w") as f:
                data=input("Write something in this file : ")
                f.write(data)

            print("FILE CREATED SUCCESSFULLY")
        else:
            print("File already exists")

    except Exception as e:
        print(f"An error occurred as {e}")   

def readfile():
    readfileandfolder()
    try: 
        name=input("Please tell your file name : ")
        p=path/name
        if p.exists() and p.is_file():
            with open(p) as f:
                print(f.read())
            print("FILE HAS BEEN READ SUCCESSFULLY")
        else:
            print("The file doesn't exist")

    except Exception as e:
        print(f"Any error occurred in the file as {e}")


def updatefile():
    readfileandfolder()
    try:
        name=input("Tell the file name to update the changes : ")
        p=path/name 
        if p.exists() and p.is_file():
            print("Press 1 for changing file name : ")
            print("Press 2 for overwriting the data : ")
            print("Press 3 to append the data into existing content  : ")
            res=int(input("Enter your choice : "))
            if res==1:
                name2=input("Enter the file name to be changed : ")
                p2=path/name2
                p.rename(p2)
                print("FILE NAME CHANGED SUCCESSFULLY")
            elif res==2:
                with open(p,"w") as f:
                    data=input("Write the data/content to be overwritten : ")
                    f.write(data)
                print("FILE CHANGES HAS BEEN UPDATED")
            elif res ==3:
                with open(p,"a") as f:
                    data=input("Write the data/content to be appended : ")
                    f.write(data)
                print("FILE CHANGES HAS BEEN UPDATED")                  
            else:
                print("Wrong option has been choosed")    
        else:
            print("File doesn't exist")               
    except Exception as e:
        print(f"An error occurred - {e}")

def deletefile():
    readfileandfolder()
    try:
        name=input("Enter the file name to delete it : ")
        p=path/name
        if p.exists() and p.is_file():
            p.unlink()
            print("FILE DELETED SUCCESSFULLY")
        else:
            print("File doesn't exists") 
    except Exception as e:
        print(f"An error occurred with {e}")           



print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")
check=int(input("Enter your choice : "))

if check==1:
    createFile()
elif check==2:
    readfile() 
elif check==3:
    updatefile()    
elif check==4:
    deletefile()
else:
    print("Wrong choice")           
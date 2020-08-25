from tkinter import *
import importlib
root = Tk()



def checkAdmin():
    if(inputAdminPass.get() == adminPass):
        Label(root, text="login successfull").grid(row=4)
        # login successfull
        # importlib.import_module(mainPage)
        # output existing table of key and value

    else:
        Label(root, text="Incorrect Password, Try Again").grid(row=4)




#admin system
#admin password
#two inputs to take key and value


#global variable
adminPass="dontkidyourselves"


# header of login page

description = Label(root, text="Welcome to Password Valut. You can manage and store all you passwords here safely.\n You just have to remember one password to rule them all!!")
description.grid(row=1)

#input feild
inputAdminPass=Entry(root, width=50)
inputAdminPass.grid(row=2)

# Login Button
loginButton=Button(root, text="Login", padx=50, command=checkAdmin)
loginButton.grid(row=3)



root.mainloop()
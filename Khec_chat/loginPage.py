
from tkinter import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector
import os
from tkinter import ttk, messagebox

# Creating object of tk class  
root = Tk()



def Authenticate():
    emailVal=emailid.get()
    print(emailVal)
    if emailVal=="Place your registered email...":
        msgLabel.config(text = "*email???",foreground = "Red",font=('Helveticabold',13))
    else:
        # print(emailVal)
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="",database="chatbot")
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT `id` FROM `new_user_regis` WHERE `email` = '{emailVal}'")
        if len(list(mycursor))!=0:
            #successful login
            root.destroy()
            os.system('python chatbot.py')
        else:
            # messagebox.showerror("Error", "Please enter valid email address.")
            # Displaying the success message
            msgLabel.config(text = "*This email is not registered yet.",foreground = "Red",font=('Helveticabold',13))

def Registration(*args):
    # print("Nepal")
    root.destroy()
    os.system('python emailValidate.py')


    # ID = list(mycursor)[0][0]
    # print(ID)
        
def removePlaceholderOfemailEntry(*args):
    emailEntry.delete(0, 'end')




# Setting the title, background color and disabling the resizing property
root.geometry("500x200")
root.title("Khec Login")
root.resizable(False, False)
root.config(background = "deepskyblue3")

emailid= StringVar()
emailLabel = Label(root, text="EMAIL-ID : ", bg="deepskyblue3",font=('Helveticabold',16))
emailLabel.grid(row=0, column=1, padx=5, pady=20)

emailEntry = Entry(root,textvariable=emailid, width=30,font=('Helveticabold',16),fg="#D2D2D2")
emailEntry.grid(row=0, column=2, padx=5, pady=5)
emailEntry.insert(0, 'Place your registered email...')

# Use bind method
emailEntry.bind("<Button-1>", removePlaceholderOfemailEntry)

msgLabel = Label(root, bg="deepskyblue3")   
msgLabel.place(x=50,y=50)

loginbutton = Button(root, text="Login", command=Authenticate, width=30,font=('Helveticabold',18),fg="white",bg="green")
loginbutton.place(x=60,y=100)
# loginbutton.grid(row=4, column=2, padx=5, pady=5)

# registerbutton =Button(root, text="Register", command=Registration, width=20,bg="deepskyblue3",foreground="red")
# registerbutton.pack()
# registerbutton.grid(row=5, column=2, padx=5, pady=5)
link = Label(root, text="Not yet Register?SignUP",font=('Helveticabold',13), fg="white", cursor="hand2", bg="deepskyblue3")
link.bind("<Button-1>",Registration)
link.place(x=180,y=150)

 
root.mainloop()


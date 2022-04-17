# Importing necessary packages
import random
import smtplib
from tkinter import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector
import os
from tkinter import ttk, messagebox




def Authenticate():
    global root
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

# def Registration(*args):
#     # print("Nepal")
#     global root
#     root.destroy()
#     os.system('python emailValidate.py')


    # ID = list(mycursor)[0][0]
    # print(ID)
        
def removePlaceholderOfemailEntry(*args):
    # global root
    emailEntry.delete(0, 'end')






def login(*args):
    global root
    global regis
    regis=Tk()
    regis.destroy()
    global main_screen
    main_screen = Tk()
    # root = Toplevel(main_screen)
    main_screen.destroy()
    
    # delete_mainscreen()

    
    # Creating object of tk class  
    root = Tk()

    # Setting the title, background color and disabling the resizing property
    root.geometry("500x200")
    root.title("Khec Login")
    root.resizable(False, False)
    root.config(background = "deepskyblue3")

    emailid = StringVar()
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
    link.bind("<Button-1>",register)
    link.place(x=180,y=150)
    root.mainloop()
  


 ################################  Registration  ######################################## 
# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidget():
    global Email
    global regis
    global email_name
    # Creating tkinter variables
    email_name = StringVar()
    otp = StringVar()

    emailLabel = Label(regis, text="ENTER YOUR EMAIL-ID : ", bg="deepskyblue3")
    emailLabel.grid(row=0, column=1, padx=5, pady=5)

    emailEntry = Entry(regis, textvariable=email_name, width=30)
    emailEntry.grid(row=0, column=2, padx=5, pady=5)

    sendOTPbutton = Button(regis, text="Send OTP", command=sendOTP, width=20)
    sendOTPbutton.grid(row=0, column=3, padx=5, pady=5)

    regis.msgLabel = Label(regis, bg="deepskyblue3")
    regis.msgLabel.grid(row=1, column=1, padx=5, pady=5, columnspan=3)

    otpLabel = Label(regis, text="ENTER THE OTP : ", bg="deepskyblue3")
    otpLabel.grid(row=2, column=1, padx=5, pady=5)

    regis.otpEntry = Entry(regis, textvariable=otp, width=30, show="*")
    regis.otpEntry.grid(row=2, column=2, padx=5, pady=5)

    validOTPbutton = Button(regis, text="Validate OTP", command=validOTP, width=20)
    validOTPbutton.grid(row=2, column=3, padx=5, pady=5)

    regis.otpLabel = Label(regis, bg="deepskyblue3")
    regis.otpLabel.grid(row=3, column=1, padx=5, pady=5, columnspan=3)
    link = Label(regis, text="Already have account?Login",font=('Helveticabold',13), fg="red", cursor="hand2", bg="deepskyblue3")
    link.bind("<Button-1>",login)
    link.place(x=80,y=130)


# Defining sendOTP() to generate and send OTP to user-input email-id
def sendOTP():
    global regis
    global Email
    global email_name
    # Storing digits from 0 to 9 as string in numbers variable & declaring empty string
    # variable named root.genOTP
    numbers = "0123456789"
    regis.genOTP = ""
    # Fetching and storing user-input mail id in receiverEmail variable
    receiverEmail = email_name.get()
    Email=receiverEmail

    # Generating 6-digits OTP
    for i in range(6):
        regis.genOTP += numbers[int(random.random() * 10)]
    # Concatenating and Storing generated OTP with Message to be sent in otpMSG
    otpMSG = "YOUR OTP IS : " + regis.genOTP

    # Creating instance of class MIMEMultipart()
    message = MIMEMultipart()
    # Storing the email details in respective fields
    message['FROM'] = "OTP VALIDATOR (python_scripts)"
    message['To'] = receiverEmail
    message['Subject'] = "OTP VALIDATION"
    # Attaching the otgMSG with MIME instance
    message.attach(MIMEText(otpMSG))

  # Creating a smtp session
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # Starting TLS for security
    smtp.starttls()
    # Authenticating the sender using the login() method
    smtp.login("omitbajracharya55@gmail.com", "khec_chatbot")
    # Sending the email with Mulitpart message converted into string
    smtp.sendmail("omitbajracharya55@gmail.com", receiverEmail, message.as_string())
    # Terminating the session
    smtp.quit()

    # Formatting receiveEmail to replace(hide) mail id with *
    receiverEmail = '{}********{}'.format(receiverEmail[0:2], receiverEmail[-10:])
    # Displaying the success message
    regis.msgLabel.config(text = "OTP HAS BEEN SENT TO " + receiverEmail)

# Defining validOTP() to validate user-input OTP mail with script generated OTP
def validOTP():
    global regis
    global email_name
    global Email
    global ID
    # Storing user-input OTP
    userInputOTP = otp.get()
    # Storing system generated OTP
    systemOTP = regis.genOTP

    # Validating OTP
    if userInputOTP == systemOTP:
        regis.otpLabel.config(text="OTP VALIDATED SUCCESSFULLY")
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="",database="chatbot")
        mycursor = mydb.cursor()
        mycursor.execute(f"INSERT INTO `new_user_regis`(`email`) VALUES ('{Email}')")
        mydb.commit()
        # mycursor.execute(f"SELECT `id` FROM `new_user_regis` WHERE `email` = 'riyabudhathoki2@gmail.com'")
        # ID = list(mycursor)[0][0]
        # print(ID)
       # db....
        #user->id,email,status
        #login...
        #enter your email....email->status---your are block....no email ->register...select-email with status 1->welcome....chatpage
    else:
        regis.otpLabel.config(text="*INVALID OTP",fg="red")

def register(*args):
    global root
    global regis
    root.destroy()
    regis = Tk()
    # Setting the title, background color and disabling the resizing property
    regis.geometry("500x160")
    regis.title("Khec Validation")
    regis.resizable(False, False)
    regis.config(background = "deepskyblue3")

    # Calling the CreateWidgets() function with argument bgColor
    CreateWidget()

    # Defining infinite loop to run application
    regis.mainloop()


######################################   Registration code upto here...   ####################################





# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=login).pack()
 
    main_screen.mainloop()

 ############################################################################
def delete_mainscreen():
    global main_screen
    main_screen.destroy()
 # ################################################################################### 
main_account_screen() 

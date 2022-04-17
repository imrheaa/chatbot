import random
import json
from numpy.lib.function_base import gradient
import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize, stem

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "khec_Bot"

#Creating GUI with tkinter
import tkinter
from tkinter import *

def send(*args):
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    
    # sentence = input("You: ")
    sentence = tokenize(msg)

    #------------------------------Stemming
    # ignore_words = ['?', '.', '!',',','@','#','$','&','(',')','?','<','>','%','-','_','/']
    # all_words = [stem(w) for w in sentence if w not in ignore_words]
    # # remove duplicates and sort
    # #sentence  = sorted(set(sentence ))  #remove the duplicate words
            
    #-----------------------------
    X = bag_of_words(sentence, all_words)
    print(type(X))
    X = X.reshape(1, X.shape[0])   #1=row and 0 for column  [1,0,1,0,..]
    print("",X)
    X = torch.from_numpy(X).to(device)
    print(X)
    output = model(X)
    print(output)
    _, predicted = torch.max(output, dim=1)
    print(predicted)
    tag = tags[predicted.item()]
            
    

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.90:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(tag,prob.item())
                response = random.choice(intent['responses'])
                # print(f"{bot_name}: {response}")
    else:
        response = "Hey, I'm only a bot, I need things simple.Could you please place query more detailly or Exclude slang words?,Thank you"
        # print(f"{bot_name}: I do not understand...")
        import mysql.connector
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="",database="chatbot_query")

        mycursor = mydb.cursor()
        # newquery= "red panda"
        query = f"INSERT INTO new_query (Query)  VALUES ('{msg}')"
  
        mycursor.execute(query)
        mydb.commit()
        mydb.close()

    # _______________***************************_________________
    
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="white", font=("Times New Roman", 12 ))
        # ChatLog.place(x=40,y=100)
        res = response
        ChatLog.insert(END, "khecBot : " + res  + '\n\n')
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

base = Tk()
base.title(bot_name)
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="#000000", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Create the box to enter message
EntryBox = Text(base,bg="#ADD8E6",bd=0,width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=6, y=400, height=50, width=370)
SendButton.place(x=6, y=460, height=30, width=370)
base.bind('<Return>', send)   #if enter key is pressed call function
base.mainloop()
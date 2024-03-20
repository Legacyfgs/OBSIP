from tkinter import *
import openai
import socket
import threading


# My OpenAI API key here
api_key = "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"
openai.api_key = api_key

# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function
def send():
    user_input = e.get()
    send_message("You", user_input)

    response = get_ai_response(user_input)
    send_message("Bot", response)

    e.delete(0, END)

def send_message(sender, message):
    formatted_message = f"{sender} -> {message}"
    txt.insert(END, "\n" + formatted_message)

def get_ai_response(user_input):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ],
        max_tokens=50
    )
    return response["choices"][0]["message"]["content"]



# Send function
def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
 
    user = e.get().lower()
 
    if (user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")
 
    elif (user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")
 
    elif (user == "how are you"):
        txt.insert(END, "\n" + "Bot -> fine! and you")
 
    elif (user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "\n" + "Bot -> Great! how can I help you.")
 
    elif (user == "thanks" or user == "thank you" or user == "now its my time"):
        txt.insert(END, "\n" + "Bot -> My pleasure !")
 
    elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
        txt.insert(END, "\n" + "Bot -> We have coffee and tea")
 
    elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
        txt.insert(
            END, "\n" + "Bot -> What did the buffalo say when his son left for college? Legacy.! ")
 
    elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
        txt.insert(END, "\n" + "Bot -> Have a nice day!")
 
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")
 
    e.delete(0, END)
def generate_response(user_input):
    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=user_input,
        max_tokens=50
    )
    return response.choices[0].text.strip()

lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=send).grid(row=2, column=1)

root.mainloop()



# Choose a port that is free
PORT = 5000
 
# An IPv4 address is obtained
# for the server.
SERVER = socket.gethostbyname(socket.gethostname())
 
# Address is stored as a tuple
ADDRESS = (SERVER, PORT)
 
# the format in which encoding
# and decoding will occur
FORMAT = "utf-8"
 
# Lists that will contains
# all the clients connected to
# the server and their names.
clients, names = [], []
 
# Create a new socket for
# the server
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)
 
# bind the address of the
# server to the socket
server.bind(ADDRESS)
 
# function to start the connection
 
 
def startChat():

    print("server is working on " + SERVER)
 
    # listening for connections
    server.listen()
 
    while True:
 
        # accept connections and returns
        # a new connection to the client
        #  and  the address bound to it
        conn, addr = server.accept()
        conn.send("NAME".encode(FORMAT))
 
        # 1024 represents the max amount
        # of data that can be received (bytes)
        name = conn.recv(1024).decode(FORMAT)
 
        # append the name and client
        # to the respective list
        names.append(name)
        clients.append(conn)
 
        print(f"Name is :{name}")
 
        # broadcast message
        broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))
 
        conn.send('Connection successful!'.encode(FORMAT))
 
        # Start the handling thread
        thread = threading.Thread(target=handle,
                                  args=(conn, addr))
        thread.start()
 
        # no. of clients connected
        # to the server
        print(f"active connections {threading.activeCount()-1}")
 
# method to handle the
# incoming messages
 
 
def handle(conn, addr):
 
    print(f"new connection {addr}")
    connected = True
 
    while connected:
          # receive message
        message = conn.recv(1024)
 
        # broadcast message
        broadcastMessage(message)
 
    # close the connection
    conn.close()
 
# method for broadcasting
# messages to the each clients
 
 
def broadcastMessage(message):
    for client in clients:
        client.send(message)
 
 
# call the method to
# begin the communication
startChat()
from tkinter import *
from web3 import Web3, HTTPProvider

def log_unlock():
    T.configure(state='normal')

def log_lock():
    T.configure(state="disabled")

def log_clear():
    T.configure(state="normal")
    T.delete('1.0', END)
    T.configure(state="disabled")

def log(text):
    T.configure(state='normal')
    T.insert(END, text + "\n")
    T.configure(state="disabled")

def connectToChain():
    try:
        web = Web3(HTTPProvider(url.get()+":"+port.get()))

        if web.eth.coinbase!=None:
            connectButton["text"]="Connected"
            log("----------------------------------------------")
            log("Connected, Coinbase Address:"+web.eth.coinbase)
            log("----------------------------------------------")

             # root.geometry(root.winfo_screenwidth()+"x500")


    except:
        connectButton["text"] = "Error"
        log("Connection Refused on:"+ url.get()+":"+port.get())
        root.geometry("518x28")



#Root Window
root = Tk()
root.title("'Viper For ETH' - by TestPilot")

topframe = Frame(root)
topframe.pack(fill=X)

url = Entry(topframe)
url.insert(0,"http://")
port= Entry(topframe)

url_Label= Label(topframe, text="URL:")
port_Label= Label(topframe, text="Port:")

url_Label.grid(row=0, column=0, sticky=EW)
url.grid(row=0, column=1, sticky=EW)
port_Label.grid(row=0, column=2, sticky=EW)
port.grid(row=0, column=3, sticky=EW)
connectButton = Button(topframe, text="Connect",command=connectToChain)
connectButton.grid(row=0, column=4, sticky=EW)

#Log Window
log_root = Tk()
log_root.title("Log Window")

logtopframe = Frame(log_root)
logtopframe.pack(fill=X)
logLockButton = Button(logtopframe,text="Lock",command=log_lock)
logUnlockButton = Button(logtopframe,text="Unlock",command=log_unlock)
logClearButton = Button(logtopframe,text="Clear Log",command=log_clear)

logLockButton.pack(side=LEFT)
logUnlockButton.pack(side=LEFT)
logClearButton.pack(side=LEFT)

S = Scrollbar(log_root)
T = Text(log_root, height=4, width=100)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.configure(state="disabled")



root.mainloop()
log_root.mainloop()
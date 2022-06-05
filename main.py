from tkinter import *
import socket
from tkinter import messagebox
from tkinter import filedialog
import os


screen = Tk()
screen.title("FetchIT")
screen.geometry("450x560")
screen.configure(bg="#f4fdfe")
screen.resizable(False, False)


def fsend():
    window = Toplevel(screen)
    window.title("Send File")
    window.geometry("450x560")
    window.configure(bg= "#f4fdfe")
    window.resizable(False, False)

    def fileSelect():
        global filename
        filename = filedialog.askopenfilename(initialdir = os.getcwd(), title= "Select Image File", filetype= (('file_type','*.txt'),('all files','*.*')))
        file_explorer.configure(text=filename)

    def socketSend():
        s = socket.socket()
        host = socket.gethostname()
        port= 8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print(filename)
        print("Waiting for incoming connections....")
        conn, addr = s.accept()
        file=open(filename, 'rb')
        file_data = file.read(1024)
        conn.send(file_data)
        print("Data has been transferred successfully.....")

    icon1 = PhotoImage(file = "send.png")
    window.iconphoto(False, icon1)

    background1 = PhotoImage(file = "sender.png")
    Label(window, image = background1).place(x=-2, y = 0)

    background2 = PhotoImage(file = "id.png")
    Label(window, image = background2, bg="#f4fdfe").place(x=100, y = 260)

    host = socket.gethostname()
    Label(window, text=f'ID: {host}', bg="white", fg="black").place(x=165, y = 295)
    
    file_explorer = Label(window, width=30, height=2, font="Robote 10", bg="#fff", fg="#000", wraplength=200)
    file_explorer.place(x=160 , y=90)
    Button(window, text="+ Select File", width= 10, height=1, font="arial 14 bold", bg="#fff", fg="#000", command=fileSelect).place(x=160,y=150)
    Button(window, text="SEND", width= 8, height=1, font="arial 14 bold", fg="#fff", bg="#000", command=socketSend).place(x=300,y= 150)

    window.mainloop()

def freceive():
    window1 = Toplevel(screen)
    window1.title("Receive File")
    window1.geometry("450x560")
    window1.configure(bg="#f4fdfe")
    window1.resizable(False, False)

    def receiver():
        ID = senderId.get()
        filename1 = incoming_filename.get()
        if ID != "" and filename1 != "":
            s = socket.socket()
            port = 8080
            s.connect((ID, port))
            file1 = open(filename1, 'wb')
            file_data = s.recv(1024)
            file1.write(file_data)
            file1.close()
            print("File received successfully..")
        elif filename1 == "" or ID == "":
            messagebox.showerror("Receiver","Input Filename/Sender ID")
    
    icon2 = PhotoImage(file = 'receive.png')
    window1.iconphoto(False, icon2)

    background1 = PhotoImage(file = "receiver.png")
    Label(window1, image=background1).place(x= -2, y= 0)

    logo = PhotoImage(file = "profile.png")
    Label(window1, image= logo, bg="#f4fdfe").place(x=100, y=250)

    Label(window1, text="Receive", font = ("arial", 20),bg="#f4fdfe").place(x=100, y =280)
    Label(window1, text= "Input Sender ID:", font=("arial",10,"bold"), bg="#f4fdfe").place(x= 20, y= 340)
    senderId = Entry(window1, width=20, fg="black", border=2, bg="white",font=("arial", 15))
    senderId.place(x= 20, y=370)
    senderId.focus()

    Label(window1, text= "Input Filename:", font=("arial",10,"bold"), bg="#f4fdfe").place(x= 20, y= 420)
    incoming_filename = Entry(window1, width=20, fg="black", border=2, bg="white",font=("arial", 15))
    incoming_filename.place(x= 20, y=450)   
    
    imageicon = PhotoImage(file= "arrow.png")
    ic = Button(window1, text = "Receive", compound= LEFT, image=imageicon, width=130,bg="#39c790", font="arial 14 bold",command= receiver )
    ic.place(x = 20, y = 500)
    window1.mainloop()

image = PhotoImage(file= "download.png")
screen.iconphoto(False, image)

Label(screen, text="FILE TRANSFER APPLICATION", font=("Robote 10", 18, 'bold'), bg="#f4fdfe").place(x = 40, y=20)

Frame(screen, width= 400, height= 3, bg= "black").place(x= 25, y = 50)
#dp = PhotoImage(file = "dp.png")
#l1 = Label(screen, image=dp, width=30, height= 20)
#l1.place(x=260, y =60)  
Button(screen, text= "Register", width=12,height=1,font="arial 14 bold", fg= "black", bg= "white").place(x=250, y= 60)

s_image = PhotoImage(file = "send.png")
send = Button(screen, image= s_image, bg= "#f4fdfe", bd= 0, command= fsend)
send.place(x = 70, y= 130)

r_image = PhotoImage(file = "receive.png")
receive = Button(screen, image= r_image, bg= "#f4fdfe", bd= 0, command= freceive)
receive.place(x = 280, y= 130)

Label(screen, text= "Send", font=("Arial",17, "bold"), bg ="#fefdfe").place(x = 85, y = 240)
Label(screen, text= "Receive", font=("Arial",17, "bold"), bg ="#fefdfe").place(x = 280, y = 240)

background = PhotoImage(file = "background.png")
Label(screen, image=background).place(x= -2, y = 323)

screen.mainloop()
from tkinter import*
import tkinter.messagebox

root=Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(background="Cadet Blue")

tops=Frame(root,bg="Cadet Blue",pady=2,width=1350,height=100,relief=RIDGE)
tops.grid(row=0,column=0)

lab=Label(tops,font=('arial',50,"bold"),text="TIC TAC TOE",justify=CENTER,bd=12,bg="Cadet Blue",fg="black")
lab.pack(fill=X)

mainframe=Frame(root,bg="Powder Blue",bd=10,width=1365,height=600,relief=RIDGE)
mainframe.grid(row=1,column=0)

leftframe=Frame(mainframe,bd=10,width=750,height=550,pady=2,padx=10,bg="Cadet Blue",relief=RIDGE)
leftframe.pack(side=LEFT)

rightframe=Frame(mainframe,bd=0,width=560,height=550,pady=2,padx=10,bg="Powder Blue",relief=RIDGE)
rightframe.pack(side=RIGHT)

rightframe1=Frame(rightframe,bd=10,width=580,height=200,pady=2,padx=10,bg="Cadet Blue",relief=RIDGE)
rightframe1.grid(row=0,column=0)

rightframe2=Frame(rightframe,bd=10,width=580,height=200,pady=2,padx=10,bg="Cadet Blue",relief=RIDGE)
rightframe2.grid(row=1,column=0)

PlayerX=IntVar()
PlayerY=IntVar()

PlayerX.set(0)
PlayerY.set(0)

button=StringVar()
click=True
 #functions
def checker(buttons):
    global click
    if buttons["text"]==" " and click==True:
        buttons["text"]="X"
        click = False
        score()
    elif buttons["text"] == " " and click ==False :
        buttons["text"]="O"
        click = True
        score()
        
def score():
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        button1.configure(background="red")
        button2.configure(background="red")
        button3.configure(background="red")
        n=float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("WINNER X","You have won the game")
        
    if(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        button4.configure(background="red")
        button5.configure(background="red")
        button6.configure(background="red")
        n=float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("WINNER X","You have won the game")

    if(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        button7.configure(background="red")
        button8.configure(background="red")
        button9.configure(background="red")
        n=float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("WINNER X","You have won the game")

    if(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        button3.configure(background="red")
        button5.configure(background="red")
        button7.configure(background="red")
        n=float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("WINNER X","You have won the game")
        
    if(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        button1.configure(background="red")
        button5.configure(background="red")
        button9.configure(background="red")
        n=float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("WINNER X","You have won the game")
        
    if(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        button1.configure(background="red")
        button4.configure(background="red")
        button7.configure(background="red")
        n=float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("WINNER X","You have won the game")

    if(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        button3.configure(background="red")
        button6.configure(background="red")
        button9.configure(background="red")
        n=float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("WINNER X","You have won the game")

    if(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        button2.configure(background="red")
        button5.configure(background="red")
        button8.configure(background="red")
        n=float(PlayerX.get())
        score=(n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("WINNER X","You have won the game")
# winner O
    if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        button1.configure(background="red")
        button2.configure(background="red")
        button3.configure(background="red")
        n=float(PlayerY.get())
        score=(n+1)
        PlayerY.set(score)
        tkinter.messagebox.showinfo("WINNER Y","You have won the game")
        

    if(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
        button4.configure(background="red")
        button5.configure(background="red")
        button6.configure(background="red")
        n=float(PlayerY.get())
        score=(n+1)
        PlayerY.set(score)
        tkinter.messagebox.showinfo("WINNER Y","You have won the game")

    if(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
        button7.configure(background="red")
        button8.configure(background="red")
        button9.configure(background="red")
        n=float(PlayerY.get())
        score=(n+1)
        PlayerY.set(score)
        tkinter.messagebox.showinfo("WINNER Y","You have won the game")

    if(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        button3.configure(background="red")
        button5.configure(background="red")
        button7.configure(background="red")
        n=float(PlayerY.get())
        score=(n+1)
        PlayerY.set(score)
        tkinter.messagebox.showinfo("WINNER Y","You have won the game")

    if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        button1.configure(background="red")
        button5.configure(background="red")
        button9.configure(background="red")
        n=float(PlayerY.get())
        score=(n+1)
        PlayerY.set(score)
        tkinter.messagebox.showinfo("WINNER Y","You have won the game")
        
    if(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        button1.configure(background="red")
        button4.configure(background="red")
        button7.configure(background="red")
        n=float(PlayerY.get())
        score=(n+1)
        PlayerY.set(score)
        tkinter.messagebox.showinfo("WINNER Y","You have won the game")

    if(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        button3.configure(background="red")
        button6.configure(background="red")
        button9.configure(background="red")
        n=float(PlayerY.get())
        score=(n+1)
        PlayerY.set(score)
        tkinter.messagebox.showinfo("WINNER Y","You have won the game")

    if(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
        button2.configure(background="red")
        button5.configure(background="red")
        button8.configure(background="red")
        n=float(PlayerY.get())
        score=(n+1)
        PlayerY.set(score)
        tkinter.messagebox.showinfo("WINNER Y","You have won the game")
    
    
    
def reset():
    button1.configure(background="gainsboro")
    button2.configure(background="gainsboro")
    button3.configure(background="gainsboro")
    button4.configure(background="gainsboro")
    button5.configure(background="gainsboro")
    button6.configure(background="gainsboro")
    button7.configure(background="gainsboro")
    button8.configure(background="gainsboro")
    button9.configure(background="gainsboro")
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" "
    
def new():
    reset()
    PlayerX.set(0)
    PlayerY.set(0)


playerX=Label(rightframe1,font=('arial',30,'bold'),text="Player X: ",padx=2,pady=2,bg="Cadet Blue")
playerX.place(x=0,y=10)
txtPlayerX=Entry(rightframe1,font=('arial',30,'bold'),bd=2,fg="black",textvariable=PlayerX,width=12,justify=LEFT,state="readonly")
txtPlayerX.place(x=200,y=10)

playerY=Label(rightframe1,font=('arial',30,'bold'),text="Player Y: ",padx=2,pady=2,bg="Cadet Blue")
playerY.place(x=0,y=100)
txtPlayerY=Entry(rightframe1,font=('arial',30,'bold'),bd=2,fg="black",textvariable=PlayerY,width=12,justify=LEFT,state="readonly")
txtPlayerY.place(x=200,y=100)

btnReset=Button(rightframe2,text="Reset",font=('Times 26 bold'),height=1,width=10,bg="gainsboro",justify=RIGHT,command=lambda:reset())
btnReset.place(x=0,y=10)

btnnew=Button(rightframe2,text="New Game",font=('Times 26 bold'),height=1,width=10,bg="gainsboro",justify=RIGHT,command=lambda:new())
btnnew.place(x=0,y=100)

# buttons of game 
button1=Button(leftframe,text=" ",font=('Times New Roman',26,"bold"),height=3,width=11,bg="gainsboro",relief=GROOVE,command=lambda:checker(button1))
button1.place(x=0,y=2)

button2=Button(leftframe,text=" ",font=('Times New Roman',26,"bold"),height=3,width=11,bg="gainsboro",relief=GROOVE,command=lambda:checker(button2))
button2.place(x=250,y=2)

button3=Button(leftframe,text=" ",font=('Times New Roman',26,"bold"),height=3,width=10,bg="gainsboro",relief=GROOVE,command=lambda:checker(button3))
button3.place(x=500,y=2)

button4=Button(leftframe,text=" ",font=('Times New Roman',26,"bold"),height=3,width=11,bg="gainsboro",relief=GROOVE,command=lambda:checker(button4))
button4.place(x=0,y=170)

button5=Button(leftframe,text=" ",font=('Times New Roman',26,"bold"),height=3,width=11,bg="gainsboro",relief=GROOVE,command=lambda:checker(button5))
button5.place(x=250,y=170)

button6=Button(leftframe,text=" ",font=('Times New Roman',26,"bold"),height=3,width=10,bg="gainsboro",relief=GROOVE,command=lambda:checker(button6))
button6.place(x=500,y=170)

button7=Button(leftframe,text=" ",font=('Times New Roman',26,"bold"),height=3,width=11,bg="gainsboro",relief=GROOVE,command=lambda:checker(button7))
button7.place(x=0,y=350)

button8=Button(leftframe,text=" ",font=('Times New Roman',26,"bold"),height=3,width=11,bg="gainsboro",relief=GROOVE,command=lambda:checker(button8))
button8.place(x=250,y=350)

button9=Button(leftframe,text=" ",font=('Times New Roman',26,"bold"),height=3,width=10,bg="gainsboro",relief=GROOVE,command=lambda:checker(button9))
button9.place(x=500,y=350)




root.mainloop()

# importing all necessary libraries
import tkinter
from tkinter import *
from functools import partial
import tkinter.messagebox
from PIL import ImageTk,Image

click = True
count = 0

def menu():
# gui design
    root = Tk()
    root.geometry("500x450")
    root.title('ERovoutika - Tic Tac Toe')
    root.iconbitmap("gear.ico")
    root.config(bg ='lightsteelblue1')
    root.resizable(0,0)
    game = partial(tictactoe, root)
# erovoutika logo
    img = ImageTk.PhotoImage(Image.open("erov logo.png"))
    img_label = Label(image=img, bg='lightsteelblue1')
    img_label.pack()
    Label(root, font ='{courier new} 30', text = 'Tic Tac Toe', fg = 'black' ,bg ='lightsteelblue1').pack(side = TOP , pady = 5)
    btnPlay = Button(root, font ='{courier new} 30', text='Play', bd='5', width= 200,
             command= game)
    btnPlay.pack(side=TOP, padx=50, pady= 50)
    root.mainloop()

def tictactoe(ttt):
    ttt.destroy()

    ttt = Tk()

    ttt.iconbitmap('gear.ico')

    ttt.title('ERovoutika - Tic Tac Toe')

    ttt.resizable(False,False)

    btn1 = StringVar()
    btn2 = StringVar()
    btn3 = StringVar()
    btn4 = StringVar()
    btn5 = StringVar()
    btn6 = StringVar()
    btn7 = StringVar()
    btn8 = StringVar()
    btn9 = StringVar()

    xPhoto = PhotoImage(file = 'wrenchX.png')
    oPhoto = PhotoImage(file = 'gearO.png')

    def play():
        button1 = Button(ttt,height=9,width=19,bd=.5,relief = 'ridge',bg = 'lightsteelblue1',textvariable = btn1,
                         command=lambda: press(1,0,0)) 
        button1.grid(row=0,column=0)

        button2 = Button(ttt,height=9,width=19,bd = .5,relief = 'ridge',bg = 'lightsteelblue1',textvariable = btn2,
                         command=lambda: press(2,0,1))
        button2.grid(row=0,column=1)

        button3 = Button(ttt,height=9,width=19,bd = .5,relief = 'ridge',bg = 'lightsteelblue1',textvariable = btn3,
                         command=lambda: press(3,0,2))
        button3.grid(row=0,column=2)

        button4 = Button(ttt,height=9,width=19,bd = .5,relief = 'ridge',bg = 'lightsteelblue2',textvariable = btn4,
                         command=lambda: press(4,1,0))
        button4.grid(row=1,column=0)

        button5 = Button(ttt,height=9,width=19,bd = .5,relief = 'ridge',bg = 'lightsteelblue2',textvariable = btn5,
                        command=lambda: press(5,1,1))
        button5.grid(row=1,column=1)

        button6 = Button(ttt,height=9,width=19,bd = .5,relief = 'ridge',bg = 'lightsteelblue2',textvariable = btn6,
                        command=lambda: press(6,1,2))
        button6.grid(row=1,column=2)

        button7 = Button(ttt,height=9,width=19,bd = .5,relief = 'ridge',bg = 'lightsteelblue3',textvariable = btn7,
                        command=lambda: press(7,2,0))
        button7.grid(row=2,column=0)

        button8 = Button(ttt,height=9,width=19,bd = .5,relief = 'ridge',bg = 'lightsteelblue3',textvariable = btn8,
                        command=lambda: press(8,2,1))
        button8.grid(row=2,column=1)

        button9 = Button(ttt,height=9,width=19,bd = .5,relief = 'ridge',bg = 'lightsteelblue3',textvariable = btn9,
                        command=lambda: press(9,2,2))
        button9.grid(row=2,column=2)

    def press(num,r,c):
        global click,count
        if click == True:
            labelPhoto = Label(ttt,image = xPhoto, bg='lightsteelblue1')
            labelPhoto.grid(row=r,column=c)
            if num == 1:
                btn1.set('X')
            elif num == 2:
                btn2.set('X')
            elif num == 3:
                btn3.set('X')
            elif num == 4:
                btn4.set('X')
            elif num == 5:
                btn5.set('X')
            elif num == 6:
                btn6.set('X')
            elif num == 7:
                btn7.set('X')
            elif num == 8:
                btn8.set('X')
            else:
                btn9.set('X')
            count += 1
            click = False
            checkWin()
        
        else:
            labelPhoto = Label(ttt,image = oPhoto, bg='lightsteelblue1')
            labelPhoto.grid(row=r,column=c)
            if num == 1:
                btn1.set('O')
            elif num == 2:
                btn2.set('O')
            elif num == 3:
                btn3.set('O')
            elif num == 4:
                btn4.set('O')
            elif num == 5:
                btn5.set('O')
            elif num == 6:
                btn6.set('O')
            elif num == 7:
                btn7.set('O')
            elif num == 8:
                btn8.set('O')
            else:
                btn9.set('O')
            count += 1
            click = True
            checkWin()
       
        
    def checkWin():
        global count,click
    
        if (btn1.get() == 'X' and btn2.get() == 'X' and btn3.get() == 'X' or
            btn4.get() == 'X' and btn5.get() == 'X' and btn6.get() == 'X' or
            btn7.get() == 'X' and btn8.get() == 'X' and btn9.get() == 'X' or
            btn1.get() == 'X' and btn4.get() == 'X' and btn7.get() == 'X' or
            btn2.get() == 'X' and btn5.get() == 'X' and btn8.get() == 'X' or
            btn3.get() == 'X' and btn6.get() == 'X' and btn9.get() == 'X' or
            btn1.get() == 'X' and btn5.get() == 'X' and btn9.get() == 'X' or
            btn3.get() == 'X' and btn5.get() == 'X' and btn7.get() == 'X'):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", 'X Wins !')
            click = True
            count = 0
            clear()
            play()
        
        elif (btn1.get() == 'O' and btn2.get() == 'O' and btn3.get() == 'O' or
            btn4.get() == 'O' and btn5.get() == 'O' and btn6.get() == 'O' or
            btn7.get() == 'O' and btn8.get() == 'O' and btn9.get() == 'O' or
            btn1.get() == 'O' and btn4.get() == 'O' and btn7.get() == 'O' or
            btn2.get() == 'O' and btn5.get() == 'O' and btn8.get() == 'O' or
            btn3.get() == 'O' and btn6.get() == 'O' and btn9.get() == 'O' or
            btn1.get() == 'O' and btn5.get() == 'O' and btn9.get() == 'O' or
            btn3.get() == 'O' and btn5.get() == 'O' and btn7.get() == 'O'):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", 'O Wins !')
            count = 0
            clear()
            play()
          
        elif (count == 9):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Cat game! It's a tie!")
            click = True
            count = 0
            clear()
            play()

    def clear():
        btn1.set('')
        btn2.set('')
        btn3.set('')
        btn4.set('')
        btn5.set('')
        btn6.set('')
        btn7.set('')
        btn8.set('')
        btn9.set('')

    play()

    ttt.mainloop()

# Call main function
if __name__ == '__main__':
    menu()

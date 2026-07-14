import tkinter 

def button_behavior(row, column):
    global cur_player 
    
    if (game_over):
        return      
    
    #hna anzid whd l condition ila kan l morba3 deja 3amr 
    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"]=cur_player 

    #hna anbda nswitchi mabin l players 

    if cur_player == playerO :
        cur_player = playerX
    else :
        cur_player = playerO
    
    label["text"]= cur_player+"'s turn" 

    #hna anzid fonction li atchuf lia chkun rbe7
    check_winner()


def check_winner():
    global turns, game_over

    turns += 1 
    
    #horizontal check
    for row in range (3) :    
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] 
        and board[row][0]["text"] != "") :
            label.config(text=board[row][0]["text"]+"is the winner" , foreground="yellow")
            
            for column in range(3) :
                board[row][column].config(foreground="yellow")
            game_over = True
            return    
    
    #vertical check
    for column in range (3) :    
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] 
        and board[0][column]["text"] != "") :
            label.config(text=board[column][1]["text"]+" is the winner !" , foreground="yellow")
            
            for row in range(3) :
                board[row][column].config(foreground="yellow")
            game_over = True
            return    

    #diagonal check
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] 
    and board[0][0]["text"] != "") :
        label.config(text=board[0][0]["text"]+" is the winner !" , foreground="yellow")
        
        for i in range(3) :
            board[i][i].config(foreground="yellow")
        game_over = True
        return      
    
    #diagonal check jiha lakhra 
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] 
    and board[0][2]["text"] != "") :
        label.config(text=board[0][0]["text"]+" is the winner !" , foreground="yellow")
        
        #khasna n loopiwha manually (9ELEB 3LACH)
        board[0][2].config(foreground="yellow")
        board[1][1].config(foreground="yellow")
        board[2][0].config(foreground="yellow")        
        game_over = True
        return    

    #ta3adol 
    if (turns == 9) :
        game_over = True
        label.config(foreground="yellow", text="Ta3adol ajemi!")              


def new_game():
    global turns, game_over

    turns = 0
    game_over = False

    label.config(text=cur_player+"'s turn", font=("Consolas", 20), foreground="white", background=("black"))
    for row in range (3) :
        for column in range (3) :
            board[row][column].config(text="", background="gray" , foreground="blue")

#game variabls

playerX = "X"
playerO = "O"
cur_player = playerX

board= [[0,0,0],
        [0,0,0],
        [0,0,0]
        ]

turns = 0
game_over = False

#zid hnaya chi colors stockihum




#window setup 

window=tkinter.Tk()  #kat creer biha l window 
window.title("Tic Tac Toe")
window.resizable(False,False)

frame= tkinter.Frame(window)
label= tkinter.Label(frame, text=cur_player+"'s turn", font=("Consolas", 20), foreground="white", background=("black"))
label.grid(row=0, column=0, columnspan=3, sticky="we") #we hia west to east : mn limn l lissr

#creeiti l buttons 
for row in range (3) :
    for column in range (3) :
        board[row][column]=tkinter.Button(frame, text="", background="gray" , foreground="blue" , font=("consolas", 50, "bold"), width=5, height=2,
                                           command=lambda row=row, column=column : button_behavior(row, column))
        
        #hna aykhssk tgadhum bach ybano
        board[row][column].grid(row=row+1, column=column)

button=tkinter.Button(frame, text="Restart", font=("Consolas", 20), foreground="white", background=("black"), command=new_game)
button.grid(row=4, column=0, columnspan=3 , sticky="we")        

frame.pack()

# center the window (jbtha mn google)
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int(screen_width/2 - window_width/2)
window_y = int(screen_height/2 - window_height/2)

window.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')


window.mainloop()
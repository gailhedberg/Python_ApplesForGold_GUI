# ApplesForGold.py by gail hedberg - august 11, 2015
# updated version of this game for class project, original version found at:
#  https://www.youtube.com/watch?v=1ELfaJcUWOQ
#
# python final practical - added a tkinter gui for the game

from tkinter import *
from tkinter import ttk
from tkinter import messagebox




class GameLoot:
    def __init__(self):
        print('GameLoot init')
        self.apples = 0
        self.gold = 0
        self.play = 'N'

    def addAnApple(self):
        self.apples = self.apples + 1
        
    def getApples(self):
        return self.apples

    def hasApples(self):
        if self.apples == 0:
            return False
        else: return True

    def sellApples(self):
        self.gold = self.gold + (self.apples * 10)
        self.apples = 0

    def getGold(self):
        return self.gold

    def setPlay(self, play):
        self.play = play.upper()
 #       print('play is ', self.play)

    def playGame(self):
        if self.play == 'Y':
            return True
        else:
            return False
        
    def isAWinner(self):
        if self.gold > 57:
            return True
        else : return False

    def printScore(self):
        s = "Good going! You have {} apples, and ${} million in Gold!".format(self.apples, self.gold)
        print(s)
        
    def newGame(self):
        self.apples = 0
        self.gold = 0
        
    def printLoot(self):
        pass
        ##this function is used for debugging
        #print('apples : ', self.apples)
        #print('gold   : ', self.gold)
        #print('play   : ', self.play)
##       
### this ends the GameLoot class definition
##
     
class MainGui:
    
    def __init__(self, root, this_game):
        
        self.this_game = this_game
        #print(type(self.this_game))

        # create the frame
        root.title("Let's Play - APPLES FOR GOLD")
   
       # create the content frame
        self.fr_content = ttk.Frame(root, padding = "3 3 12 12")

        # create the welcome and rules labels
        str_welcome = "Hello and Welcome to the Game"
        ttk.Label(self.fr_content, text = str_welcome, foreground = 'blue', 
                  justify = CENTER).grid(row = 0, column = 0, columnspan = 5, pady = 5, sticky = (E, W))
        
        str_rules = """The objective of the game is to pick apples and trade them for Gold.
    You need $57 million in Gold to Win!     Good Luck!"""
        ttk.Label(self.fr_content, text=str_rules, foreground = 'blueviolet', 
                  justify = CENTER).grid(row=1, column = 0, columnspan = 5, padx = 5, pady = 5, sticky = (E, W))
   

        # create the images
        img = PhotoImage(file = 'apple_tree50.gif')
        lbl_apple_image = ttk.Label(self.fr_content, image = img)
        lbl_apple_image.image_names = img

        img2 = PhotoImage(file = 'potofgold50.gif')
        lbl_gold_image = ttk.Label(self.fr_content, image = img2)
        lbl_gold_image.image_names = img2
      
                   
        # create the Apple widgets
        lbl_apple = ttk.Label(self.fr_content, text = 'Apples', foreground = 'red')
        lbl_apple.config( font = ('Tahoma', 14, 'bold'), foreground = 'red')                                
  
        self.apple_count = StringVar()
        self.apple_count.set('0')
        
        self.lbl_apple_count = ttk.Label(self.fr_content, textvariable = self.apple_count, foreground = 'red')
        self.lbl_apple_count.config( font = ('Tahoma', 14, 'bold'), foreground = 'red')                                
     

         # create the Gold widgets
        lbl_gold = ttk.Label(self.fr_content, text = 'Gold $')
        lbl_gold.config( font = ('Tahoma', 14, 'bold'), foreground = 'gold')                                

        self.gold_amt = StringVar()
        self.gold_amt.set('0')
        self.lbl_gold_amt = ttk.Label(self.fr_content, textvariable = self.gold_amt)
        self.lbl_gold_amt.config( font = ('Tahoma', 14, 'bold'), foreground = 'gold')                                


        #create the buttons
        self.btn_buy_apples = ttk.Button(self.fr_content, text = 'Pick Apples', command = self.btn_buy_apples)
        btn_buy_gold = ttk.Button(self.fr_content, text = 'Trade for Gold', command = self.btn_buy_gold)
   

        ## place the widgets
        self.fr_content.grid(row = 2, column = 0, rowspan = 4, columnspan = 5, pady = 5, padx = 5, sticky = (N, E, S, W))

        lbl_apple.grid(row = 2, column = 0, padx = 7, pady = 7)
        self.lbl_apple_count.grid(row = 2, column = 1)
        lbl_apple_image.grid(row = 3, column = 0, rowspan = 2, columnspan = 2, padx = 5, pady = 5, sticky = (N, E, S, W))

        lbl_gold.grid(row = 2, column = 4, padx = 7, pady = 7)
        self.lbl_gold_amt.grid(row = 2, column = 5)
        lbl_gold_image.grid(row = 3, column = 4, rowspan = 2, columnspan = 2, padx = 5, pady = 5)

        self.btn_buy_apples.grid(row = 3, column = 3, padx = 10, pady =10)
        btn_buy_gold.grid(row = 4, column = 3, padx = 10, pady = 10)
  
              
    # define the event handlers     
    def btn_buy_apples(self):
        #print('buy apples')
        
        self.this_game.addAnApple()
        #self.this_game.printScore() 
        self.apple_count.set('{}'.format(self.this_game.getApples()))

    def btn_buy_gold(self):
        #print('buy gold')

        if self.this_game.hasApples() == False:
            messagebox.showinfo(title="Oops", 
                                message="You have no apples to trade for gold!\n\n\tGo pick some!")            
        else:
            self.this_game.sellApples()
            #self.this_game.printScore()
            self.apple_count.set('{}'.format(self.this_game.getApples()))
            self.gold_amt.set('{}'.format(self.this_game.getGold()))

            if self.this_game.isAWinner():
                #print("\n * * * You Won the Game! * * *\n")
                ret = messagebox.askyesno(title="You are a WINNER!", 
                                          message="You won the game!\n\nDo you want to play again?")
                if ret == False:
                    self.close_app()
                else: 
                    self.this_game.newGame()
                    self.apple_count.set('{}'.format(self.this_game.getApples()))
                    self.gold_amt.set('{}'.format(self.this_game.getGold()))
                    self.btn_buy_apples.focus()


    def close_app(self):
        sys.exit()


    def OnCloseWindow(self, event):
        self.Destroy()
        


def main():
    root = Tk()
    this_game = GameLoot()
    main_gui = MainGui(root, this_game)
    #play_game(root, this_game)

    root.mainloop()


if __name__  ==  "__main__" : main()
    
    


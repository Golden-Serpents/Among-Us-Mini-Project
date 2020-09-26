import tkinter as tk
import time

##crew mate names as inputs to test it's probably better to have them set instead of input##

crew0=str(input())
crew1=str(input())
crew2=str(input())
crew3=str(input())
crew4=str(input())
crew5=str(input())
crew6=str(input())
crew7=str(input())
crew8=str(input())
crew9=str(input())

crew_list=[crew0, crew1, crew2, crew3, crew4, crew5, crew6, crew7, crew8, crew9, crew0, crew1, crew2, crew3, crew4, crew5, crew6, crew7, crew8, crew9, crew0, crew1, crew2, crew3, crew4, crew5, crew6, crew7, crew8, crew9]

##i think this is obselete##

sus_on0=False
sus_on1=False
sus_on2=False
sus_on3=False
sus_on4=False
sus_on5=False
sus_on6=False
sus_on7=False
sus_on8=False
sus_on9=False

sus_on=[sus_on0, sus_on1, sus_on2, sus_on3, sus_on4, sus_on5, sus_on6, sus_on7, sus_on8, sus_on9]



##the tkinter bit that kinda works but not quite


class Application(tk.Frame):
    
    def __init__(self, master=None):        ##this makes it work i definitely didn't copy paste from documentation##
        
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):       ##creating the buttons headers and their placement##
        self.crew = []
        self.crew_innocent = []
        self.crew_suspicious = []
        self.crew_dead = []

        # define functions
        def suspicious(x):           ##defining suspicious() to change the label/title font colour to red##
            self.crew[x]["fg"] = "red"
            return False
        def dead(x):                 ##defining dead() to disable the buttons and change label/title font colour to black##
            self.crew[x]["fg"] = "black"
            self.crew_suspicious[x]["state"] = tk.DISABLED
            self.crew_innocent[x]["state"] = tk.DISABLED
            self.crew_dead[x]["state"] = tk.DISABLED
            return False
        def innocent(x):             ##defining innocent() to change the label/title font colour to blue
            self.crew[x]["fg"] = "blue"
            return False

        for i in range(0,10):            ##iterative process to create unknown crew mate buttons##

            row_number = i*3             ##probably the worst way to iterate which row and column is assigned to which crew mate##
            if (row_number % 2) == 0:
                row_number = int(row_number/2)
            else:
                row_number = int((row_number - 3)/2)

            column_number = i % 2
            if column_number == 1:
                column_number = 5
            else:
                column_number = 0
            
            self.crew.append(tk.Label(self, width = 10, height = 1, fg = "green", text = crew_list[i]))       ##creating a label/title for each i, tried to use width 30 to give maximum space for names but that screwed with the rest of the grid##
            self.crew[i].grid(row = row_number, column = column_number)

            row_number = row_number + 1

            self.crew_innocent.append(tk.Button(self, width = 10, height = 1, fg = "black", text="Innocent"))       ##creating innocent button to be placed beneath the label/title##
            self.crew_innocent[i]["command"] = lambda i=i: innocent(i)
            self.crew_innocent[i].grid(row = row_number, column = column_number)

            column_number = column_number + 1

            self.crew_suspicious.append(tk.Button(self, width = 10, height = 1, fg = "black", text = "Suspicious"))     ##creating suspicious button to be placed immediately right of innocent button##
            self.crew_suspicious[i]["command"] = lambda i=i: suspicious(i)
            self.crew_suspicious[i].grid(row = row_number, column = column_number)

            column_number = column_number + 1

            self.crew_dead.append(tk.Button(self, width = 10, height = 1, fg = "black", text = "Dead"))          ##creating dead button to be placed immediately right of suspicious button##
            self.crew_dead[i]["command"] = lambda i=i: dead(i)
            self.crew_dead[i].grid(row = row_number, column = column_number)


            #if self.crew_innocent["state"] == tk.DISABLED:      ##absolute bodge of selections to have the buttons return to normal state. commands do not work after being enabled again##
            #    self.crew_innocent["state"] = tk.NORMAL
            #else:
            #    self.crew_innocent["state"] = tk.DISABLED
            #if self.crew_suspicious["state"] == tk.DISABLED:
            #    self.crew_suspicious["state"] = tk.NORMAL
            #else:
            #    self.crew_suspicious = tk.DISABLED
            #if self.crew_dead["state"] == tk.DISABLED:
            #    self.crew_dead["state"] = tk.NORMAL
            #else:
            #    self.crew_dead["state"] = tk.DISABLED
            #if self.crew["fg"] == "black":
            #    self.crew["fg"] = "green"
            #else:
            #    self.crew["fg"] = "black"

        
                ##i think this doesn't need to be here but i prefer not risking dumb errors it's bad practise i'm aware##


        self.quit = tk.Button(self, width = 10, height = 1, fg = "red")                     ##creating button to quit, row is set well beyond everything else as if nothing is in a column/row it defaults to being immediately below
        self.quit["text"] = "QUIT"                                                          ##the other buttons (in rows) or immediately next to with columns just adds extra room in case i need to add anything lese##
        self.quit["command"] = self.master.destroy
        self.quit.grid(row = 999, column = 4)


root = tk.Tk()      ##definitely not more copy pasting i promise this time Kappa##

app = Application(master=root)

app.master.title("Among Us Notes")
app.master.geometry("600x270")
app.mainloop()

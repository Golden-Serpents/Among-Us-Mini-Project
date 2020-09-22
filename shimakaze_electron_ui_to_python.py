import tkinter as tk
import time

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






class Application(tk.Frame):
    
    def __init__(self, master=None):        ##this makes it work i definitely didn't copy paste from documentation##
        
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):       ##creating the buttons headers and their placement##

        
        for crewmate in range(0,10):            ##iterative process to create unknown crew mate buttons##

            row_number = crewmate*3

            if (row_number % 2) == 0:

                
                row_number = int(row_number/2)

            else:

                row_number = int((row_number - 3)/2)



            
            column_number = crewmate % 2
            
            if column_number == 1:

                column_number = 5
                
            else:
                column_number = 0


                
            crew=crew_list[crewmate]
            
            self.crew = tk.Label(self, width = 10, height = 1, fg = "green")
            self.crew["text"] = crew
            self.crew.grid(row = row_number, column = column_number)

            row_number = row_number + 1

            def innocent():
                
                self.crew["fg"] = "blue"

            
            self.crew_innocent = tk.Button(self, width = 10, height = 1, fg = "blue")
            self.crew_innocent["text"] = "Innocent"
            self.crew_innocent["command"] = innocent()
            self.crew_innocent.grid(row = row_number, column = column_number)

            column_number = column_number + 1

            def suspicious():

                self.crew["fg"] = "red"

            self.crew_suspicious = tk.Button(self, width = 10, height = 1, fg = "red")
            self.crew_suspicious["text"] = "Suspicious"
            self.crew_suspicious["command"] = suspicious()
            self.crew_suspicious.grid(row = row_number, column = column_number)

            column_number = column_number + 1

            def dead():
                
                self.crew["fg"] = "black"
                self.crew_suspicious["state"] = tk.DISABLED
                self.crew_innocent["state"] = tk.DISABLED
                self.crew_dead["state"] = tk.DISABLED

            self.crew_dead = tk.Button(self, width = 10, height = 1, fg = "black")
            self.crew_dead["text"] = "Dead"
            self.crew_dead["command"] = dead()
            self.crew_dead.grid(row = row_number, column = column_number)


        
        crewmate = crewmate + 1


        self.quit = tk.Button(self, width = 10, height = 1, fg = "red")
        self.quit["text"] = "QUIT"
        self.quit["command"] = self.master.destroy
        self.quit.grid(row = 999, column = 4)


root = tk.Tk()      #main window

app = Application(master=root)

app.master.title("Among Us Notes")
app.master.geometry("600x270")
app.mainloop()

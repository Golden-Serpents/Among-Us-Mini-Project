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


def decision_crew():        

    if (self.crew["state"] == tk.NORMAL):
        
        self.crew["state"] = tk.DISABLED

        for crewmate in range(11, 30):

            crew_member= crew_list[crewmate]

            if (self.crew["text"] == "inno " + crewmate) or (self.crew["text"] == "sus " + crewmate):

                self.crewmate["state"] = tk.NORMAL

                crewmate = crewmate + 1

            else:

                crewmate = crewmate + 1

                    

class Application(tk.Frame):
    
    def __init__(self, master=None):        ##this makes it work i definitely didn't copy paste from documentation##
        
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        unknown_crewmates=tk.Label(self, width = 10, height = 1, text = "unknown", fg = "green")
        unknown_crewmates.grid(row = 0, column = 2)

        sus_crewmates=tk.Label(self, width = 10, height = 1, text = "suspicious", fg = "red")
        sus_crewmates.grid(row = 6, column = 2)

        safe_crewmates=tk.Label(self, width = 10, height = 1, text = "innocent", fg = "blue")
        safe_crewmates.grid(row = 14, column = 2)
        
    def decision_crew():        

        if (self.crew["state"] == tk.NORMAL):
            
            self.crew["state"] = tk.DISABLED

            for crewmate in range(11, 30):

                crew_member= crew_list[crewmate]

                if (self.crew["text"] == "inno " + crewmate) or (self.crew["text"] == "sus " + crewmate):

                    self.crewmate["state"] = tk.NORMAL

                    crewmate = crewmate + 1

                else:

                    crewmate = crewmate + 1
                
    def create_widgets(self):       ##creating the buttons headers and their placement##

        
        for crewmate in range(0,10):            ##iterative process to create unknown crew mate buttons##

            row_number = crewmate 

            if row_number % 2 == 1:
                
                row_number = int((crewmate/2) + 0.5)
                
            else:
                
                row_number = int((crewmate/2) + 1)

            
            column_number = crewmate % 2
            
            if column_number == 1:
                
                column_number = 3
                
            else:
                
                column_number = 1

            crew=crew_list[crewmate]
            
            self.crew = tk.Button(self, width = 10, height = 1, fg = "green")
            self.crew["text"] = crew
            self.crew["state"] = tk.NORMAL
            self.crew["command"] = decision_crew()
            self.crew.grid(row = row_number , column = column_number)
            crewmate = crewmate + 1


        crewmate=0

        for crewmate in range(0, 10):            ##iterative process to create sus crew mate buttons##
            
            row_number = crewmate

            if row_number % 2 == 1:
                
                row_number = (crewmate/2) + 6.5
                
                row_number = int(row_number)
                
            else:

                row_number = int((crewmate/2) + 7)

            column_number = crewmate

            if column_number % 2 == 1:
                
                column_number = 3
                
            else:
                
                column_number = 1

            crew=crew_list[crewmate]
                
            self.crew = tk.Button(self, width = 10, height = 1, fg = "red")
            self.crew["text"] = "sus " + crew
            self.crew["state"] = tk.DISABLED
            self.crew["command"] = self.disable()
            self.crew.grid(row = row_number , column = column_number)
            crewmate = crewmate + 1
            
        crewmate=0

        for crewmate in range(0, 10):            ##iterative process to create inno crew mate buttons##
            
            row_number = crewmate

            if row_number % 2 == 1:
                
                row_number = (crewmate/2) + 14.5
                
                row_number = int(row_number)
                
            else:

                row_number = int((crewmate/2) + 15)

            column_number = crewmate

            if column_number % 2 == 1:
                
                column_number = 3
                
            else:
                
                column_number = 1

            crew=crew_list[crewmate]
                
            self.crew = tk.Button(self, width = 10, height = 1, fg = "blue")
            self.crew["text"] = "inno " + crew
            self.crew["state"] = tk.DISABLED
            self.crew["command"] = self.disable()
            self.crew.grid(row = row_number , column = column_number)
            crewmate = crewmate + 1
            identity = crew
                
        self.quit = tk.Button(self, text = "quit", width = 10, height = 1, fg = "red",
                             command = self.master.destroy)
        self.quit.grid(row = 20, column = 2)

        def decision_crew():        #duplicate at previous indent level

            if (self.crew["state"] == tk.NORMAL):
                
                self.crew["state"] = tk.DISABLED

                for crewmate in range(11, 30):

                    crew_member= crew_list[crewmate]

                    if (self.crew["text"] == "inno " + crewmate) or (self.crew["text"] == "sus " + crewmate):

                        self.crewmate["state"] = tk.NORMAL

                        crewmate = crewmate + 1

                    else:

                        crewmate = crewmate + 1

    
    def decision_crew():        

        if (self.crew["state"] == tk.NORMAL):
            
            self.crew["state"] = tk.DISABLED

            for crewmate in range(11, 30):

                crew_member= crew_list[crewmate]

                if (self.crew["text"] == "inno " + crewmate) or (self.crew["text"] == "sus " + crewmate):

                    self.crewmate["state"] = tk.NORMAL

                    crewmate = crewmate + 1

                else:

                    crewmate = crewmate + 1


root = tk.Tk()

app = Application(master=root)

app.master.title("Among Us Notes")
app.master.geometry("300x500")
app.mainloop()

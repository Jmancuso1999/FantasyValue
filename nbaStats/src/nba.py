import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog 


def get_Value(player):
        return player[1]

def lineupEvaluation(lineup):
        players = pd.read_csv(lineup) 

        # print(players.info()) # Provides information about the data frame and the columns data types

        value = []

        name = players['Name']
        fantasyPoints = players['AvgPointsPerGame']
        salary = players['Salary']

        for i in range(len(players)):
                val = fantasyPoints[i] / (salary[i] / 1000)
                value.append([name[i], val.round(2), salary[i]])   

        value.sort(key = get_Value, reverse = True)
        
        df = pd.DataFrame(value)
        df.columns = ['Player' , 'Value', 'Salary']
        df.to_csv('../value/lineupValue.csv')
        
class GUI:

        # Create GUI 
        window = tk.Tk()

        def __init__(self, title):
                self.title = title
                window.title(title)

        def import_csv_data():
                filename = filedialog.askopenfilename()
                evaluating = filename
                lineupEvaluation(evaluating) # Change based on the lineup you'd like to evaluate

        window.geometry("500x500")
        selectFile = tk.Button(text = 'Select File', command = import_csv_data)
        button_exit = tk.Button(text = "Exit", command = exit) 
        selectFile.place(relx=0.5, rely=0.5, anchor=CENTER)
        button_exit.place(relx=.6, rely=0.5, anchor=CENTER)

        window.mainloop()

def main():
        userGUI = GUI("Evaluation")

if __name__ == "__main__":
    main()
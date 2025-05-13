import tkinter as tk
from tkinter import messagebox

class Quiz:
    def __init__(self ,root):
        self.question_num = tk.IntVar(root)
        self.question_num.set(0)
        self.questions = ["What is the Chemical Symbol for Copemicium?", "What is the average lifespan of a jellyfish?", "What is the average height for Asians"]
        self.answers = [3, 2, 1]
        self.choices = [["Cu", "Co", "Cn", "Cr"], ["24 months", "12 months", "16 months", "6 months"], ["5'4", "5'6", "5'9", "5'7"]]
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)


        self.title_frame = tk.Frame(root, width= "400", height= "50", bg= "green")
        self.main_frame = tk.Frame(root, width= "400", height= "350", bg= "blue")
        self.quiz_frame = tk.Frame(root, width= "400", height= "350", bg= "black")
        self.title_frame.grid(row=0, column=0, sticky= "ew")
        self.main_frame.grid(row=1, column=0, sticky= "nsew")

        self.start = tk.Button(self.main_frame, text="START", command=self.start_quiz)
        self.start.place(x= 175, y= 175)

    def start_quiz(self):
        self.main_frame.grid_forget()
        self.quiz_frame.grid(row=1, column=0, sticky= "nsew")
        num = 0
        for choices in self.choices[num]:
            choice = tk.Radiobutton(self.quiz_frame, variable= self.question_num, value = choices, text = choices)
            choice.pack()
        


if __name__ == "__main__":
    root = tk.Tk()
    order = Quiz(root)
    root.title("Quiz")
    root.geometry("400x400")
    root.resizable(False, False)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox

class Quiz:
    def __init__(self ,root):
        self.question_word = tk.StringVar(root)
        self.question_word.set(None)
        self.score = 0
        self.quesno = 0
        self.ans_no = 0

        self.questions = [
            "What is the Chemical Symbol for Copemicium?", 
            "What is the average lifespan of a jellyfish?", 
            "What is the average height for Asians", 
            "What country has the most pyramids in the world?", 
            "What is the largest organ in the human body?", 
            "What is the shortest war in history?", 
            "What is the most stolen food in the world?", 
            "What chemical element has the highest melting point?", 
            "What is the world's oldest currency?",
            "What is the national animal of Scotland?"
            ]
        self.answers = ["Cn", "12 months", "5'4", "Sudan", "Skin", "Anglo Zanzibar War", "Cheese", "Tungsten", "Pound Sterling", "Unicorn"]

        self.choices = [
            ["Cu", "Co", "Cn", "Cr"],
            ["24 months", "12 months", "16 months", "6 months"],
            ["5'4", "5'6", "5'9", "5'7"],
            ["Sudan", "Egypt", "Peru", "Guatemala"], 
            ["Brain", "Cranium", "Skin", "Lungs"], 
            ["The Six Day War", "The Winter War", "The Falklands War", "Anglo Zanzibar War"], 
            ["Wine", "Cheese", "Steak", "Caviar"], ["Platinum", "Tungsten", "Magnesium", "Rhenium"], 
            ["Japanese Yen", "Chinese Yuan", "Pound Sterling", "Indian Rupee"],
            ["Unicorn", "Dragon", "Griffin", "Otters"]]
        
        self.radio_butts = []
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)


        self.title_frame = tk.Frame(root, width= "400", height= "50", bg= "#061A40")
        self.main_frame = tk.Frame(root, width= "400", height= "350", bg= "#B9D6F2")
        self.quiz_frame = tk.Frame(root, width= "400", height= "350", bg= "cornsilk2")
        self.finish_frame = tk.Frame(root, width= "400", height= "350", bg= "#A1B5D8")
        self.title_frame.grid(row=0, column=0, sticky= "ew")
        self.main_frame.grid(row=1, column=0, sticky= "nsew")

        self.title_label = tk.Label(self.title_frame, text= "General Knowledge Quiz")
        self.title_label.place(relx= 0.5, rely= 0.5, anchor= "center")
        self.stats_label = tk.Label(self.finish_frame, text= f"You have a score of {self.score} out of 10!")

        self.submit_button = tk.Button(self.quiz_frame, text= "Submit", command= self.submit_check, state= "disabled")
        self.submit_button.pack()

        self.start = tk.Button(self.main_frame, text="START", command=self.start_quiz)
        self.start.place(x= 175, y= 175)

    def start_quiz(self):
        self.main_frame.grid_forget()
        self.quiz_frame.grid(row=1, column=0, sticky= "nsew")
        num = 1
        for choices in self.choices[0]:
            self.choice = tk.Radiobutton(self.quiz_frame, variable= self.question_word, value = choices, text = choices, command=self.enable_button)
            self.choice.pack()
            self.radio_butts.append(self.choice)
            num += 1
        self.title_label.configure(text=self.questions[0])

    def radio_forget(self):
        for radio_button in self.radio_butts:
            radio_button.forget()

    def finish(self):
        self.quiz_frame.grid_forget()
        self.finish_frame.grid(row=1, column=0, sticky= "nsew")
        self.stats_label.pack()
        self.stats_label.config(text= f"You scored a {self.score} out of 10!")
        

    def make_button(self, number):
        for choices in self.choices[number]:
            self.choice = tk.Radiobutton(self.quiz_frame, variable= self.question_word, value = choices, text = choices, command=self.enable_button)
            self.choice.pack()
            self.radio_butts.append(self.choice)

    def enable_button(self):
        self.submit_button.config(state="normal")

    def submit_check(self):
        if self.quesno + 1 >= len(self.questions):
            self.finish()
        else:
            answer = self.answers[self.quesno]
            self.quesno += 1

            if self.question_word.get() != answer:
                messagebox.showerror("Wrong!", f"The correct answer is {answer}")
            else:
                messagebox.showinfo("Correct!", "You got it right!")
                self.score += 1
            self.title_label.configure(text=self.questions[self.quesno])
            self.radio_forget()
            self.make_button(self.quesno)
            self.submit_button.config(state="disabled")

        
        
        


if __name__ == "__main__":
    root = tk.Tk()
    order = Quiz(root)
    root.title("Quiz")
    root.geometry("600x600")
    root.mainloop()

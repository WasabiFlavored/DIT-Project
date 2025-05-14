"""This file is a General Knowledge quiz for users."""
import tkinter as tk
from tkinter import messagebox


class Questions:
    """Handles all the lists, makes it easier to handle in Quiz."""

    def __init__(self):
        """Store the questions, choices and answers."""
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

        self.choices = [
            ["Cu", "Co", "Cn", "Cr"],
            ["24 months", "12 months", "16 months", "6 months"],
            ["5'4", "5'6", "5'9", "5'7"],
            ["Sudan", "Egypt", "Peru", "Guatemala"],
            ["Brain", "Cranium", "Skin", "Lungs"],
            ["The Six Day War", "The Winter War",
                "The Falklands War", "Anglo Zanzibar War"],
            ["Wine", "Cheese", "Steak", "Caviar"],
            ["Platinum", "Tungsten", "Magnesium", "Rhenium"],
            ["Japanese Yen", "Chinese Yuan", "Pound Sterling", "Indian Rupee"],
            ["Unicorn", "Dragon", "Griffin", "Otters"]
            ]

        self.answers = [
                "Cn", "12 months", "5'4", "Sudan",
                "Skin", "Anglo Zanzibar War", "Cheese",
                "Tungsten", "Pound Sterling", "Unicorn"
                ]
        self.question_num = 0

    def get_ques(self, num):
        """Short method to call a specific question number."""
        return self.questions[num]

    def get_choice(self, num):
        """Call a specific multiple question selection choice."""
        return self.choices[num]

    def get_ans(self, num):
        """Short method to call a specific question answer."""
        return self.answers[num]

    def all_ques(self):
        """Return the length of the question list to use in loop."""
        return len(self.questions)


class Quiz:
    """This class is where the main function will run."""

    def __init__(self, root):
        """Store all variables required."""
        self.question_stats = Questions()  # Stores support class in a variable
        self.question_word = tk.StringVar(root)  # Stores a string variable
        self.question_word.set(None)  # Makes the string variable blank
        self.score = 0
        self.quesno = 0
        self.radio_butts = []  # List to store radiobuttons

        root.grid_columnconfigure(0, weight=1)
        # Makes the column fill all space
        root.grid_rowconfigure(1, weight=1)
        # Makes the first row fill all space

        self.title_frame = tk.Frame(root, width="400",
                                    height="100", bg="#061A40")
        self.main_frame = tk.Frame(root, width="400",
                                   height="500", bg="#B9D6F2")
        self.quiz_frame = tk.Frame(root, width="400",
                                   height="500", bg="#BDCADB")
        self.finish_frame = tk.Frame(root, width="400",
                                     height="500", bg="#A1B5D8")
        self.title_frame.grid(row=0, column=0, sticky="ew")
        self.main_frame.grid(row=1, column=0, sticky="nsew")

        self.title_label = tk.Label(self.title_frame,
                                    text="General Knowledge Quiz", fg="white",
                                    bg="#061A40", font=("Arial", 18))
        self.title_label.place(relx=0.5, rely=0.5,
                               anchor="center")
        self.stats_label = tk.Label(self.finish_frame)
        # Empty label to display user score when finished
        self.age_label = tk.Label(self.main_frame,
                                  text="How old are you?")
        self.submit_button = tk.Button(self.quiz_frame,
                                       text="Submit",
                                       command=self.submit_check,
                                       state="disabled")
        self.submit_button.place(relx=0.5,
                                 rely=0.5, anchor="center")
        # Starts off disabled, enabled once a radiobutton is selected
        self.restart_button = tk.Button(self.finish_frame,
                                        text="Restart", command=self.restart)
        self.restart_button.pack()
        self.enter_button = tk.Button(self.main_frame,
                                      text="Enter", command=self.check_age)

        self.entry = tk.Entry(self.main_frame)
        self.age_label.pack()
        self.entry.pack()
        self.enter_button.pack()

        self.start = tk.Button(self.main_frame, text="START",
                               command=self.start_quiz, state="disabled")
        self.start.place(relx=0.5, rely=0.5, anchor="center")
        # Sets relative x and relative y to half, centering it to the page

    def check_age(self):
        """Validate age to allow user to start quiz."""
        age = self.entry.get()
        try:
            age = int(age)
            if 1 < age < 100:
                self.start.config(state="normal")
                messagebox.showinfo("Pass!", "Enjoy the Quiz!")
            else:
                messagebox.showerror("Error", "Please enter a valid age!")
        except ValueError:
            messagebox.showerror("Uh Oh!", "Please type a valid number!")

    def start_quiz(self):
        """Assign to Start button on home page.

        Mainly changes the main frame into the quiz frame
        and makes all the initial radiobuttons
        """
        self.main_frame.grid_forget()
        # Removes the Main Frame to allow space for the Quiz Frame
        self.quiz_frame.grid(row=1, column=0, sticky="nsew")
        # Calls the Quiz Frame
        self.make_button(0)
        # Makes initial radiobuttons for the first question
        self.title_label.configure(text=self.question_stats.get_ques(0))

    def radio_forget(self):
        """Remove all Radiobuttons to allow space for new ones."""
        for radio_button in self.radio_butts:
            radio_button.forget()
            # Creates a for loop that forgets/removes all existing radiobuttons

    def finish(self):
        """Change quiz frame to finish frame and display score."""
        self.quiz_frame.grid_forget()  # Removes the quiz frame
        self.finish_frame.grid(row=1, column=0, sticky="nsew")
        # Calls the finish frame
        self.stats_label.pack()
        # Packs the label that displays the users score
        self.stats_label.config(text=f"You scored a {self.score} out of 10!")
        # Refreshes the self.score stat to update to user's actual score

    def make_button(self, number):
        """Create the radiobuttons for each question."""
        for choices in self.question_stats.get_choice(number):
            # A for loop for each available choice every question (4)
            self.choice = tk.Radiobutton(self.quiz_frame,
                                         variable=self.question_word,
                                         value=choices, text=choices,
                                         command=self.enable_button,
                                         font=("Arial", 15), bg="#BDCADB")
            self.choice.pack()
            self.radio_butts.append(self.choice)
            # Adds each radiobutton into a list

    def enable_button(self):
        """Re-enable buttons after user selects a choice."""
        self.submit_button.config(state="normal")

    def check_answer(self, answer):
        """Use to check the user's answers.

        Displays corresponding message boxes depending
        on if they got the question right or wrong
        """
        if self.question_word.get() != answer:
            messagebox.showerror("Wrong!", f"The correct answer is {answer}")
            # Displays an Error message box that states that the user is wrong
        else:
            messagebox.showinfo("Correct!", "You got it right!")
            # Displays an info message box that shows the user is correct
            self.score += 1

    def submit_check(self):
        """Submit button on each question.

        Calls the check_answer method to check answers
        Calls radio_forget and make_button methods to
        remove and make new radiobuttons.
        """
        answer = self.question_stats.get_ans(self.quesno)
        # Puts the answer into a shorter variable
        self.check_answer(answer)
        if self.quesno + 1 >= self.question_stats.all_ques():
            # Moves on to the Score page when all out of questions
            self.radio_forget()
            self.finish()
        else:
            self.quesno += 1
            # Adds one to help keep track which question the user is on
            self.title_label.configure(
                text=self.question_stats.get_ques(self.quesno))
            # Changes the title label to the question the user is on
            self.radio_forget()
            self.make_button(self.quesno)
            self.submit_button.config(state="disabled")
            # Disables submit button until a radiobutton is selected

    def restart(self):
        """Restarts the quiz."""
        self.score = 0
        self.quesno = 0
        self.finish_frame.grid_forget()
        self.main_frame.grid(row=1, column=0, sticky="nsew")


if __name__ == "__main__":
    root = tk.Tk()
    order = Quiz(root)
    root.title("Quiz")
    root.geometry("600x600")  # Sets the window size to 600px by 600px
    root.resizable(False, False)  # Makes the window not resizable
    root.mainloop()

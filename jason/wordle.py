import tkinter as tk
import tkmacosx as tkm
from tkinter import messagebox
import os
import random
from typing import Dict, List, Union, Set

VALID_WORDS = os.path.join(os.path.dirname(__file__), "valid_words.txt")
WORD_BANK = os.path.join(os.path.dirname(__file__), "word_bank.txt")


class Wordle:
    def __init__(self, root: Union[tk.Tk, tk.Frame]):
        self.root = root
        self.root.bind("<Control-R>", self.reset)
        self.valid_words = self.getValidWords()
        self.target_word = self.getTargetWord()
        self.hidden_frame = tk.Frame(root)
        self.grid_frame = tk.Frame(root)
        self.top_lbl = tk.Label(text="WORDLE", font=("Helvetica", 60, "bold"))
        self.feedback_lbl = tk.Label(font=("Helvetica", 20, "normal"))
        self.original_fg = self.top_lbl.cget("fg")
        self.guess = tk.StringVar()
        self.guess.trace_add(mode="write", callback=self.displayWord)
        self.guess_box = tk.Entry(root, textvariable=self.guess)
        self.guess_box.bind("<Return>", self.onReturnKey)
        self.word_grid = self.createSquares(self.grid_frame)
        self.current_row = 0
        self.qwerty_top = tk.Frame()
        self.qwerty_mid = tk.Frame()
        self.qwerty_bot = tk.Frame()
        self.letter_buttons: Dict[str, tkm.Button] = {}
        self.createLetterButtons()
        self.original_bg = self.letter_buttons['A'].cget("bg")
        self.arrange()

    def createLetterButtons(self):
        rows = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
        frames = [self.qwerty_top, self.qwerty_mid, self.qwerty_bot]
        for i, row in enumerate(rows):
            for j, char in enumerate(row):
                self.letter_buttons[char] = tkm.Button(
                    frames[i], text=char, width=48, height=48,
                    font=("Helvetica", 24, "bold"),
                    command=lambda c=char: self.letterPress(c))
                self.letter_buttons[char].grid(row=0, column=j)

    def letterPress(self, char):
        pos = self.guess_box.index(tk.INSERT)
        self.guess.set(self.guess.get()+char)
        self.guess_box.icursor(pos+1)
        self.guess_box.focus()

    def getValidWords(self) -> Set[str]:
        valid_words = set()
        with open(VALID_WORDS, "r") as f:
            words = f.readlines()
            for word in words:
                valid_words.add(word.strip())
        return valid_words

    def getTargetWord(self) -> str:
        with open(WORD_BANK, "r") as f:
            words = f.readlines()
            target_word = random.choice(words)
            return target_word.strip()

    def onReturnKey(self, *unused_args):
        if not self.validateGuess():
            return
        if self.checkGuess():
            self.feedback_lbl.config(text="Splendid!", fg=self.original_fg)
            self.root.update()
            yes = messagebox.askyesno(
                title="You Win!",
                message=(f"Amazing, you won in {self.current_row+1} guesses! "
                          "Do you want to play again?"))
            self.reset() if yes else self.root.destroy()
            self.root.focus_force()
            self.guess_box.focus()
        elif self.current_row == 5:
            self.feedback_lbl.config(text=self.target_word, fg=self.original_fg)
            self.root.update()
            yes = messagebox.askyesno(
                title="You Lost",
                message=(f"The word was {self.target_word.upper()}. "
                          "Do you want to play again?"))
            self.reset() if yes else self.root.destroy()
            self.root.focus_force()
            self.guess_box.focus()
        else:
            self.current_row += 1
            self.guess.set("")
            self.feedback_lbl.config(text="")

    def validateGuess(self):
        guess = self.guess.get().lower().strip()
        if len(guess) != 5:
            self.feedback_lbl.config(text="Not enough letters", fg="red")
            return False
        if guess not in self.valid_words:
            self.feedback_lbl.config(text="Not in word list", fg="red")
            return False
        self.feedback_lbl.config(text="")
        return True

    def checkGuess(self) -> bool:
        guess = self.guess.get().lower().strip()
        guess_correct = [False]*5
        unmatched = []
        for col in range(5):
            if guess[col] == self.target_word[col]:
                self.word_grid[self.current_row][col].config(bg="green")
                self.letter_buttons[guess[col].upper()].config(bg="green")
                guess_correct[col] = True
            else:
                unmatched.append(self.target_word[col])
        for col in range(5):
            if guess_correct[col]:
                continue
            if guess[col] in unmatched:
                self.word_grid[self.current_row][col].config(bg="orange")
                if self.letter_buttons[guess[col].upper()].cget("bg") != "green":
                    self.letter_buttons[guess[col].upper()].config(bg="orange")
                del unmatched[unmatched.index(guess[col])]
            else:
                self.letter_buttons[guess[col].upper()].config(bg="gray")
        if guess == self.target_word:
            return True
        return False

    def createSquares(self, root) -> List[List[tk.Label]]:
        l = [[] for _ in range(6)]
        for row in l:
            for _ in range(5):
                row.append(tk.Label(root, borderwidth=3, relief="sunken",
                                    width=2, font=("Helvetica", 60, "bold")))
        return l

    def displayWord(self, *unused_args):
        guess = self.guess.get().upper()
        if len(guess) > 5:
            self.guess.set(guess[:5])
            guess = guess[:5]
        guess = guess.ljust(5)
        for col, char in enumerate(guess):
            self.word_grid[self.current_row][col].config(text=char)

    def arrange(self):
        self.top_lbl.pack()
        self.feedback_lbl.pack()
        for i in range(6):
            for j in range(5):
                self.word_grid[i][j].grid(row=i, column=j, padx=2, pady=2)
        self.grid_frame.pack(padx=10, pady=10)
        self.qwerty_top.pack(padx=10)
        self.qwerty_mid.pack(padx=10)
        self.qwerty_bot.pack(padx=10)
        self.hidden_frame.pack()
        self.guess_box.pack(in_=self.hidden_frame)
        self.guess_box.lower(self.hidden_frame)
        self.guess_box.focus()

    def reset(self):
        self.current_row = 0
        self.target_word = self.getTargetWord()
        self.feedback_lbl.config(text="")
        self.guess.set("")
        for row in self.word_grid:
            for lbl in row:
                lbl.config(text="", bg=root.cget("background"))
        for button in self.letter_buttons.values():
            button.configure(bg=self.original_bg)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Wordle")
    app = Wordle(root)
    root.mainloop()

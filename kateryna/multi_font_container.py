from tkinter import *
from tkinter.font import *


def example_method(): print("Click!")


class Button2:

    """
Allows multiple fonts in a very simple button.
Only supports 'master', 'text' and 'command' keywords
    ('master' is compulsory)
Fonts are delared in < > with the following options:
    BOLD = Make the text bold
    ITALIC = Make the text italic
    STRIKEOUT = Strike through the text
    UNDERLINE = Underlines the text
    an integer = the text size
    any other keyword is assumed to be the text family
    For the default text style, leave the < > empty
NOTE: Only supports the grid method due to internal handling
    """

    def __init__(self, master, text="<>", command=None):
        self.f = Frame(root)
        self.command = command
        self.f.bind("<Button-1>", lambda event: self.__click())
        self.f.bind("<ButtonRelease-1>", lambda event: self.__release())

        sections = [i.split(">") for i in text.split("<")[1:]]

        row, column = 0, 0
        for section in sections:

            font_decomp, kw = section[0].split("_"), {}
            for keyword in font_decomp:
                if keyword == "STRIKEOUT":
                    kw["overstrike"] = True
                elif keyword == "BOLD":
                    kw["weight"] = BOLD
                elif keyword == "ITALIC":
                    kw["slant"] = ITALIC
                elif keyword == "UNDERLINE":
                    kw["underline"] = True
                try:
                    kw["size"] = int(keyword)
                except:
                    kw["family"] = keyword

            temp_font = Font(**kw)
            l = Label(self.f, text=section[1].replace(
                "\n", ""), font=temp_font)
            l.grid(row=row, column=column)
            l.bind("<Button-1>", lambda event: self.__click())
            l.bind("<ButtonRelease-1>", lambda event: self.__release())

            if section[1].count("\n") >= 1:
                column = -1
                for i in range(section[1].count("\n") - 1):
                    l = Label(self.f, text="", font=temp_font)
                    l.grid(row=row, column=column)
                    l.bind("<Button-1>", lambda event: self.__click())
                    l.bind("<ButtonRelease-1>", lambda event: self.__release())
                    row += 1
                row += 1
            column += 1

    def __click(self):
        self.f.config(relief=SUNKEN)
        if self.command:
            self.command()

    def __release(self): self.f.config(relief=RAISED)

    def grid(self, **kw): self.f.grid(**kw)

    def config(self, **kw): self.f.config(**kw)


root = Tk()
root.title("Multiple fonts")
button = Button2(root, text="<30>82\n<50_BOLD>Pb\n<25>lead", command=example_method)
button.config(relief=RAISED, borderwidth=3, height=3, width=500)
button.grid()
root.mainloop()

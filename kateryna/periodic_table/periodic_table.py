import pandas as pd
import os
import tkinter as tk
import tkmacosx as tkm
from typing import List

TABLE_PATH = os.path.join(os.path.dirname(
    __file__), "Periodic Table of Elements.csv")


class PeriodicTable:
    def __init__(self, root):
        self.df: pd.DataFrame = pd.read_csv(TABLE_PATH)
        # print(self.df["Type"].unique())
        # print(self.df.Type.unique())
        self.df = self.df.convert_dtypes(convert_integer=True)
        self.table_frame = tk.Frame(root)
        self.title_lbl = tk.Label(self.table_frame,
                                  font=("Helvetica", 60, "bold underline"),
                                  text="The Periodic Table of Elements")
        self.search_var = tk.StringVar()
        self.search_var.trace_add(mode="write", callback=self.searchElements)
        self.search_box = tk.Entry(
            self.table_frame, textvariable=self.search_var)
        self.main_grid = tk.Frame(self.table_frame)
        self.series_grid = tk.Frame(self.table_frame)
        self.info_grid = tk.Frame(root)
        self.element_buttons: List[tkm.Button] = []
        for i, el in self.df.iterrows():
            if el.AtomicNumber in range(57, 72):
                self.setElement(self.series_grid, i, el,
                                0, el.AtomicNumber-57)
            elif el.AtomicNumber in range(89, 104):
                self.setElement(self.series_grid, i, el,
                                1, el.AtomicNumber-89)
            else:
                self.setElement(self.main_grid, i, el, el.Period-1,
                                int(el.Group)-1)
        self.colorElements()
        self.title_lbl.pack(pady=20, side="top")
        self.search_box.pack(pady=20, side="top")
        self.main_grid.pack(padx=10)
        self.series_grid.pack(pady=20)
        self.table_frame.pack(side=tk.LEFT)
        self.info_grid.pack(side=tk.RIGHT)

    def searchElements(self, *unused_args):
        query = self.search_var.get()
        if not query:
            self.clearHighlights()
            return
        if query.isdecimal():
            df2 = self.df[self.df.AtomicNumber == int(query)]
        else:
            df2 = self.df[
                self.df.Element.str.contains(f"^{query}", case=False, regex=True) |
                self.df.Symbol.str.contains(f"^{query}", case=False, regex=True)]
        elems = df2.index.to_list()
        if len(elems) == 1:
            self.elemPress(elems[0])
        else:
            self.clearHighlights()
            for widgets in self.info_grid.winfo_children():
                widgets.destroy()
            for i in elems:
                self.element_buttons[i].config(highlightbackground="yellow",
                                               highlightcolor="yellow")

    def setElement(self, root, idx, el, row, col):
        self.element_buttons.append(tkm.Button(
            root, text=f"{el.AtomicNumber}\n{el.Symbol}", fg="white",
            font=("Helvetica", 14, "bold"), borderwidth=0, highlightthickness=5,
            command=lambda i=idx: self.elemPress(i), height=32, width=32))
        self.element_buttons[-1].grid(row=row, column=col, padx=1, pady=1)

    def colorElements(self):
        color_dict = {"Nonmetal": "red", "Transactinide": "yellow green",
                      "Noble Gas": "purple", "Halogen": "gray", "Actinide": "dark red",
                      "Transition Metal": "green", "Metal": "lime green",
                      "Metalloid": "light green", "Alkaline Earth Metal": "orange",
                      "Alkali Metal": "dark orange", "Lanthanide": "dark green"}
        for i, el in self.df.iterrows():
            self.element_buttons[i].config(
                bg=color_dict[el.Type],
                bordercolor=color_dict[el.Type])

    def clearHighlights(self):
        for b in self.element_buttons:
            b.config(highlightbackground=b.cget("bg"))

    def elemPress(self, i):
        self.clearHighlights()
        self.element_buttons[i].config(highlightbackground="yellow",
                                       highlightcolor="yellow")
        rc = 0
        for key, value in self.df.loc[i, :].items():
            if str(value) == "<NA>":
                value = ""
            tk.Button()
            tk.Label(self.info_grid, text=f"{key}: ", borderwidth=1, anchor="e",
                     width=16, font=("Helvetica", 12, "normal")
                     ).grid(row=rc, column=0)

            tb: tk.Text = tk.Text(self.info_grid, wrap="none", borderwidth=1,
                                  height=1, width=20, font=("Helvetica", 12, "normal"))
            tb.insert(1.0, value)
            tb.grid(row=rc, column=1)
            tb.config(spacing1=1, state="disabled")
            rc += 1


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Periodic Table")
    pt = PeriodicTable(root)
    root.mainloop()

import tkinter as tk

class PeriodicTable:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        elements = [
            {'symbol': 'H', 'name': 'Hydrogen', 'number': 1},
            {'symbol': 'He', 'name': 'Helium', 'number': 2},
            {'symbol': 'Li', 'name': 'Lithium', 'number': 3},
            {'symbol': 'Be', 'name': 'Beryllium', 'number': 4},
            {'symbol': 'B', 'name': 'Boron', 'number': 5},
            {'symbol': 'C', 'name': 'Carbon', 'number': 6},
            {'symbol': 'N', 'name': 'Nitrogen', 'number': 7},
            {'symbol': 'O', 'name': 'Oxygen', 'number': 8},
            {'symbol': 'F', 'name': 'Fluorine', 'number': 9},
            {'symbol': 'Ne', 'name': 'Neon', 'number': 10}
        ]
        
        for element in elements:
            button = tk.Button(self.master, text=element['symbol'])
            button['command'] = lambda e=element: self.show_info(e)
            button.pack(side='left')

        self.info_label = tk.Label(self.master)
        self.info_label.pack(side='bottom')

    def show_info(self, element):
        info = f"{element['name']} ({element['symbol']}) has atomic number {element['number']}."
        self.info_label['text'] = info

if __name__ == '__main__':
    window = tk.Tk()
    table = PeriodicTable(window)
    window.mainloop()
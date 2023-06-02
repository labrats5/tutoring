import tkinter as tk
import tkinter.font as tkft
from tkinter import messagebox
import os
from PIL import Image, ImageTk

IMAGE_DIR = os.path.join(os.path.dirname(__file__), "froggies")


class SlideShow:
    def __init__(self, root: tk.Tk):
        self.image_dir = IMAGE_DIR
        try:
            self.images = os.listdir(self.image_dir)
        except FileNotFoundError as e:
            messagebox.showerror(message=e)
            root.destroy() 
        if not self.images:
            messagebox.showerror(message="No Images in this Directory")
            root.destroy()
        self.image_idx = 0
        self.img = self.getImage()
        self.menu_var = tk.StringVar(root, value=self.images[0])
        self.image_menu = tk.OptionMenu(root, self.menu_var, *self.images,
                                        command=self.menuSelect)  
        self.image_box = tk.Label(root, image=self.img)
        self.image_name = tk.Label(root, text=self.getImageName())
        self.first_button = tk.Button(root, text="<< First", command=self.firstClick)
        self.prev_button = tk.Button(root, text="< Prev", command=self.prevClick)
        self.next_button = tk.Button(root, text="Next >", command=self.nextClick)
        self.last_button = tk.Button(root, text="Last >>", command=self.lastClick)
        self.setButtonStatus()
        self.arrange()

    def setButtonStatus(self):
        # prev/first button.
        if self.image_idx == 0:
            self.prev_button.config(state='disabled')
            self.first_button.config(state='disabled')
        else:
            self.prev_button.config(state='normal')
            self.first_button.config(state='normal')
        # next/last button.
        if self.image_idx == len(self.images) - 1:
            self.next_button.config(state='disabled')
            self.last_button.config(state='disabled')
        else:
            self.next_button.config(state='normal')
            self.last_button.config(state='normal')

    def arrange(self):
        self.image_name.pack(pady=5)
        self.image_box.pack(padx=5)
        self.first_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.prev_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.last_button.pack(side=tk.RIGHT, padx=5, pady=5)
        self.next_button.pack(side=tk.RIGHT, padx=5, pady=5)
        self.image_menu.config(width=12)
        self.image_menu.pack(padx=5, pady=5)

    def getImageName(self) -> str:
        return f"{self.images[self.image_idx]} ({self.image_idx+1}/{len(self.images)})"

    def getImage(self) -> ImageTk.PhotoImage:
        fname = self.images[self.image_idx]
        img = Image.open(os.path.join(self.image_dir, fname))
        img = img.resize(size=(640, 600))
        return ImageTk.PhotoImage(img)
    
    def setImage(self, idx):
        self.image_idx = idx
        self.image_name.config(text=self.getImageName())
        self.img = self.getImage()
        self.image_box.config(image=self.img)
        self.menu_var.set(self.images[idx])
        self.setButtonStatus()
    
    def firstClick(self):
        self.setImage(0)

    def prevClick(self):
        self.setImage(self.image_idx - 1)

    def nextClick(self):
        self.setImage(self.image_idx + 1)

    def lastClick(self):
        self.setImage(len(self.images) - 1)

    def menuSelect(self, choice):
        self.setImage(self.images.index(choice))


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Slide Show")
    tkft.nametofont("TkDefaultFont").config(size=20)
    window = SlideShow(root)
    root.mainloop()

import tkinter as tk
import os
from PIL import Image, ImageTk

IMAGE_DIR = "/Users/maxwellcorbin/vs_stuff/kateryna/froggies"

def getImages(path):
    image_paths = os.listdir(path)
    for fname in image_paths:
        img = Image.open(os.path.join(path, fname))
        img = img.resize(size=(300, 300))
        yield img

def drawSlideShow():
    window = tk.Tk()
    imageIter = getImages(IMAGE_DIR)
    img = ImageTk.PhotoImage(next(imageIter))
    imageLabel = tk.Label(image=img)
    nextButton = tk.Button(command=lambda: next(imageIter))

    imageLabel.pack()
    nextButton.pack()
    window.mainloop()


if __name__ == '__main__':
    drawSlideShow()
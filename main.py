from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import photoEdition


class GUI:
    def __init__(self, c, tk):
        self.c = c
        self.tk = tk

    def main(self):
        self.rotate = Label(self.tk, text='Rotate: ', font=("ariel 17 bold"))
        self.rotate.place(x=630, y=65)
        angles = [0, 45, 90, 180, 270, 360]
        self.rotation = ttk.Combobox(self.tk, width=13, values=angles, font=('italic'))
        self.rotation.place(x=725, y=67)
        self.rotation.bind("<<ComboboxSelected>>", self.__rotatePhoto)

        self.waterMark = Label(self.tk, text='WaterMark: ', font=("ariel 17 bold"))
        self.waterMark.place(x=245, y=65)
        self.entry_text = Entry(self.tk, width=25)
        self.entry_text.place(x=380, y=73)
        self.button1 = Button(text='Print', font=('underline'), relief=RAISED, command=self.__waterMark)
        self.button1.place(x=535, y=65)

        self.resize = Label(self.tk, text='Size:', font=("ariel 17 bold"))
        self.resize.place(x=630, y=10)
        sizes = ['1920x1080', '1280x720', '1080x1080', '720x720', '640x360']
        self.resizing = ttk.Combobox(tk, width=13, values=sizes, font=('italic'))
        self.resizing.bind("<<ComboboxSelected>>", self.__resizePhoto)
        self.resizing.place(x=725, y=14)

        self.filter = Label(self.tk, text="Filter:", font=("ariel 17 bold"))
        self.filter.place(x=245, y=10)
        f = ['BLUR', 'CONTOUR', 'DETAIL', 'EMBOSS', 'EDGE_ENHANCE_MORE', 'FIND_EDGES', 'SHARPEN', 'SMOOTH']
        self.filters = ttk.Combobox(self.tk, width=23, values=f, font=("italic"))
        self.filters.bind("<<ComboboxSelected>>", self.__filterPhoto)
        self.filters.place(x=320, y=14)

        self.select = Button(self.tk, text='Select image', width=23, bg='SILVER', fg='BLUE', font=('underline'), relief=RAISED, command=self.__select)
        self.select.place(x=5, y=240)

        self.entryName = Label(self.tk, text='Save as: ', font=("ariel 12 bold"))
        self.entryName.place(x=1, y=297)
        self.entryFileName = Entry(self.tk, width=25)
        self.entryFileName.place(x=71, y=300)
        self.save = Button(self.tk, text='Save', width=23, bg='SILVER', fg='BLUE', font=('underline'), relief=RAISED, command=self.__save)
        self.save.place(x=5, y=320)

        self.exit = Button(self.tk, text='Exit', width=23, bg='SILVER', fg='BLUE', font=('underline'), relief=RAISED, command=self.tk.destroy)
        self.exit.place(x=5, y=370)

        img = ImageTk.PhotoImage(Image.open("font/logo.jpg"))
        self.logo = Label(self.tk, image=img)
        self.logo.place(x=0, y=0)
        
        self.tk.mainloop()

    def __select(self):
        self.img_path = filedialog.askopenfilename(initialdir=os.getcwd())
        self.image = Image.open(self.img_path)
        self.image.thumbnail((550, 600))
        self.img = ImageTk.PhotoImage(self.image)
        self.c.create_image(550, 350, image=self.img)
        self.c.image = self.img

    def __filterPhoto(self, filter):
        filter = self.filters.get()
        self.image = photoEdition.filterImage(self.image, filter)
        self.img = ImageTk.PhotoImage(self.image)
        self.c.create_image(550, 350, image=self.img)
        self.c.image = self.image

    def __resizePhoto(self, size):
        size = self.resizing.get()
        self.image = photoEdition.resize(self.image, size)
        self.image.thumbnail((550, 600))
        self.img = ImageTk.PhotoImage(self.image)
        self.c.create_image(550, 350, image=self.img)
        self.c.image = self.image

    def __waterMark(self):
        text = str(self.entry_text.get())
        self.image = photoEdition.waterMark(self.image, text)
        self.img = ImageTk.PhotoImage(self.image)
        self.c.create_image(550, 350, image=self.img)
        self.c.image = self.image

    def __rotatePhoto(self, angle):
        rotate = int(self.rotation.get())
        self.image = photoEdition.rotate(self.image, rotate)
        self.img = ImageTk.PhotoImage(self.image)
        self.c.create_image(550, 350, image=self.img)
        self.c.image = self.image

    def __save(self):
        filename = self.entryFileName.get()
        complete_name = os.path.join('./images', filename+'.png')
        self.image.save(complete_name)


tk = Tk()
tk.geometry("900x700")
tk.title('AUI Photo Editor')
c = Canvas(tk, width=900, height=700)
c.pack()

g = GUI(c, tk)
g.main()

from imgurpython import ImgurClient
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
from tkinter import messagebox


def upload_image(path):
    client = ImgurClient('ddcc8dbd63aee99', 'e03f8a161df5657e05d2d00152f672bf0da0df76')
    image = client.upload_from_path(path, anon=True)
    return image


class Window(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=4)
        self.create_variables()
        self.create_widgets()
        self.create_layout()
        self.bind_buttons()

    def create_variables(self):
        self.PathVar = tk.StringVar()
        self.LinkVar = tk.StringVar()

    def create_widgets(self):
        self.ChooseImageButton = ttk.Button(self, text='Choose image')
        self.PathEntry = tk.Entry(self, textvariable=self.PathVar)
        self.PathLabel = ttk.Label(self, text='Path to image:')
        self.UploadImageButton = ttk.Button(self, text='Upload image')
        self.LinkLabel = ttk.Label(self, text='Link to image')
        self.LinkEntry = tk.Entry(self, textvariable=self.LinkVar, state='readonly')

    def create_layout(self):
        self.PathLabel.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.PathEntry.grid(column=1, row=0, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.ChooseImageButton.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.UploadImageButton.grid(column=1, row=1, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.LinkLabel.grid(column=0, row=2, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.LinkEntry.grid(column=1, row=2, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.S, tk.N))
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.S, tk.N))

    def choose_file(self, event):
        self.PathVar.set(filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"))))

    def upload_image(self, event):
        if self.PathVar.get() != '':
            try:
                client = ImgurClient('ddcc8dbd63aee99', 'e03f8a161df5657e05d2d00152f672bf0da0df76')
                image = client.upload_from_path(self.PathVar.get(), anon=True)
                self.LinkVar.set(image['link'])
            except:
                messagebox.showerror('Error', 'Invalid path')

    def bind_buttons(self):
        self.ChooseImageButton.bind('<Button-1>', self.choose_file)
        self.UploadImageButton.bind('<Button-1>', self.upload_image)


root = tk.Tk()
Window(root)
root.geometry('500x80')
root.title('Image Uploader')
root.mainloop()

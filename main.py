#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import ttk, colorchooser, Menu, Spinbox, scrolledtext, messagebox as mb, filedialog as fd
import cv2

#===========================
# Main App
#===========================

class App(tk.Tk):
    """Main Application."""
    #--------------------------------------------
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.style = ttk.Style(self)

        self.init_UI()

    def init_UI(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.fieldset = ttk.LabelFrame(self.main_frame, text='Pencil Sketch Filter')
        self.fieldset.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        browse_btn = ttk.Button(self.fieldset, text='Browse Image', command=self.open_file)
        browse_btn.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        self.filepath = tk.StringVar()
        filepath_entry = ttk.Entry(self.fieldset, textvariable=self.filepath, width=50, state=tk.DISABLED)
        filepath_entry.grid(row=0, column=2, sticky=tk.W, padx=(0, 5), ipady=5)

        go_btn = ttk.Button(self.fieldset, text='Go', command=self.apply_filter)
        go_btn.grid(row=1, column=1, columnspan=2, sticky=tk.E, padx=5, pady=(0, 5))

    def open_file(self):
        """Open and loads the image file."""
        try:
            file_types = (('JPEG Files', '*.jpg'), ('PNG Files', '*.png'))
            self.filename = fd.askopenfilename(title='Open', initialdir='/', filetypes=file_types)
            self.filepath.set(self.filename)

        except Exception as e:
            return

    def apply_filter(self):
        try:
            img = cv2.imread(self.filename)

            # convert the image to grayscale
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            invert_gray_img = 255 - gray_img
            blurred_img  = cv2.GaussianBlur(invert_gray_img, (21, 21), 0)
            invert_blurred_img = 255 - blurred_img
            pencil_sketch_img = cv2.divide(gray_img, invert_blurred_img, scale=256.0)

            cv2.imshow('Pencil Sketch', pencil_sketch_img)
            cv2.waitKey(0)

        except Exception as e:
            mb.showerror('Exception', e)

#===========================
# Start GUI
#===========================

def main():
    pencil_sketch = App()
    pencil_sketch.title('Image To Sketch Version 1.0')
    pencil_sketch.iconbitmap('python.ico')
    pencil_sketch.style.theme_use('clam')
    pencil_sketch.mainloop()

if __name__ == '__main__':
    main()
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk, ImageGrab
from matplotlib import patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import time

import levelness

global upload
global lock
lock = False
upload = None

#from main import uploaded
if __name__ == "__main__":

    root = Tk()  # create root window
    root.title("Dysgraphia Initial Investigation Tool")  # title of the GUI window
    root.minsize(800, 700)
    root.config(bg="skyblue")  # specify background color

    # Create left and right frames
    #top_row = Frame(root, width = 200, height = 100, borderwidth=1)
    #top_row.grid(row=0, column = 2)

    #frame = Frame(root, width=50, height=500, bg = '#caf0f8', relief="solid", borderwidth=2)
    #frame.grid(row=0, column=0, padx=19, pady=5)

    #right_frame = Frame(root, width=500, height=300, bg = "#002C3E", relief="solid", borderwidth=2)
    #right_frame.grid(row=1, column=1, padx=5, pady=5)

    #root.rowconfigure(1, maxsize=20)





    # Create frames and labels in left_frame
    #Label(left_frame, text="Assessment Values", bg = '#caf0f8').grid(row=0, column=0, padx=5, pady=5)

    # load image to be "edited"
    def paint(event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        canvas.create_line(x1, y1, x2, y2, fill="white", width=5)
        canvas.update()


    canvas = tk.Canvas(root, bg="black", width=900, height=61)
    canvas.bind("<B1-Motion>", paint)
    canvas.grid(row=3, column=2, padx = 2, pady=20)

    def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        window.geometry(f"{width}x{height}+{x}+{y}")
        window_bg_color = "#002C3E"  # Change this to your desired background color
        root.configure(bg=window_bg_color)

    window_width = 1100
    window_height = 700

    center_window(root, window_width, window_height)
    #Label(right_frame, canvas).grid(row=0,column=0, padx=5, pady=5)

    canvas2 = tk.Canvas(root, width=100, height=50, bg="#002C3E", highlightthickness=0)
    canvas2.grid(row=0, column = 1, padx=0, pady=10, sticky = 'w')
    image2 = PhotoImage(file="title.png")
    image_label = tk.Label(root, image=image2, bg ='#002C3E')
    image_label.grid(row=0, column=2, padx=1, pady=1)

    canvas9 = tk.Canvas(root, width=5, height=5, bg="#002C3E", highlightthickness=0)
    canvas9.grid(row=0, column=1, padx=0, pady=10, sticky='w')
    image9 = PhotoImage(file="writing.png")
    resized_image = image9.subsample(5, 5)
    image_label9 = tk.Label(root, image=resized_image, bg='#002C3E')
    image_label9.grid(row=0, column=2, padx=1, pady=1, sticky = 'W', rowspan=3)

    Label(root, text="This system was created to investigate potential dysgraphia through handwriting. \nThis project is intended for project use only under Software Engineering.\nThis does not guarantee and shall not be a medical  basis for diagnosis of Dysgraphia",
          font= 'Bahnschrift' ,bg="#002C3E", fg = 'white').grid(row=2, column=2, padx=1)
    Label(root, text="Write your name here as input in printed form:", font= 'Bahnschrift' ,bg="#002C3E", fg = 'white').grid(row=4, column=2, padx=0, pady=0, sticky = 'nw')


    def start_loading():
        progress_bar.start()

        # Simulate a task that takes time
        for _ in range(75):
            time.sleep(0.05)  # Simulate some work
            progress_bar.step(1)
            root.update_idletasks()

        progress_bar.stop()

    style = ttk.Style()
    style.theme_use('alt')
    style.configure("TProgressbar", thickness=20, background = '#051e78')
    progress_bar = ttk.Progressbar(root, mode="determinate", length=300, style="TProgressbar")
    progress_bar.grid(row=4, column=2, padx=0, pady=0, sticky = 'ws')


    separator = ttk.Separator(root, orient='horizontal')
    separator.grid(row=5, column=2, padx=0, pady=10, sticky = 'ew')
    bold_font = ("Bahnschrift", 12, "bold")
    Label(root, text="RESULTS AND ANALYZATION:", font= bold_font ,bg="#002C3E", fg = 'white').grid(row=6, column=2, padx=0, pady=0, sticky = 'nw')
    Label(root, text="LABELS", font= bold_font ,bg="#002C3E", fg = 'white').grid(row=7, column=2, padx=0, pady=0, sticky = 'nw')
    Label(root, text="Baseline:", font= 'Bahnschrift' ,bg="#002C3E", fg = 'white').grid(row=8, column=2, padx=0, pady=0, sticky = 'nw')
    Label(root, text="?", font='Bahnschrift', bg="#002C3E", fg='#caf0f8').grid(row=8, column=2, padx=150, pady=0, sticky='w')
    Label(root, text="Letter Thickness:", font= 'Bahnschrift' ,bg="#002C3E", fg = 'white').grid(row=9, column=2, padx=0, pady=0, sticky = 'nw')
    Label(root, text="?", font='Bahnschrift', bg="#002C3E", fg='#caf0f8').grid(row=9, column=2, padx=150, pady=0, sticky='w')
    Label(root, text="Spacings: ", font= 'Bahnschrift' ,bg="#002C3E", fg = 'white').grid(row=10, column=2, padx=0, pady=0, sticky = 'nw')
    Label(root, text="?", font='Bahnschrift', bg="#002C3E", fg='#caf0f8').grid(row=10, column=2, padx=150, pady=0, sticky='w')
    Label(root, text=" ", font= 'Bahnschrift' ,bg="#002C3E", fg = 'white').grid(row=11, column=2, padx=0, pady=0, sticky = 'nw')
    Label(root, text="VALUES", font= bold_font ,bg="#002C3E", fg = 'white').grid(row=12, column=2, padx=0, pady=0, sticky = 'nw')
    Label(root, text="Baseline:", font= 'Bahnschrift' ,bg="#002C3E", fg = 'white').grid(row=13, column=2, padx=0, pady=0, sticky = 'nw')
    Label(root, text="Letter Thickness:", font= 'Bahnschrift' ,bg="#002C3E", fg = 'white').grid(row=14, column=2, padx=0, pady=0, sticky = 'nw')
    Label(root, text="Spacings: ", font= 'Bahnschrift' ,bg="#002C3E", fg = 'white').grid(row=15, column=2, padx=0, pady=0, sticky = 'nw')
    Label(root, text=" ", font= 'Bahnschrift' ,bg="#002C3E", fg = 'white').grid(row=16, column=2, padx=0, pady=0, sticky = 'nw')
    Label(root, text="PREDICTION", font= bold_font ,bg="#002C3E", fg = 'white').grid(row=17, column=2, padx=0, pady=0, sticky = 'nw')
    Label(root, text="Percentage of Low Potential Dysgraphia: ", font= 'Bahnschrift' ,bg="#002C3E", fg = 'white').grid(row=18, column=2, padx=0, pady=0, sticky = 'nw')
    Label(root, text="?", font='Bahnschrift', bg="#002C3E", fg='#caf0f8').grid(row=18, column=2, padx=320, pady=0, sticky='w')
    Label(root, text="Percentage of Potential Dysgraphia: ", font= 'Bahnschrift' ,bg="#002C3E", fg = 'white').grid(row=19, column=2, padx=0, pady=0, sticky = 'nw')
    Label(root, text="?", font='Bahnschrift', bg="#002C3E", fg='#caf0f8').grid(row=19, column=2, padx=320, pady=0, sticky='w')

    #Label(root, text="Letter Detected: ", font='Bahnschrift', bg="#002C3E", fg='white').grid(row=19, column=2, padx=230,pady=0, sticky='e')
    #Label(root, text='detected text will output here.', font='Bahnschrift', bg="#002C3E", fg='#caf0f8').grid(row=19, column=2, padx=10, pady=0,sticky='e')





    icon = Image.open("writing.png")
    iconresimage = icon.resize((80, 80))
    iconphoto = ImageTk.PhotoImage(iconresimage)
    #photo = ImageTk.PhotoImage(image)

    #image_label.grid(row=0, column=1, padx=10, pady=10)

    def save_canvas():
        import cv2

        start_loading()
        if lock is False:
            levelness.predictnow(upload, False)
        elif lock is True:
            levelness.predictnow(upload, True)
        from levelness import category1, category, category_thickness, probabilities, average_angle, std_dev_thickness, \
            std_dev, result_tesseract, image_tesseract, predictnow, image_path, text
        bold_font = ("Bahnschrift", 12, "bold")
        Label(root, text="RESULTS AND ANALYZATION:", font=bold_font, bg="#002C3E", fg='white').grid(row=6, column=2, padx=0,pady=0, sticky='nw')
        Label(root, text="LABELS", font=bold_font, bg="#002C3E", fg='white').grid(row=7, column=2, padx=0, pady=0,sticky='nw')

        Label(root, text="Baseline:", font='Bahnschrift', bg="#002C3E", fg='white').grid(row=8, column=2, padx=0, pady=0, sticky='nw')
        Label(root, text=category1.upper(), font='Bahnschrift', bg="#002C3E", fg='#eb9e34').grid(row=8, column=2, padx=150, pady=0, sticky='w')

        Label(root, text="Letter Thickness:", font='Bahnschrift', bg="#002C3E", fg='white').grid(row=9, column=2, padx=0,pady=0, sticky='nw')
        Label(root, text=category_thickness.upper(), font='Bahnschrift', bg="#002C3E", fg='#25a816').grid(row=9, column=2, padx=150, pady=0,sticky='w')

        Label(root, text="Spacings: ", font='Bahnschrift', bg="#002C3E", fg='white').grid(row=10, column=2, padx=0, pady=0,sticky='nw')
        Label(root, text=category.upper(), font='Bahnschrift', bg="#002C3E", fg='#e324ad').grid(row=10, column=2, padx=150, pady=0,sticky='w')

        Label(root, text=" ", font='Bahnschrift', bg="#002C3E", fg='white').grid(row=11, column=2, padx=0, pady=0,sticky='nw')
        Label(root, text="VALUES", font=bold_font, bg="#002C3E", fg='white').grid(row=12, column=2, padx=0, pady=0,sticky='nw')

        Label(root, text="Baseline:", font='Bahnschrift', bg="#002C3E", fg='white').grid(row=13, column=2, padx=0, pady=0,sticky='nw')
        Label(root, text=average_angle, font='Bahnschrift', bg="#002C3E", fg='#caf0f8').grid(row=13, column=2, padx=150, pady=0,sticky='w')

        Label(root, text="Letter Thickness:", font='Bahnschrift', bg="#002C3E", fg='white').grid(row=14, column=2, padx=0, pady=0, sticky='nw')
        Label(root, text=std_dev_thickness, font='Bahnschrift', bg="#002C3E", fg='#caf0f8').grid(row=14, column=2, padx=150, pady=0,sticky='w')

        Label(root, text="Spacings: ", font='Bahnschrift', bg="#002C3E", fg='white').grid(row=15, column=2, padx=0, pady=0,sticky='nw')
        Label(root, text=std_dev, font='Bahnschrift', bg="#002C3E", fg='#caf0f8').grid(row=15, column=2, padx=150,pady=0, sticky='w')

        Label(root, text=" ", font='Bahnschrift', bg="#002C3E", fg='white').grid(row=16, column=2, padx=0, pady=0,sticky='nw')
        Label(root, text="PREDICTION", font=bold_font, bg="#002C3E", fg='white').grid(row=17, column=2, padx=0, pady=0,sticky='nw')
        Label(root, text="Percentage of Low Potential Dysgraphia: ", font='Bahnschrift', bg="#002C3E", fg='white').grid(row=18, column=2, padx=0, pady=0, sticky='nw')
        Label(root, text=str(probabilities[0][0]) + " (Confidence Level)", font='Bahnschrift', bg="#002C3E", fg='#caf0f8').grid(row=18, column=2, padx=320,pady=0, sticky='w')
        Label(root, text="Percentage of Potential Dysgraphia: ", font='Bahnschrift', bg="#002C3E", fg='white').grid(row=19,column=2,padx=0,pady=0,sticky='nw')
        Label(root, text=str(probabilities[0][1]) + " (Confidence Level)", font='Bahnschrift', bg="#002C3E", fg='#caf0f8').grid(row=19, column=2,padx=320, pady=0,sticky='w')

        #Label(root, text="Letter Detected: ", font='Bahnschrift', bg="#002C3E", fg='white').grid(row=19, column=2,padx=230, pady=0,sticky='e')
        #Label(root, text=text, font='Bahnschrift', bg="#002C3E", fg='#caf0f8').grid(row=19, column=2,padx=10,pady=0,sticky='e')

        # Convert the PIL Image to a Tkinter PhotoImage
        fig, ax = plt.subplots(figsize = (6,1))
        ax.tick_params(axis='both', which='both', labelsize=10, colors = 'white')
        #fig.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)
        fig.set_facecolor('#002C3E')
        ax.set_facecolor('#002C3E')
        # 002C3E
        image2 = cv2.imread("paddleoutput.jpg")
        image_rgb = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        ax.imshow(image_rgb)
        canvas8 = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas8.get_tk_widget()
        canvas_widget.grid(row=3, column=2, columnspan=200, rowspan = 15, padx=360, pady=10, sticky="w")

        fig2, ax2 = plt.subplots(figsize = (6,1))
        ax2.tick_params(axis='both', which='both', labelsize=10, colors = 'white')
        #fig2.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)
        fig2.set_facecolor('#002C3E')
        ax2.set_facecolor('#002C3E')#002C3E

        for line in result_tesseract.split('\n'):
            if len(line.split()) == 6:
                char, x1, y1, x2, y2, _ = line.split()
                # Calculate letter thickness and spacing
                spacing = int(y2) - int(y1)
                thickness = int(x2) - int(x1)
                # Draw bounding box for each character
                rect = patches.Rectangle((int(x1), image_tesseract.shape[0] - int(y2)), int(x2) - int(x1),
                                         int(y2) - int(y1), linewidth=1, edgecolor='g', facecolor='none')
                ax2.add_patch(rect)
        ax2.imshow(image_tesseract)
        canvas9 = FigureCanvasTkAgg(fig2, master=root)
        canvas_widget2 = canvas9.get_tk_widget()
        canvas_widget2.grid(row=4, column=2, columnspan=200, rowspan = 200, padx=360, pady=220, sticky="w")





    def savetry():
        root.update()
        x = root.winfo_rootx() + canvas.winfo_x()
        y = root.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        # Grab the image and save it
        drawing = ImageGrab.grab(bbox=(x, y, x1, y1))

        # Save as a JPG file
        drawing.save("drawing.jpg")
        global lock
        lock = True


    def erase():
        canvas.delete("all")
        print("hehe: ", upload)


    def open_link(event):
        global upload
        file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
        if file_path:
            print(f"Selected file: {file_path}")
            upload = file_path
        global lock
        lock = False
        return file_path



    hyperlink_label = tk.Label(root, text="Upload a file", fg="white", cursor="hand2", bg='#002C3E', underline=True, font = 'Bahnschrift')
    hyperlink_label.bind("<Button-1>", open_link)
    hyperlink_label.grid(row=4, column=2, ipadx=5, pady=0, padx = 320, sticky = 'se')

    save_button = tk.Button(root, text="Predict", command=save_canvas, bd=0, height=2, width=15, bg='#0077b6', fg = 'white', font= 'Bahnschrift')
    save_button.grid(row=4, column=2, ipadx=5, pady=0, padx = 160, sticky = 'e')
    importbutton = tk.Button(root, text="Clear", command = erase, bd=0, height=2, width=6, bg='#BC3D41', fg = 'white', font= 'Bahnschrift')
    importbutton.grid(row=4, column=2, ipadx=5, pady=0, sticky = 'e')
    importbutton = tk.Button(root, text="Lock", command = savetry, bd=0, height=2, width=6, bg='#0077b6', fg = 'white', font= 'Bahnschrift')
    importbutton.grid(row=4, column=2, ipadx=5,padx = 80, pady=0, sticky = 'e')


    #fig, ax = plt.subplots(figsize = (2,2))
    #ax.tick_params(axis='both', which='both', labelsize=8, colors = 'white')
    #fig.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)
    #fig.set_facecolor('#002C3E')
    #ax.set_facecolor('#002C3E')
    #canvas8 = FigureCanvasTkAgg(fig, master=root)
    #canvas_widget = canvas8.get_tk_widget()
    #canvas_widget.grid(row=8, column=2, columnspan=2, rowspan = 10, padx=10, pady=10, sticky="e")

    #fig2, ax2 = plt.subplots(figsize = (2,2))
    #ax2.tick_params(axis='both', which='both', labelsize=8, colors = 'white')
    #fig2.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)
    #fig2.set_facecolor('#002C3E')
    #ax2.set_facecolor('#002C3E')
    #canvas9 = FigureCanvasTkAgg(fig2, master=root)
    #canvas_widget2 = canvas9.get_tk_widget()
    #canvas_widget2.grid(row=8, column=2, columnspan=2, rowspan = 10, padx=240, pady=10, sticky="e")


    # Example labels that could be displayed under the "Tool" menu
    #Label(root, text="Baseline:", bg="#90e0ef", font= 'Bahnschrift').grid(row=1, column=0, padx=5, pady=5, sticky="w")
    #Label(root, text="Spacing:", bg="#90e0ef", font= 'Bahnschrift').grid(row=2, column=0, padx=5, pady=5, sticky="w")
    #Label(root, text="Letter Thickness:", bg="#90e0ef", font= 'Bahnschrift').grid(row=3, column=0, padx=5, pady=5, sticky="w")
    #Label(root, text="Non-Dysgraphic Percentage:", bg="#90e0ef", font= 'Bahnschrift').grid(row=4, column=0, padx=5, pady=5, sticky="w")
    #Label(root, text="Dysgraphic Percentage:", bg="#90e0ef", font= 'Bahnschrift').grid(row=5, column=0, padx=5, pady=5, sticky="w")

    root.resizable(0, 0)
    root.mainloop()
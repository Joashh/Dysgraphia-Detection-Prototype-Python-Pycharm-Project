import tkinter as tk
from PIL import Image, ImageTk
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")
    window_bg_color = "#002C3E"  # Change this to your desired background color
    root.configure(bg=window_bg_color)
def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill="black", width=9)


root = tk.Tk()
root.title("Drawing Application")
root.resizable(0, 0)
# Set the width and height of the window
window_width = 1000
window_height = 500

center_window(root, window_width, window_height)

canvas = tk.Canvas(root, bg="white", width=700, height=300)
canvas.place(x=150, y=120)
canvas.bind("<B1-Motion>", paint)

title = Image.open("title.png")
icon = Image.open("writing.png")
iconresimage = icon.resize((80, 80))
iconphoto = ImageTk.PhotoImage(iconresimage)
photo = ImageTk.PhotoImage(title)

frame = tk.Frame(root)
frame.configure(bg="#002C3E")
frame.lower()
border_frame = tk.Frame(frame, relief="solid", borderwidth=2)
#border_frame.place(relwidth=1, relheight=1)
frame.pack(side=tk.TOP, anchor = tk.NW, padx = 120)


canvas2 = tk.Canvas(frame, width=iconphoto.width(), height=iconphoto.height())
canvas2.create_image(0, 0, anchor=tk.NW, image=iconphoto)
canvas2.configure(bg="#002C3E")
canvas2.config(highlightthickness=0)
canvas2.pack(side=tk.LEFT, anchor=tk.NW,  padx=12, pady=20)

canvas1 = tk.Canvas(frame, width=photo.width(), height=photo.height())
canvas1.create_image(0, 0, anchor=tk.NW, image=photo)
canvas1.configure(bg="#002C3E")
canvas1.config(highlightthickness=0)
canvas1.pack(side=tk.LEFT, anchor=tk.NW, padx=0, pady=50)



root.mainloop()
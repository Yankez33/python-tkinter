import tkinter as tk

root = tk.Tk()

# creates the canvas, canvas size and bg color
canvas = tk.Canvas(root, highlightbackground="white", width=300, height=300)
canvas.pack()

# creates the circle. The tuple contains the bounding box ( first 2 are top left x & y, next 2 are bottom right x & y
# )# fill makes bg color yellow
canvas.create_oval((0, 0, 300, 300), fill="yellow")

# create_arc is used to draw the eyes. Default arc size is 90 degrees. extent method with 180 makes it a half circle.
# fill colors them black
canvas.create_arc((50, 100, 100, 150), extent=180, fill="black")
canvas.create_arc((200, 100, 250, 150), extent=180, fill="black")

# draw-line is used to create the smile. Each line is one of the three lines used in the smile
canvas.create_line((50, 200, 110, 240), fill="red", width=5)
canvas.create_line((110, 240, 190, 240), fill="red", width=5)
canvas.create_line((190, 240, 250, 200), fill="red", width=5)


root.mainloop()
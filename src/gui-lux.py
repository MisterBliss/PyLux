import tkinter.filedialog
from src.lux_cls import Luxafor


lux = Luxafor()

def center_window(width, height):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def OnButtonClick(color):
    lux.set_clr_by_name(color)

root = tkinter.Tk()
center_window(400, 300)
root.title("Lux gui")
root.duration = tkinter.StringVar()
frame=tkinter.Frame(root)

num_colors = len(lux.colors.keys())
buttons = []

for clr in lux.colors.keys():
    buttons.append(tkinter.Button(frame, text=clr, command=lambda clr=clr: OnButtonClick(clr)))

buttons.append(tkinter.Button(frame, text="stop", command=lambda: OnButtonClick("no-color")))
i = 0
j = 0
for btn in buttons:
    btn.grid(column=i,row=j)
    if i < 2:
        i+=1
    else:
        j+=1
        i=0

frame.pack(pady=100)
root.mainloop()
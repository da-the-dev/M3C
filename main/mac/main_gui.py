import text_gui as text
from AnimatedGif import *
from Tkinter import *
from os import getcwd

root = Tk()
root.title("M3C")
########################################
way = getcwd()
########################################
mmbg = AnimatedGif(root, way + "/resources/mmbg.gif", 0.01)
mmbg.start()
mmbg.grid(row=0, columnspan=100)


########################################
def none():
    pass


########################################
def to_text():
    text.start()


########################################
Button(root, text="Text compiler", command=to_text).grid(row=1, column=0, sticky=W)
Button(root, text="NBT/Data tags", command=none).grid(row=1, column=1, sticky=W)
########################################
root.mainloop()
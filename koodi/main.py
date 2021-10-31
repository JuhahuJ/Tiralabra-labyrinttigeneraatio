from tkinter import Tk
from ui.ui import UI

ikkuna = Tk()
ikkuna.title("Labyrinttigeneraattori")

ui = UI(ikkuna)
ui.alku()

ikkuna.mainloop()

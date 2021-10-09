from tkinter import ttk, constants
import tkinter

class AloitusIkkuna:
    def __init__(self, root, syvyyshaku_kasittely):
        self._root = root
        self._frame = None
        self._syvyyshaku_kasittely = syvyyshaku_kasittely
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Tervetuloa labyrinttigeneraattoriin!")

        valittu_arvo = tkinter.StringVar(self._frame)
        valittu_arvo.set(3)

        val_lista = [3, 4, 5, 6, 7, 8, 9, 15, 24, 33, 38]

        koko_valinta = tkinter.OptionMenu(self._frame, valittu_arvo, *val_lista)

        button = ttk.Button(
            master=self._frame,
            text="Luo labyrintti syvyyshaulla",
            command=lambda : self._syvyyshaku_kasittely(valittu_arvo.get())
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)
        koko_valinta.grid(row=1, column=1)
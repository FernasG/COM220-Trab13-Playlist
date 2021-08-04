import tkinter as tk
import os.path
import pickle

class CtrlPlaylist():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        if not os.path.isfile("playlist.pickle"):
            self.listaPlaylist =  []
        else:
            with open("playlist.pickle", "rb") as f:
                self.listaPlaylist = pickle.load(f)

    def getListaPlaylist(self):
        return self.listaPlaylist

    def salvaPlaylist(self):
        if len(self.listaPlaylist) != 0:
            with open("playlist.pickle","wb") as f:
                pickle.dump(self.listaPlaylist, f)


class LimitePrincipal():
    def __init__(self, root, controle):
        self.sairMenu = tk.Menu(self.menubar)


        self.sairMenu.add_command(label="Salva", command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", menu=self.sairMenu)

class ControlePrincipal():
    def salvaDados(self):
        self.ctrlArtista.salvaArtista()
        self.ctrlAlbum.salvaAlbum()
        self.ctrlPlaylist.salvaPlaylist()
        self.root.destroy()


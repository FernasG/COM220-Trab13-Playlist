import tkinter as tk
import artista as art
import album as alb

class LimitePrincipal:
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x300')

        self.menubar = tk.Menu(self.root)
        self.artistaMenu = tk.Menu(self.menubar)
        self.albumMenu = tk.Menu(self.menubar)

        self.artistaMenu.add_command(label="Cadastrar", command=self.controle.cadastrarArtista)
        self.artistaMenu.add_command(label="Consultar", command=self.controle.consultarArtista)
        self.menubar.add_cascade(label="Artista", menu=self.artistaMenu)

        self.albumMenu.add_command(label="Cadastrar", command=self.controle.cadastrarAlbum)
        self.albumMenu.add_command(label="Consultar", command=self.controle.consultarAlbum)
        self.menubar.add_cascade(label="Álbum", menu=self.albumMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal:
    def __init__(self):
        self.root = tk.Tk()

        # add others controllers
        self.ctrlArtista = art.CtrlArtista()
        self.ctrlAlbum = alb.CtrlAlbum()

        self.limite = LimitePrincipal(self.root, self)
        self.root.title("Trab13 - Playlist")

        self.root.mainloop()
    
    def cadastrarArtista(self):
        self.ctrlArtista.cadastrarArtista()
    
    def consultarArtista(self):
        self.ctrlArtista.consultarArtista(self.ctrlAlbum)

    def cadastrarAlbum(self):
        self.ctrlAlbum.cadastrarAlbum(self.ctrlArtista)

    def consultarAlbum(self):
        self.ctrlAlbum.consultarAlbum()

if __name__=="__main__":
    c = ControlePrincipal()
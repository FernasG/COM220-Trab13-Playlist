import tkinter as tk
import artista as art
import album as alb
import playlist as pl

class LimitePrincipal:
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x300')

        self.menubar = tk.Menu(self.root)
        self.artistaMenu = tk.Menu(self.menubar)
        self.albumMenu = tk.Menu(self.menubar)
        self.playlistMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)

        self.artistaMenu.add_command(label="Cadastrar", command=self.controle.cadastrarArtista)
        self.artistaMenu.add_command(label="Consultar", command=self.controle.consultarArtista)
        self.menubar.add_cascade(label="Artista", menu=self.artistaMenu)

        self.albumMenu.add_command(label="Cadastrar", command=self.controle.cadastrarAlbum)
        self.albumMenu.add_command(label="Consultar", command=self.controle.consultarAlbum)
        self.menubar.add_cascade(label="Álbum", menu=self.albumMenu)

        self.playlistMenu.add_command(label="Cadastrar", command=self.controle.cadastrarPlaylist)
        self.playlistMenu.add_command(label="Consultar", command=self.controle.consultarPlaylist)
        self.menubar.add_cascade(label="Playlist", menu=self.playlistMenu)

        self.sairMenu.add_command(label="Salva", command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", menu=self.sairMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal:
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlArtista = art.CtrlArtista()
        self.ctrlAlbum = alb.CtrlAlbum()
        self.ctrlPlaylist = pl.CtrlPlaylist()

        self.limite = LimitePrincipal(self.root, self)
        self.root.title("Trab13 - Playlist")

        self.root.mainloop()

    def salvaDados(self):
        self.ctrlArtista.salvaArtista()
        self.ctrlAlbum.salvaAlbum()
        self.ctrlPlaylist.salvaPlaylist()
        self.root.destroy()
    
    #   Artista
    def cadastrarArtista(self):
        self.ctrlArtista.cadastrarArtista()
    
    def consultarArtista(self):
        self.ctrlArtista.consultarArtista(self.ctrlAlbum)

    #   Album
    def cadastrarAlbum(self):
        self.ctrlAlbum.cadastrarAlbum(self.ctrlArtista)

    def consultarAlbum(self):
        self.ctrlAlbum.consultarAlbum()

    #   Playlist
    def cadastrarPlaylist(self):
        self.ctrlPlaylist.cadastrarPlaylist(self.ctrlArtista, self.ctrlAlbum)

    def consultarPlaylist(self):
        self.ctrlPlaylist.consultarPlaylist()

if __name__=="__main__":
    c = ControlePrincipal()
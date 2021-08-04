import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pickle

class Playlist:
    def __init__(self, nome, musicas = []):
        self.__nome = nome
        self.__musicas = musicas
    
    def getNome(self):
        return self.__nome
    
    def getMusicas(self):
        return self.__musicas

class LimiteCadastrarPlaylist(tk.Toplevel):
    def __init__(self, controle, artistas):
        tk.Toplevel.__init__(self)
        self.geometry('400x300')
        self.title('Playlist - Cadastrar')
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameFaixas = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameTitulo.pack()
        self.frameArtista.pack()
        self.frameFaixas.pack()
        self.frameButton.pack()

        self.frameTitulo = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameFaixas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameTitulo.pack()
        self.frameArtista.pack()
        self.frameAno.pack()
        self.frameFaixas.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo, text="Titulo: ")
        self.labelTitulo.pack(side="left")
        
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")

        self.labelArtista = tk.Label(self.frameArtista, text="Artista: ")
        self.labelArtista.pack(side="left")

        self.comboboxArtistaValue = tk.StringVar()
        self.comboboxArtista = ttk.Combobox(self.frameArtista, textvariable=self.comboboxArtistaValue)
        self.comboboxArtista['values'] = artistas
        self.comboboxArtista.pack(side="left")
        self.comboboxArtista.bind("<<ComboboxSelected>>", controle.selectHandler)

        self.labelFaixas = tk.Label(self.frameFaixas, text="Lista de Músicas:")
        self.labelFaixas.pack()
        self.listboxSongs = tk.Listbox(self.frameFaixas)
        self.listboxSongs.pack()

        self.buttonSubmit = tk.Button(self.frameButton, text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.handleCadastrarPlaylist)

        self.buttonAddSong = tk.Button(self.frameButton, text="Adicionar")
        self.buttonAddSong.pack(side="left")
        self.buttonAddSong.bind("<Button>", controle.adicionarMusica)

        self.buttonClose = tk.Button(self.frameButton, text="Cancelar")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.cancelHandler)

class LimiteConsultaPlaylist(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('200x60')
        self.title('Playlist - Consultar')
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo, text="Titulo: ")
        self.labelTitulo.pack(side="left")

        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Consultar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.handleConsultarPlaylist)

        self.buttonClose = tk.Button(self.frameButton, text="Cancelar")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.cancelHandler)

class CtrlPlaylist:
    def __init__(self):
        self.listaPlaylists = []
        self.listaMusicasPlaylist = []
        self.musicasAux = []

    def cancelHandler(self, event = None):
        self.limiteIns.destroy()

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

    def consultarPlaylist(self):
        self.limiteIns = LimiteConsultaPlaylist(self)

    def salvaPlaylist(self):
        if len(self.listaPlaylist) != 0:
            with open("playlist.pickle","wb") as f:
                pickle.dump(self.listaPlaylist, f)


    def adicionarMusica(self, event):
        selectedSong = self.limiteIns.listboxSongs.get(tk.ACTIVE)

        if selectedSong:
            songName = selectedSong[selectedSong.find("- ")+2:]

            for faixa in self.musicasAux:
                if faixa.getTitulo() == selectedSong:
                    self.listaMusicasPlaylist.append(faixa)
                    self.mostraJanela('Sucesso', 'Música adicionada com sucesso!')

    def selectHandler(self, event):
        albuns = []
        artistaSelecionado = self.limiteIns.comboboxArtistaValue.get()
        self.limiteIns.listboxSongs.delete(0, tk.END)

        for artista in self.ctrlArtista.listaArtistas:
            if artista.getNome() == artistaSelecionado:
                for album in self.ctrlAlbum.listaAlbuns:
                    if album.getArtista() == artista:
                        albuns.append(album)

                for album in albuns:
                    for faixa in album.getFaixas():
                        self.musicasAux.append(faixa)
                        self.limiteIns.listboxSongs.insert(tk.END, f'{faixa.getNroFaixa()} - {faixa.getTitulo()}')

    def cadastrarPlaylist(self, ctrlArtista, ctrlAlbum):
        listaArtistas = []
        self.ctrlArtista = ctrlArtista
        self.ctrlAlbum = ctrlAlbum

        for artista in self.ctrlArtista.listaArtistas:
            listaArtistas.append(artista.getNome())
        
        if listaArtistas:
            self.limiteIns = LimiteCadastrarPlaylist(self, listaArtistas)
        else:
            self.mostraJanela('Erro', 'Cadastre um artista antes de cadastrar uma Playlist.')
    
    def handleCadastrarPlaylist(self, event):
        titulo = self.limiteIns.inputTitulo.get()

        if titulo and self.listaMusicasPlaylist:
            novaPlaylist = Playlist(titulo, self.listaMusicasPlaylist)

            self.listaPlaylists.append(novaPlaylist)
            self.listaMusicasPlaylist = []
            self.musicasAux = []

            self.mostraJanela('Sucesso', 'Playlist cadastrada com sucesso!')

        else:
            self.mostraJanela('Erro', 'Campos não preenchidos ou inválidos.')




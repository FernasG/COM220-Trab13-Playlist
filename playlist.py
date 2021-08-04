import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class Playlist:
    def __init__(self, nome):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome

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
        self.comboboxArtista.bind("<<ComboboxSelect>>", controle.selectHandler)
        self.comboboxArtista.pack(side="left")

        self.labelFaixas = tk.Label(self.frameFaixas, text="Lista de Músicas:")
        self.labelFaixas.pack()
        self.listboxSongs = tk.Listbox(self.frameFaixas)
        self.listboxSongs.pack()

        self.buttonSubmit = tk.Button(self.frameButton, text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.handleCadastrarPlaylist)

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

    def cancelHandler(self, event = None):
        self.limiteIns.destroy()

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

    def consultarPlaylist(self):
        self.limiteIns = LimiteConsultaPlaylist(self)

    def selectHandler(self):
        albuns = []
        artistaSelecionado = self.limiteIns.comboboxArtistaValue.get()

        for artista in self.limiteIns.ctrlArtista.listaArtistas:
            if artista.getNome() == artistaSelecionado:
                
                for album in self.limiteIns.ctrlAlbum.listaAlbuns:
                    if album.getArtista() == artista:
                        albuns.append(album)
                    
                for album in albuns:
                    for faixa in album.getFaixas():
                        print(faixa)
                        self.limiteIns.listboxSongs.insert(tk.END, f'{faixa.getNroFaixa()} - {faixa.getTitulo()}')

    # def adicionarMusica(self, event):
    #     songName = simpledialog.askstring('Música', 'Nome: ')

    #     if songName:
    #         self.limiteIns.albumId += 1
    #         self.limiteIns.listaFaixas.append(Musica(songName, self.limiteIns.albumId))
    #         self.limiteIns.listboxSongs.insert(tk.END, f'{self.limiteIns.albumId} - {songName}')

    def cadastrarPlaylist(self, ctrlArtista):
        listaArtistas = []
        self.ctrlArtista = ctrlArtista

        for artista in self.ctrlArtista.listaArtistas:
            listaArtistas.append(artista.getNome())
        
        if listaArtistas:
            self.limiteIns = LimiteCadastrarPlaylist(self, listaArtistas)
        else:
            self.mostraJanela('Erro', 'Cadastre um artista antes de cadastrar uma Playlist.')
    
    def handleCadastrarPlaylist(self, event):
        titulo = self.limiteIns.inputTitulo.get()
        artistaName = self.limiteIns.comboboxArtistaValue.get()
        faixas = self.limiteIns.listaFaixas

        if titulo and artistaName and faixas:
            found = None
            for artista in self.ctrlArtista.listaArtistas:
                if artista.getNome() == artistaName:
                    found = artista
                    break

            if found:
                novaPlaylist = Playlist(titulo, found, faixas)
                self.listaAlbuns.append(novaPlaylist)

                self.mostraJanela('Sucesso', 'Playlist cadastrado com sucesso!')
                self.cancelHandler()
            else:
                self.mostraJanela('Erro', 'Ocorreu um erro ao tentar criar a playlist')
        else:
            self.mostraJanela('Erro', 'Dado inválido ou não preenchido.')
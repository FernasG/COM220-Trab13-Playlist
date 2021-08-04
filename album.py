import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class Album:
    def __init__(self, titulo, ano, artista, faixas):
        self.__titulo = titulo
        self.__ano = ano
        self.__artista = artista
        self.__faixas = faixas

    def getTitulo(self):
        return self.__titulo

    def getAno(self):
        return self.__ano

    def getArtista(self):
        return self.__artista
    
    def getFaixas(self):
        return self.__faixas
    
class Musica:
    def __init__(self, titulo, nroFaixa):
        self.__titulo = titulo
        self.__nroFaixa = nroFaixa

    def getTitulo(self):
        return self.__titulo

    def getNroFaixa(self):
        return self.__nroFaixa

class LimiteCadastrarAlbum(tk.Toplevel):
    def __init__(self, controle, artistas):
        tk.Toplevel.__init__(self)
        self.geometry('400x300')
        self.title('Álbum - Cadastrar')
        self.controle = controle
        self.albumId = 0
        self.listaFaixas = []

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

        self.labelAno = tk.Label(self.frameAno, text="Ano: ")
        self.labelAno.pack(side="left")
        
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")

        self.labelFaixas = tk.Label(self.frameFaixas, text="Lista de Músicas:")
        self.labelFaixas.pack()
        self.listboxSongs = tk.Listbox(self.frameFaixas)
        self.listboxSongs.pack()

        self.buttonSubmit = tk.Button(self.frameButton, text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.handleCadastrarAlbum)

        self.buttonAddSong = tk.Button(self.frameButton, text="Adicionar Música")
        self.buttonAddSong.pack(side="left")
        self.buttonAddSong.bind("<Button>", controle.addSongHandler)

        self.buttonClose = tk.Button(self.frameButton, text="Cancelar")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.cancelHandler)

class LimiteConsultaAlbum(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('200x60')
        self.title('Álbum - Consultar')
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
        self.buttonSubmit.bind("<Button>", controle.handleConsultarAlbum)

        self.buttonClose = tk.Button(self.frameButton, text="Cancelar")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.cancelHandler)

class CtrlAlbum:
    def __init__(self):
        self.listaAlbuns = []

    def cadastrarAlbum(self, ctrlArtista):
        listaArtistas = []
        self.ctrlArtista = ctrlArtista

        for artista in self.ctrlArtista.listaArtistas:
            listaArtistas.append(artista.getNome())
        
        if listaArtistas:
            self.limiteIns = LimiteCadastrarAlbum(self, listaArtistas)
        else:
            self.mostraJanela('Erro', 'Cadastre um artista antes de cadastrar um álbum.')
    
    def consultarAlbum(self):
        self.limiteIns = LimiteConsultaAlbum(self)

    def handleCadastrarAlbum(self, event):
        titulo = self.limiteIns.inputTitulo.get()
        ano = self.limiteIns.inputAno.get()
        artistaName = self.limiteIns.comboboxArtistaValue.get()
        faixas = self.limiteIns.listaFaixas

        if titulo and ano and artistaName and faixas:
            found = None
            for artista in self.ctrlArtista.listaArtistas:
                if artista.getNome() == artistaName:
                    found = artista
                    break

            if found:
                novoAlbum = Album(titulo, ano, found, faixas)
                self.listaAlbuns.append(novoAlbum)

                self.mostraJanela('Sucesso', 'Álbum cadastrado com sucesso!')
                self.cancelHandler()
            else:
                self.mostraJanela('Erro', 'Ocorreu um erro ao tentar criar álbum')
        else:
            self.mostraJanela('Erro', 'Dado inválido ou não preenchido.')

    def handleConsultarAlbum(self, event):
        titulo = self.limiteIns.inputTitulo.get()

        if titulo:
            found = None

            for album in self.listaAlbuns:
                if album.getTitulo() == titulo:
                    found = album
                    break
            
            if found:
                faixasMsg = ''

                for faixa in found.getFaixas():
                    faixasMsg +=  f'\n{faixa.getNroFaixa()} - {faixa.getTitulo()}'
                
                self.mostraJanela('Sucesso', f'Álbum: {found.getTitulo()}\nArtista: {found.getArtista().getNome()}\nAno: {found.getAno()}\nFaixas: {faixasMsg}')
            else:
                self.mostraJanela('Erro', 'Álbum não encontrado.')
        else:
            self.mostraJanela('Erro', 'Titulo de álbum vázio ou incorreto.')

    def cancelHandler(self, event = None):
        self.limiteIns.destroy()

    def addSongHandler(self, event):
        songName = simpledialog.askstring('Música', 'Nome: ')

        if songName:
            self.limiteIns.albumId += 1
            self.limiteIns.listaFaixas.append(Musica(songName, self.limiteIns.albumId))
            self.limiteIns.listboxSongs.insert(tk.END, f'{self.limiteIns.albumId} - {songName}')

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

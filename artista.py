import tkinter as tk
from tkinter import messagebox

class Artista:
    def __init__(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

class LimiteCadastraArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('200x70')
        self.title('Artista - Cadastrar')
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.handleCadastrarArtista)

        self.buttonClose = tk.Button(self.frameButton, text="Cancelar")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.cancelHandler)

class LimiteConsultaArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('200x70')
        self.title('Artista - Consultar')
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Consultar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.handleConsultarArtista)

        self.buttonClose = tk.Button(self.frameButton, text="Cancelar")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.cancelHandler)

class CtrlArtista:
    def __init__(self):
        self.listaArtistas = []

    def cadastrarArtista(self):
        self.limiteIns = LimiteCadastraArtista(self)

    def consultarArtista(self):
        self.limiteIns = LimiteConsultaArtista(self)

    def handleCadastrarArtista(self, event):
        nome = self.limiteIns.inputNome.get()

        if nome:
            novoArtista = Artista(nome)
            self.listaArtistas.append(novoArtista)

            self.mostraJanela('Sucesso', 'Artista cadastrado com sucesso!')
            self.cancelHandler()
    
    def handleConsultarArtista(self, event):
        nome = self.limiteIns.inputNome.get()
        found = None

        if nome:
            for artista in self.listaArtistas:
                if artista.getNome() == nome:
                    found = artista
                    break

        if found:
            self.mostraJanela('Sucesso', f'Artista: {found.getNome()}\nAlbuns: ')

    def cancelHandler(self, event = None):
        self.limiteIns.destroy()

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
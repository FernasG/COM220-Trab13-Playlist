import tkinter as tk

class Album:
    def __init__(self, titulo, ano, artista):
        self.__titulo = titulo
        self.__ano = ano
        self.__artista = artista

    def getTitulo(self):
        return self.__titulo

    def getAno(self):
        return self.__ano

    def getArtista(self):
        return self.__artista

class LimiteCadastarAlbum(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('200x70')
        self.title('Álbum - Cadastrar')
        self.controle = controle

class CtrlAlbum:
    def __init__(self):
        self.__listaAlbuns = []

    def cadastarAlbum(self):
        self.limiteIns = LimiteCadastarAlbum(self)

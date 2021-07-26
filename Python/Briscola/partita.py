import sys
import numpy
import cv2 as cv
import tkinter as tk

class Giocatore:
    def __init__(self, nome, carte, punteggio, numerogiocatore, CPU, passo, chiamante, punteggiochiamato, chiamato):
        self.nome = nome
        self.carte = carte
        self.punteggio = punteggio
        self.numerogiocatore = numerogiocatore
        self.turnogiocatore = turnogiocatore
        self.CPU = CPU
        self.passo = chiamante
        self.chiamante = chiamante
        self.punteggiochiamato = punteggiochiamato
        self.chiamato = chiamato

    def scheda_personale(self):
        return f"Scheda Giocatore\n Nome:{self.nome}\n Ordine Giocatore:{self.turnogiocatore}"

giocatore1 = Giocatore
giocatore2 = Giocatore
giocatore3 = Giocatore
giocatore4 = Giocatore
CP = Giocatore

finestra = tk.Tk()

finestra.resizable(True,True)
finestra.title("Inserimento dati")
finestra.geometry("600x600")
finestra.configure(background= "green")

txt_out = tk.Label(finestra, text="Nome Giocatore 1:", fg="blue", font=("Roboto, 16"), padx=20)
txt_out.grid(row=0, column=0)
name = tk.Entry()
name.grid(row=0, column=1)
giocatore1.nome = name
txt_out = tk.Label(finestra, text="Turno Giocatore 1:", fg="blue", font=("Roboto, 16"), padx=20)
txt_out.grid(row=0, column=2)
num = tk.Entry()
num.grid(row=0, column=3)
giocatore1.turnogiocatore = num

txt_out = tk.Label(finestra, text="Nome Giocatore 2:", fg="blue", font=("Roboto, 16"), padx=20)
txt_out.grid(row=1, column=0)
name = tk.Entry()
name.grid(row=1, column=1)
giocatore2.nome = name
txt_out = tk.Label(finestra, text="Turno Giocatore 2:", fg="blue", font=("Roboto, 16"), padx=20)
txt_out.grid(row=1, column=2)
num = tk.Entry()
num.grid(row=1, column=3)
giocatore2.turnogiocatore = num

txt_out = tk.Label(finestra, text="Nome Giocatore 3:", fg="blue", font=("Roboto, 16"), padx=20)
txt_out.grid(row=2, column=0)
name = tk.Entry()
name.grid(row=2, column=1)
giocatore3.nome = name
txt_out = tk.Label(finestra, text="Turno Giocatore 3:", fg="blue", font=("Roboto, 16"), padx=20)
txt_out.grid(row=2, column=2)
num = tk.Entry()
num.grid(row=2, column=3)
giocatore3.turnogiocatore = num

txt_out = tk.Label(finestra, text="Nome Giocatore 4:", fg="blue", font=("Roboto, 16"), padx=20)
txt_out.grid(row=3, column=0)
name = tk.Entry()
name.grid(row=3, column=1)
giocatore4.nome = name
txt_out = tk.Label(finestra, text="Turno Giocatore 4:", fg="blue", font=("Roboto, 16"), padx=20)
txt_out.grid(row=3, column=2)
num = tk.Entry()
num.grid(row=3, column=3)
giocatore4.turnogiocatore = num

def printgiocatori():
    txt_out = tk.Label(finestra, text=giocatore1.nome, fg="blue", font=("Roboto, 16"), padx=20)
    txt_out.grid(row=0, column=3)
    txt_out = tk.Label(finestra, text=giocatore2.nome, fg="blue", font=("Roboto, 16"), padx=20)
    txt_out.grid(row=3, column=0)
    txt_out = tk.Label(finestra, text=giocatore3.nome, fg="blue", font=("Roboto, 16"), padx=20)
    txt_out.grid(row=3, column=6)
    txt_out = tk.Label(finestra, text=giocatore4.nome, fg="blue", font=("Roboto, 16"), padx=20)
    txt_out.grid(row=6, column=3)



start_button = tk.Button(text="Inizia!", command=printgiocatori())
start_button.grid(row=5, column=2)
if __name__ == "__main__":
    finestra.mainloop()
   
    



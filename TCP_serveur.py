import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading
import socket as s
import sys


# Fonction pour créer un socket serveur TCP
def socket_serveur(ip, s_type):
    for port in range(151, 65535):
        if s_type == 'TCP':
            serveur = s.socket(s.AF_INET, s.SOCK_STREAM)
        else:
            print("Erreur de type")
            return None

        try:
            serveur.bind((ip, port))
            print(f"Serveur lié à l'IP {ip} et au port {port}")
            serveur.listen()
            print('Serveur mis sur écoute')
            return serveur
        except s.error as err:
            print(f"Erreur lors de la liaison du serveur au port {port}: {err}")
            continue

    print('Aucun port disponible')
    return None


# Fonction pour envoyer des messages à tous les clients
def envoie(message):
    for cl in clients:
        cl.send(message)


# Fonction pour gérer les connexions clientes
def handle(cl):
    while True:
        try:
            message = cl.recv(1024)
            envoie(message)
        except:
            i = clients.index(cl)
            clients.remove(cl)
            cl.close()
            sn = surnoms[i]
            envoie(f'{sn} a quitté le chat!'.encode('utf-8'))
            surnoms.remove(sn)
            break


# Fonction pour recevoir les connexions entrantes
def recu():
    while True:
        cl, adresse = serveur.accept()
        console_text.insert(tk.END, f"Connecté avec {str(adresse)}\n")
        console_text.see(tk.END)

        cl.send('NICK'.encode('utf-8'))
        sn = cl.recv(1024).decode('utf-8')
        surnoms.append(sn)
        clients.append(cl)
        console_text.insert(tk.END, f"Surnom du client : {sn}!\n\n")
        console_text.see(tk.END)
        
        envoie(f'{sn} a rejoint le chat\n'.encode('utf-8'))
        cl.send('Connecté au serveur!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(cl,))
        thread.start()


#################### - Partie Tkinter - ###########################

# Classe pour rediriger les sorties de la console vers l'interface graphique Tkinter
class RedirectionConsole:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)


fenetre = tk.Tk()
fenetre.title("Console du Serveur")

console_text = ScrolledText(fenetre, height=20, width=50)
console_text.pack(expand=True, fill=tk.BOTH)

sys.stdout = RedirectionConsole(console_text)

ip, s_type = "", "TCP"
serveur = socket_serveur(ip, s_type)

clients = []
surnoms = []

thread_recu = threading.Thread(target=recu)
thread_recu.start()

fenetre.mainloop()

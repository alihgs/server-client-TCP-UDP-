import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading
import socket

# Adresse IP et port du serveur
IP_SERVEUR, PORT = '127.0.0.1', 54321

# Création du socket UDP
sserveur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sserveur.bind((IP_SERVEUR, PORT))

# Dictionnaire pour stocker les clients connectés
clients = {}

# Fonction pour mettre à jour l'affichage de la console
def update_console(message):
    console_text.insert(tk.END, message)
    console_text.see(tk.END)

# Fonction pour recevoir et traiter les messages des clients
def receive_messages():
    while True:
        data, client_address = sserveur.recvfrom(4096)
        data_decoded = data.decode()

        if client_address not in clients:
            update_console(f"Nouveau client connecté : {client_address}\n")
            clients[client_address] = data_decoded
        else:
            update_console(f"Message de {client_address}: {data_decoded}\n")

        # Envoi du message à tous les autres clients
        for client in clients:
            if client != client_address:
                sserveur.sendto(data, client)

# Interface graphique Tkinter
fenetre = tk.Tk()
fenetre.title("Console du Serveur UDP")

console_text = ScrolledText(fenetre, height=20, width=50)
console_text.pack(expand=True, fill=tk.BOTH)

# Lancement du thread pour recevoir les messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

fenetre.mainloop()

# Fermeture du socket UDP lorsque la fenêtre est fermée
sserveur.close()

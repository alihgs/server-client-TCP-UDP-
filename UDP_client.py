import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import socket
import threading

# Adresse IP et port du serveur
IP_SERVEUR, PORT = '127.0.0.1', 54321

# Fonction pour envoyer un message au serveur avec le surnom
def send_message(event=None):
    message = zone_saisie.get()
    zone_saisie.delete(0, tk.END)
    message_with_nickname = f"{surnom}: {message}"
    sclient.sendto(message_with_nickname.encode(), (IP_SERVEUR, PORT))

# Fonction pour recevoir les messages du serveur
def receive_message():
    while True:
        reponse, _ = sclient.recvfrom(4096)
        console_text.insert(tk.END, f"{reponse.decode()}\n")
        console_text.see(tk.END)

# Demander au client de choisir un surnom
surnom = input("Choisissez un surnom : ")

# Création du socket UDP
sclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Interface graphique Tkinter
fenetre = tk.Tk()
fenetre.title("Client du Chat UDP")

console_text = ScrolledText(fenetre, height=20, width=50)
console_text.pack(expand=True, fill=tk.BOTH)

zone_write = tk.Frame(fenetre)
zone_write.pack(side=tk.BOTTOM, fill=tk.X)

zone_saisie = tk.Entry(zone_write)
zone_saisie.pack(side=tk.LEFT, expand=True, fill=tk.X)
zone_saisie.bind("<Return>", send_message)

send_button = tk.Button(zone_write, text="Envoyer", command=send_message)
send_button.pack(side=tk.RIGHT)

# Lancement du thread pour recevoir les messages du serveur
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

# Démarrage de la boucle principale Tkinter
fenetre.mainloop()

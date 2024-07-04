import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import socket as s
import threading
import sys

def recu():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(surnom.encode('utf-8'))
            else:
                console_text.insert(tk.END, message + '\n')
                console_text.see(tk.END)
        except:
            print('Erreur')
            client.close()
            break

def ecrit(event=None):
    message = zone_saisie.get()
    zone_saisie.delete(0, tk.END)
    message = f"{surnom}: {message}"
    client.send(message.encode('utf-8'))
    

# Connexion au serveur
surnom = input("Choisissez un surnom : ")
client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(('127.0.0.1', 151))




#################### - Partie Tkinter - ###########################

# Redirection de la sortie vers la fenêtre de la console
class RedirectionConsole:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)


fenetre = tk.Tk()
fenetre.title("Client de Chat")

console_text = ScrolledText(fenetre, height=20, width=50)
console_text.pack(expand=True, fill=tk.BOTH)

zone_write = tk.Frame(fenetre)
zone_write.pack(side=tk.BOTTOM, fill=tk.X)

zone_saisie = tk.Entry(zone_write)
zone_saisie.pack(side=tk.LEFT, expand=True, fill=tk.X)
zone_saisie.bind("<Return>", ecrit)

send_button = tk.Button(zone_write, text="Envoyer", command=ecrit)
send_button.pack(side=tk.RIGHT)

sys.stdout = RedirectionConsole(console_text)

recu_thread = threading.Thread(target=recu)
recu_thread.start()

fenetre.mainloop()


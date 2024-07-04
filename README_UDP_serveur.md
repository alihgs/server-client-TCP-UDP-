# Serveur UDP avec Interface Graphique en Python

## Description
Ce script Python met en place un serveur UDP qui gère les communications réseau via une interface graphique Tkinter. Il permet de recevoir des messages de multiples clients, de les afficher dans une console graphique, et de redistribuer ces messages à tous les clients connectés.

## Fonctionnalités
- Réception et gestion de messages via un socket UDP.
- Affichage des messages et des connexions des clients dans une interface graphique.
- Redistribution des messages reçus à tous les clients connectés, à l'exception de l'émetteur.

## Comment l'utiliser
1. Assurez-vous que Python et Tkinter sont installés sur votre machine.
2. Téléchargez et enregistrez le script `UDP_serveur.py`.
3. Exécutez le script dans votre terminal ou invite de commande :
   ```bash
   python UDP_serveur.py
4. L'interface graphique se lancera, affichant les messages des clients ainsi que les notifications de nouvelles connexions.

## Dépendances
Python 3
Tkinter
Module socket pour la création et la gestion des sockets UDP.
Module threading pour la gestion des communications simultanées.

## Auteurs
- Anis NALLA 22104720
- Ali HARGAS 22104524
- Soufiane EL MOUSSAFER 21915493
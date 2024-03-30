import socket
import json

# Définir les données JSON à envoyer
json_data = {
    "request": "subscribe",
    "port": 3000,
    "name": "Ayoub",
    "matricules": ["21061", "68268"]
}

# Convertir les données JSON en chaîne
json_string = json.dumps(json_data)

# Définir l'adresse IP et le port du serveur local
server_address = ('localhost', 3000)

# Créer un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Établir la connexion au serveur
    s.connect(server_address)
    
    # Envoyer les données JSON encodées
    s.sendall(json_string.encode())
    print("Données JSON envoyées au serveur avec succès.")


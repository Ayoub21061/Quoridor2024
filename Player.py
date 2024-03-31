import socket
import json

# Les données JSON que je dois envoyer
json_data = {
    "request": "subscribe",
    "port": 8887,
    "name": "Ayoub",
    "matricules": ["21061", "68268"]
}

server_address = ('localhost', 3000)

# Création du socket pour la communication 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Établir la connexion au serveur
        s.connect(server_address)

        # J'envoie les données au serveur 
        json_string = json.dumps(json_data)
        s.sendall(json_string.encode())
        print("Données JSON envoyées au serveur avec succès.")
        
        # Attendre la réponse du serveur
        response = s.recv(2048)
        
        # Afficher la réponse du serveur
        print("Réponse du serveur:", response.decode())


# Opération du Ping-Pong
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('',8887)) 
    s.listen()
    while True:
            player, adress = s.accept()
            with player:
                server_request = player.recv(2048).decode()
                server_json = json.loads(server_request)
        
                # Vérifier si la requête est un ping
                if server_json["request"] == "ping":
                # Si c'est un ping, répondre avec un pong
                    response_pong = {"response": "pong"}
                    response_pong_json = json.dumps(response_pong)
                    player.sendall(response_pong_json.encode())
                    print("Pong envoyé au serveur en réponse à la requête de ping.")
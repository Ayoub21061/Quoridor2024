import socket
import json
import random
import time

def send_json_data(json_data, server_address):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server_address)
        json_string = json.dumps(json_data)
        s.sendall(json_string.encode())
        print("Données JSON envoyées au serveur avec succès.")
        response = s.recv(20480)
        print("Réponse du serveur:", response.decode())

def handle_ping_pong():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 8887))
        s.listen()
        while True:
            player, address = s.accept()
            with player:
                server_request = player.recv(2048).decode()
                server_json = json.loads(server_request)
                print("Requête du serveur:", server_json)
                if server_json["request"] == "ping":
                    response_pong = {"response": "pong"}
                    response_pong_json = json.dumps(response_pong)
                    player.sendall(response_pong_json.encode())
                    print("Pong envoyé au serveur en réponse à la requête de ping.")
                elif server_json["request"] == "play":
                    response_move_string = {"response": "move", "move": "player_move", "message": "J'attends ton coup"}
                    print(response_move_string)
                    response_move_json = json.dumps(response_move_string)
                    player.sendall(response_move_json.encode())
                    print("Coup joué et réponse envoyée au serveur.")


# Les données JSON que je dois envoyer
json_data = {
    "request": "subscribe",
    "port": 8887,
    "name": "Ayoub",
    "matricules": ["21061", "68268"]
}

# Définir l'adresse IP et le port du serveur local
server_address = ('localhost', 3000)

send_json_data(json_data, server_address)
handle_ping_pong()

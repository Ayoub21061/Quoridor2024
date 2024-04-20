import socket
import json
import random

def send_json_data(json_data, server_address):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(server_address)
        json_string = json.dumps(json_data)
        s.sendall(json_string.encode())
        print("Données JSON envoyées au serveur avec succès.")
        response = s.recv(20480)
        print("Réponse du serveur:", response.decode())

def player_mover(server_json):

    board = server_json["state"]["board"]

    player = server_json['state']['current'] # 0 ou 1
    position = get_position(server_json, player) 
    move_available = callfunction(board, position) # [True, True, False, True]
    print(move_available)
    #randommove = get_random_true_index(move_available)# 0 as True
    listmoveavailable = get_list_position_true_index(move_available)
    if player == 0:
        if 3 in listmoveavailable:
            return down_move(position)
        elif 1 in listmoveavailable and 0 in listmoveavailable:
            return random.choice([left_move(position), right_move(position)]) 
        elif 1 in listmoveavailable:
            return left_move(position)
        elif 0 in listmoveavailable:
            return right_move(position)
        elif 2 in listmoveavailable:
            return up_move(position)
    else:
        if 2 in listmoveavailable:
            return up_move(position)
        elif 1 in listmoveavailable and 0 in listmoveavailable:
            return random.choice([left_move(position), right_move(position)]) 
        elif 1 in listmoveavailable:
            return left_move(position)
        elif 0 in listmoveavailable:
            return right_move(position)
        elif 3 in listmoveavailable:
            return down_move(position)

        



def right_move(position):

    return {
    "type": "pawn", 
    "position": [[position[0], position[1] + 2]]
  }

def left_move(position):

    return {
    "type": "pawn", 
    "position": [[position[0], position[1] - 2]]
  }
    
def up_move(position):

    return {
    "type": "pawn", 
    "position": [[position[0] - 2, position[1]]]
  }
    
def down_move(position):

    return {
    "type": "pawn", 
    "position": [[position[0] + 2, position[1]]]
  }

  
def get_random_true_index(move_available):
    true_indices = [i for i, val in enumerate(move_available) if val]  # Obtient les indices des éléments True
    return random.choice(true_indices)  # Retourne un indice aléatoire parmi les éléments True

def get_list_position_true_index(move_available):
    return [i for i, val in enumerate(move_available) if val]


def right_available(board, position):
    if position[1] + 2 > 16 or position[1] + 1 > 16:
        return False
    else:
        listcase = board[position[0]] # Je récupère la liste dans laquelle je me trouve mais dans logique du jeu je regarde le déplacement horizontale 
        print(listcase)
        if listcase[position[1]+ 1] == 3 and listcase[position[1]+ 2] == 2: # Si je me déplaces à droite et que c'est un blocker vide et que c'est une case vide 
            return True
        else:
            return False
    
def left_available(board, position):
    if position[1] - 2 < 0 or position[1] - 1 < 0:
        return False
    else:
        listcase = board[position[0]] # Je récupère la liste dans laquelle je me trouve mais dans logique du jeu je regarde le déplacement horizontale 
        if listcase[position[1]- 1] == 3 and listcase[position[1]- 2] == 2: # Si je me déplaces à gauche et que c'est un blocker vide et que c'est une case vide 
            return True
        else:
            return False

def up_available(board, position):
    if position[0] - 2 < 0 or position[0] - 1 < 0:
        return False
    else:
        listcase = board[position[0]-2] # Je récupère la liste dans laquelle je me trouve mais dans logique du jeu je regarde le déplacement verticale 
        print(f'listcase{listcase}')
        listblocker = board[position[0]-1] # La liste où il y'a le blocker
        if listblocker[position[1]] == 3 and listcase[position[1]] == 2: # Si je me déplaces en haut et que c'est un blocker vide et que c'est une case vide 
            return True
        else:
            return False

def down_available(board, position):
    if position[0] + 2 > 16 or position[0] + 1 > 16:
        return False
    else:
        listcase = board[position[0]+2] # Je récupère la liste dans laquelle je me trouve mais dans logique du jeu je regarde le déplacement verticale 
        print(f'listcase{listcase}')
        listblocker = board[position[0]+1] # La liste où il y'a le blocker
        if listblocker[position[1]] == 3 and listcase[position[1]] == 2: # Si je me déplaces en bas et que c'est un blocker vide et que c'est une case vide 
            return True
        else:
            return False
    
def callfunction(board, position):
    listefunction = []
    listefunction.append(right_available(board, position))
    listefunction.append(left_available(board, position))
    listefunction.append(up_available(board, position))
    listefunction.append(down_available(board, position))
    return listefunction


def get_position(server_json, player): # Indique position de où je suis 
    board = server_json["state"]["board"]

# [0,8] pour 0 et [16,8] pour 1
    for indicelist, elem in enumerate(board):  # Parcourt les 17 listes 
        print(f'player{player}')
        if player in elem:  # Vérifie si zéro est présent dans la liste
            pos_in_list = elem.index(player)  # Obtient la position de zéro dans la liste
            print(f'positionduplayer{[indicelist, pos_in_list] }')
            return [indicelist, pos_in_list]  # Renvoie le numéro de la liste et la position de zéro dans cette liste

def handle_ping_pong():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 8850))
        s.listen()
        while True:
            player, address = s.accept()
            with player:
                server_request = player.recv(20480).decode()
                server_json = json.loads(server_request)
                print("Requête du serveur:", server_json)
                if server_json["request"] == "ping":
                    response_pong = {"response": "pong"}
                    response_pong_json = json.dumps(response_pong)
                    player.sendall(response_pong_json.encode())
                    #print("Pong envoyé au serveur en réponse à la requête de ping.")
                elif server_json["request"] == "play":
                    lives = server_json["lives"]
                    state = server_json["state"]
                    errors = server_json["errors"]
                    player_move = player_mover(server_json)
                    response_move_string = {"response": "move", "move": player_move, "message": "Too far for Ronaldo to think about it"}
                    print(response_move_string)
                    response_move_json = json.dumps(response_move_string)
                    player.sendall(response_move_json.encode())
                    #print("Coup joué et réponse envoyée au serveur.")


# Les données JSON que je dois envoyer
json_data = {
    "request": "subscribe",
    "port": 8850,
    "name": "Ayoub",
    "matricules": ["21061", "52643"]
}

# Définir l'adresse IP et le port du serveur local
server_address = ('localhost', 3000)

send_json_data(json_data, server_address)
handle_ping_pong()

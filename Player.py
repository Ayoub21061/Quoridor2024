import socket
import json
import random

move_played = 0
message = "Too far for Ronaldo to think about it"

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
    blockeravailable = server_json['state']['blockers'][player]
    play = moveorblocker(blockeravailable)
    if play == 'blocker':
        opponent_player = get_opponent_player(player)
        opponent_position = get_position(server_json, opponent_player)
        if opponent_player == 0:
            listblockeravailable = board[opponent_position[0] + 1]
            if listblockeravailable[opponent_position[1]] == 3:
                if opponent_position[1] < 2:
                    if listblockeravailable[2] == 3:
                        blockerlist = opponent_position[0] + 1 # [0,8] -> 0 -> 0 + 1 -> 1
                        pos1 = 0
                        pos2 = 2
                        return play_blocker(blockerlist, pos1, pos2)
                elif opponent_position[1] > 14:
                    if listblockeravailable[14] == 3:
                        blockerlist = opponent_position[0] + 1 # [0,8] -> 0 -> 0 + 1 -> 1
                        pos1 = 14
                        pos2 = 16
                        return play_blocker(blockerlist, pos1, pos2)
                else:
                    leftorrightavailable = listposblockeravailable(listblockeravailable, opponent_position[1])
                    true_indices = [i for i, val in enumerate(leftorrightavailable) if val]
                    if len(true_indices) == 2:
                        index = random.choice(true_indices)
                    elif len(true_indices) == 1:
                        index = true_indices[0]
                    elif len(true_indices) == 0:
                        play = 'move'

                    if index == 0:
                        pos1 = opponent_position[1] - 2 
                        pos2 = opponent_position[1]
                        blockerlist = opponent_position[0] + 1
                        return play_blocker(blockerlist, pos1, pos2)
                    elif index == 1:
                        pos1 = opponent_position[1] + 2
                        pos2 = opponent_position[1]
                        blockerlist = opponent_position[0] + 1
                        return play_blocker(blockerlist, pos1, pos2)
            else:
                play = 'move' 
                print('Peut pas mettre de Blocker')       
        else:
            listblockeravailable = board[opponent_position[0] - 1]
            if listblockeravailable[opponent_position[1]] == 3:
                if opponent_position[1] < 2:
                    if listblockeravailable[2] == 3:
                        blockerlist = opponent_position[0] - 1 # [16,8] -> 16 -> 16 - 1 -> 15
                        pos1 = 0
                        pos2 = 2
                        return play_blocker(blockerlist, pos1, pos2)
                elif opponent_position[1] > 14:
                    if listblockeravailable[14] == 3:
                        blockerlist = opponent_position[0] - 1 # [0,8] -> 0 -> 0 + 1 -> 1
                        pos1 = 14
                        pos2 = 16
                        return play_blocker(blockerlist, pos1, pos2)
                else:
                    leftorrightavailable = listposblockeravailable(listblockeravailable, opponent_position[1])
                    true_indices = [i for i, val in enumerate(leftorrightavailable) if val]
                    if len(true_indices) == 2:
                        index = random.choice(true_indices)
                    elif len(true_indices) == 1:
                        index = true_indices[0]
                    elif len(true_indices) == 0:
                        play = 'move'
                    if index == 0:
                        pos1 = opponent_position[1] - 2 
                        pos2 = opponent_position[1]
                        blockerlist = opponent_position[0] - 1
                        return play_blocker(blockerlist, pos1, pos2)
                    elif index == 1:
                        pos1 = opponent_position[1] + 2
                        pos2 = opponent_position[1]
                        blockerlist = opponent_position[0] - 1
                        return play_blocker(blockerlist, pos1, pos2)
            else:
                play = 'move'
                print('Peut pas mettre de Blocker')

    if play == 'move':
        print('On a move')
        opponent_player = get_opponent_player(player) 
        move_available = callfunction(board, position, opponent_player) # [True, True, False, True]
        #randommove = get_random_true_index(move_available)# 0 as True
        listmoveavailable = get_list_position_true_index(move_available)
        if player == 0:
            if 3 in listmoveavailable:
                return down_move(position)
            elif 7 in listmoveavailable:
                return down_jump_move(position)
            elif 4 in listmoveavailable:
                return right_jump_move(position)
            elif 5 in listmoveavailable:
                return left_jump_move(position)
            elif 1 in listmoveavailable and 0 in listmoveavailable:
                return random.choice([left_move(position), right_move(position)]) 
            elif 1 in listmoveavailable:
                return left_move(position)
            elif 0 in listmoveavailable:
                return right_move(position)
            elif 2 in listmoveavailable:
                return up_move(position)
            elif 6 in listmoveavailable:
                return up_jump_move(position)
        else:
            if 2 in listmoveavailable:
                return up_move(position)
            elif 6 in listmoveavailable:
                return up_jump_move(position)
            elif 4 in listmoveavailable:
                return right_jump_move(position)
            elif 5 in listmoveavailable:
                return left_jump_move(position)
            elif 1 in listmoveavailable and 0 in listmoveavailable:
                return random.choice([left_move(position), right_move(position)]) 
            elif 1 in listmoveavailable:
                return left_move(position)
            elif 0 in listmoveavailable:
                return right_move(position)
            elif 3 in listmoveavailable:
                return down_move(position)
            elif 7 in listmoveavailable:
                return down_jump_move(position)
            

def listposblockeravailable(listblockeravailable, posblocker):
    result = []
    result.append(blocker_left(listblockeravailable, posblocker))
    result.append(blocker_right(listblockeravailable, posblocker))
    return result

def blocker_left(listeblockeravailable, posblocker):
    if listeblockeravailable[posblocker - 2] == 3:
        return True 
    else:
        return False


def blocker_right(listeblockeravailable, posblocker):
    if listeblockeravailable[posblocker + 2] == 3:
        return True 
    else:
        return False
    

def play_blocker(blockerlist, pos1, pos2):
    return {
    "type": "blocker", 
    "position": [[blockerlist,pos1], [blockerlist,pos2]]  
}


def get_opponent_player(player):
    if player == 0:
        return 1
    else:
        return 0   

def moveorblocker(blockeravailable):
    global move_played
    move_played += 1
    if blockeravailable == 0:
        return 'move'
    elif move_played % 2 == 0:
        return 'blocker'
    else:
        return 'move'


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

def right_jump_move(position):
    global message
    message = "Hop"
    return {
    "type": "pawn", 
    "position": [[position[0], position[1] + 4]]
  }

def left_jump_move(position):
    global message
    message = "Hop"
    return {
    "type": "pawn", 
    "position": [[position[0], position[1] - 4]]
  }

def up_jump_move(position):
    global message
    message = "Hop"
    return {
    "type": "pawn", 
    "position": [[position[0] - 4, position[1]]]
  }

def down_jump_move(position):
    global message
    message = "Hop"
    return {
    "type": "pawn", 
    "position": [[position[0] + 4, position[1]]]
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
        
def right_jump_available(board, position, opponent_player):
    if position[1] >= 14 :
        return False
    else:
        listcase = board[position[0]]
        # position = [2,8]
        # position[0] = 2
        # board[0] = liste d'indice 0
        # board[position[0]] = board[2] = liste d'indice 2
        if listcase[position[1] + 2] == opponent_player: 
            return True
        else:
            return False
        
def left_jump_available(board, position, opponent_player):
    if position[1] <= 2 :
        return False
    else:
        listcase = board[position[0]]
        if listcase[position[1] - 2] == opponent_player:
            return True
        else:
            return False
        
def up_jump_available(board, position, opponent_player):
    if position[0] <= 2 :
        return False
    else:
        listcase = board[position[0] - 2]
        if listcase[position[1]] == opponent_player:
            return True
        else:
            return False
        
def down_jump_available(board, position, opponent_player):
    if position[0] >= 14 :
        return False
    else:
        listcase = board[position[0] + 2]
        if listcase[position[1]] == opponent_player:
            return True
        else:
            return False
    
    
    
def callfunction(board, position, opponent_player):
    listefunction = []
    listefunction.append(right_available(board, position))
    listefunction.append(left_available(board, position))
    listefunction.append(up_available(board, position))
    listefunction.append(down_available(board, position))
    listefunction.append(right_jump_available(board,position,opponent_player))
    listefunction.append(left_jump_available(board,position,opponent_player))
    listefunction.append(up_jump_available(board,position,opponent_player))
    listefunction.append(down_jump_available(board,position,opponent_player))
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
                    print(player_move)
                    global message
                    response_move_string = {"response": "move", "move": player_move, "message": message}
                    message = "Too far for Ronaldo to think about it"
                    print(response_move_string)
                    response_move_json = json.dumps(response_move_string)
                    player.sendall(response_move_json.encode())
                    #print("Coup joué et réponse envoyée au serveur.")
                    

# Les données JSON que je dois envoyer
json_data = {
    "request": "subscribe",
    "port": 8850,
    "name": "Blocker",
    "matricules": ["21061", "52643"]
}

# Définir l'adresse IP et le port du serveur local
server_address = ('localhost', 3000)

send_json_data(json_data, server_address)
handle_ping_pong()

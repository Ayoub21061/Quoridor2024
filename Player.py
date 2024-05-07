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
        response = s.recv(204800)
        #print("Réponse du serveur:", response.decode())
        # with open("partie5.txt", "a") as fichier:
        #     fichier.write(str(response.decode())+"\n")



def player_mover(server_json):

    board = server_json["state"]["board"]
    
    player = server_json['state']['current'] # 0 ou 1
    position = get_position(server_json, player)
    blockeravailable = server_json['state']['blockers'][player]
    play = moveorblocker(blockeravailable)
    #play = "blocker"
    if play == 'blocker':
        opponent_player = get_opponent_player(player)
        opponent_position = get_position(server_json, opponent_player)
        if opponent_player == 0:
            listblockeravailable = board[opponent_position[0] + 1]
            listblockeravailabledown = board[opponent_position[0]]
            listblockeravailableup = board[opponent_position[0] + 2]
            if listblockeravailable[opponent_position[1]] == 3:
                if opponent_position[1] < 2:
                    if listblockeravailable[2] == 3:
                        blockerlist = opponent_position[0] + 1 # [0,8] -> 0 -> 0 + 1 -> 1
                        pos1 = 0
                        pos2 = 2
                        return play_blocker(blockerlist, pos1, pos2)
                    else :
                        play = "move"
                elif opponent_position[1] > 14:
                    if listblockeravailable[14] == 3:
                        blockerlist = opponent_position[0] + 1 # [0,8] -> 0 -> 0 + 1 -> 1
                        pos1 = 14
                        pos2 = 16
                        return play_blocker(blockerlist, pos1, pos2)
                    else :
                        play = "move"
                else:
                    leftorrightavailable = listposblockeravailable(listblockeravailable, board, opponent_position[1], opponent_position[0], listblockeravailableup, listblockeravailabledown)
                    true_indices = [i for i, val in enumerate(leftorrightavailable) if val]
                    if 0 in true_indices:
                        index = 0
                    elif 1 in true_indices:
                        index = 1
                    elif 2 in true_indices:
                        index = 2
                    elif 3 in true_indices:
                        index = 3
                    elif 4 in true_indices:
                        index = 4
                    elif 5 in true_indices:
                        index = 5
                    else:
                        play = 'move'

                    if index == 0:
                        pos1 = opponent_position[1] - 2 
                        pos2 = opponent_position[1]
                        blockerlist = opponent_position[0] + 1
                        return play_blocker(blockerlist, pos1, pos2)
                    elif index == 1:
                        pos1 = opponent_position[1] 
                        pos2 = opponent_position[1] + 2
                        blockerlist = opponent_position[0] + 1
                        return play_blocker(blockerlist, pos1, pos2)
                    elif index == 2:
                        pos1 = opponent_position[1] - 1
                        pos2 = opponent_position[1] - 1
                        blockerlist = opponent_position[0] 
                        blockerlist2 = opponent_position[0] - 2
                        return play_blocker_vertical(blockerlist, blockerlist2, pos1, pos2)
                    elif index == 3:
                        pos1 = opponent_position[1] + 1
                        pos2 = opponent_position[1] + 1
                        blockerlist = opponent_position[0] 
                        blockerlist2 = opponent_position[0] - 2
                        return play_blocker_vertical(blockerlist, blockerlist2, pos1, pos2)
                    elif index == 4:
                        pos1 = opponent_position[1] - 1
                        pos2 = pos1
                        blockerlist = opponent_position[0]
                        blockerlist2 = opponent_position[0] + 2
                        return play_blocker_vertical(blockerlist, blockerlist2, pos1, pos2) 
                    elif index == 5:
                        pos1 = opponent_position[1] + 1
                        pos2 = pos1
                        blockerlist = opponent_position[0]
                        blockerlist2 = opponent_position[0] + 2 
                        return play_blocker_vertical(blockerlist, blockerlist2, pos1, pos2)
            else:
                play = 'move' 
                print('Peut pas mettre de Blocker')       
        else:
            listblockeravailable = board[opponent_position[0] - 1]
            listblockeravailabledown = board[opponent_position[0]]
            listblockeravailableup = board[opponent_position[0] - 2]
            if listblockeravailable[opponent_position[1]] == 3:
                if opponent_position[1] < 2:
                    if listblockeravailable[2] == 3:
                        blockerlist = opponent_position[0] - 1 # [16,8] -> 16 -> 16 - 1 -> 15
                        pos1 = 0
                        pos2 = 2
                        return play_blocker(blockerlist, pos1, pos2)
                    else : 
                        play = "move"
                elif opponent_position[1] > 14:
                    if listblockeravailable[14] == 3:
                        blockerlist = opponent_position[0] - 1 # [0,8] -> 0 -> 0 + 1 -> 1
                        pos1 = 14
                        pos2 = 16
                        return play_blocker(blockerlist, pos1, pos2)
                    else :
                        play = "move"
                else:
                    leftorrightavailable = listposblockeravailable(listblockeravailable, board, opponent_position[1], opponent_position[0], listblockeravailableup, listblockeravailabledown)
                    true_indices = [i for i, val in enumerate(leftorrightavailable) if val]
                    if 0 in true_indices:
                        index = 0
                    elif 1 in true_indices:
                        index = 1
                    elif 2 in true_indices:
                        index = 2
                    elif 3 in true_indices:
                        index = 3
                    elif 4 in true_indices:
                        index = 4
                    elif 5 in true_indices:
                        index = 5
                    else:
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
                    elif index == 2:
                        pos1 = opponent_position[1] - 1
                        pos2 = pos1
                        blockerlist = opponent_position[0] 
                        blockerlist2 = opponent_position[0] + 2
                        return play_blocker_vertical(blockerlist, blockerlist2, pos1, pos2)
                    elif index == 3:
                        pos1 = opponent_position[1] + 1
                        pos2 = pos1
                        blockerlist = opponent_position[0] 
                        blockerlist2 = opponent_position[0] + 2
                        return play_blocker_vertical(blockerlist, blockerlist2, pos1, pos2)
                    elif index == 4:
                        pos1 = opponent_position[1] - 1
                        pos2 = pos1
                        blockerlist = opponent_position[0]
                        blockerlist2 = opponent_position[0] + 2 
                        return play_blocker_vertical(blockerlist, blockerlist2, pos1, pos2)
                    elif index == 5:
                        pos1 = opponent_position[1] + 1
                        pos2 = pos1
                        blockerlist = opponent_position[0]
                        blockerlist2 = opponent_position[0] + 2 
                        return play_blocker_vertical(blockerlist, blockerlist2, pos1, pos2)
            else:
                play = 'move'
                print('Peut pas mettre de Blocker')

    if play == 'move':
        print('On a move')
        opponent_player = get_opponent_player(player) 
        move_available = callfunction(board, position, opponent_player) # [True, True, False, True]
        listmoveavailable = get_list_position_true_index(move_available)
        if player == 0:
            listpathavailable = board[position[0] + 1]
            if 3 in listmoveavailable:
                return down_move(position)
            elif 7 in listmoveavailable:
                return down_jump_move(position)
            elif 4 in listmoveavailable:
                return right_jump_move(position)
            elif 5 in listmoveavailable:
                return left_jump_move(position)
            elif 1 in listmoveavailable and 0 in listmoveavailable:
                fastestmove = verifyblocker(listpathavailable, position[1])
                if fastestmove == "right":
                    return right_move(position)
                else:
                    return left_move(position)
            elif 1 in listmoveavailable:
                return left_move(position)
            elif 0 in listmoveavailable:
                return right_move(position)
            elif 2 in listmoveavailable:
                return up_move(position)
            elif 6 in listmoveavailable:
                return up_jump_move(position)
        else:
            listpathavailable = board[position[0] - 1]
            if 2 in listmoveavailable:
                return up_move(position)
            elif 6 in listmoveavailable:
                return up_jump_move(position)
            elif 4 in listmoveavailable:
                return right_jump_move(position)
            elif 5 in listmoveavailable:
                return left_jump_move(position)
            elif 1 in listmoveavailable and 0 in listmoveavailable:
                fastestmove = verifyblocker(listpathavailable, position[1])
                if fastestmove == "right":
                    return right_move(position)
                else:
                    return left_move(position)
            elif 1 in listmoveavailable:
                return left_move(position)
            elif 0 in listmoveavailable:
                return right_move(position)
            elif 3 in listmoveavailable:
                return down_move(position)
            elif 7 in listmoveavailable:
                return down_jump_move(position)

# Les 3 fonctions suivantes permettent de déterminer le chemin le plus rapide pour avancer.       
def verifyblocker(listpathavailable, pos_joueur):
    path_indices = get_index_path_available(listpathavailable)
    closest_index = find_closest_index(path_indices, pos_joueur)
    if closest_index > pos_joueur:
        return "right"
    else:
        return "left"

def get_index_path_available(listpathavailable):
    return [i for i, val in enumerate(listpathavailable) if val == 3]

def find_closest_index(indices, target):
    closest_index = None
    min_distance = float('inf')  # Initialiser la distance minimale à l'infini
    
    for index in indices:
        distance = abs(index - target)  # Calculer la distance absolue entre l'indice et la position du joueur
        if distance < min_distance:  # Mettre à jour l'indice le plus proche si la distance actuelle est plus petite
            min_distance = distance
            closest_index = index
    
    return closest_index

def listposblockeravailable(listblockeravailable, board, posblocker, posblocker2, listblockeravailableup, listblockeravailabledown):
    result = []
    result.append(blocker_left(listblockeravailableup ,listblockeravailabledown, listblockeravailable, posblocker))
    result.append(blocker_right(listblockeravailableup ,listblockeravailabledown, listblockeravailable, posblocker))
    result.append(blocker_vert_left_up(board, posblocker, posblocker2))
    result.append(blocker_vert_right_up(board, posblocker, posblocker2))
    result.append(blocker_vert_left_down(board, posblocker, posblocker2))
    result.append(blocker_vert_right_down(board, posblocker, posblocker2))
    return result

def blocker_left(listblockeravailableup ,listblockeravailabledown, listblockeravailable, posblocker):
    if posblocker < 2 or posblocker > 14:
        return False
    else:
        if listblockeravailable[posblocker - 2] == 3:
            if listblockeravailabledown[posblocker - 1] == 3 or listblockeravailableup[posblocker - 1] == 3:
                return True 
            else:
                return False
        else:
            return False


def blocker_right(listblockeravailableup ,listblockeravailabledown, listblockeravailable, posblocker):
    if posblocker < 2 or posblocker > 14:
        return False
    else:
        if listblockeravailable[posblocker + 2] == 3:
            if listblockeravailabledown[posblocker + 1] == 3 or listblockeravailableup[posblocker + 1] == 3:
                return True 
            else:
                return False
        else:
            return False
    
def blocker_vert_right_up(board, posblocker, posblocker2):  
    #posblocker = opponent_position[1]
    #posblocker2 = opponent_position[0]
    if posblocker == 16:
        return False
    elif posblocker2 < 2:
        return False 
    else:
        listblockerup = board[posblocker2 - 2]
        listblockerdown = board[posblocker2]
        list_verif_hor = board[posblocker2 - 1]
        if listblockerdown[posblocker + 1] == 3 and listblockerup[posblocker + 1] == 3:
            if list_verif_hor[posblocker] == 3 or list_verif_hor[posblocker + 2] == 3:
                return True
            else:
                return False
        else: 
            return False
    
def blocker_vert_left_up(board, posblocker, posblocker2):  
    #posblocker = opponent_position[1]
    #posblocker2 = opponent_position[0]
    if posblocker == 0:
        return False
    elif posblocker2 < 2:
        return False
    else:
        listblockerup = board[posblocker2 - 2]
        listblockerdown = board[posblocker2]
        list_verif_hor = board[posblocker2 - 1]
        if listblockerdown[posblocker - 1] == 3 and listblockerup[posblocker - 1] == 3:
            if list_verif_hor[posblocker] == 3 or list_verif_hor[posblocker - 2] == 3:
                return True
            else:
                return False
        else: 
            return False
        
def blocker_vert_right_down(board, posblocker, posblocker2):  
    #posblocker = opponent_position[1]
    #posblocker2 = opponent_position[0]
    if posblocker == 0:
        return False
    elif posblocker2 > 14:
        return False
    else:
        listblockerdown = board[posblocker2 + 2]
        listblockerup = board[posblocker2]
        list_verif_hor = board[posblocker2 + 1]
        if listblockerdown[posblocker + 1] == 3 and listblockerup[posblocker + 1] == 3:
            if list_verif_hor[posblocker] == 3 or list_verif_hor[posblocker + 2] == 3:
                return True
            else:
                return False
        else: 
            return False
        
def blocker_vert_left_down(board, posblocker, posblocker2):  
    #posblocker = opponent_position[1]
    #posblocker2 = opponent_position[0]
    if posblocker == 0:
        return False
    elif posblocker2 > 14:
        return False
    else:
        listblockerdown = board[posblocker2 + 2]
        listblockerup = board[posblocker2]
        list_verif_hor = board[posblocker2 + 1]
        if listblockerdown[posblocker - 1] == 3 and listblockerup[posblocker - 1] == 3:
            if list_verif_hor[posblocker] == 3 or list_verif_hor[posblocker - 2] == 3:
                return True
            else:
                return False
        else: 
            return False
    

def play_blocker(blockerlist, pos1, pos2):
    return {
    "type": "blocker", 
    "position": [[blockerlist,pos1], [blockerlist,pos2]] 
}

def play_blocker_vertical(blockerlist, blockerlist2, pos1, pos2):
    return {
    "type": "blocker", 
    "position": [[blockerlist,pos1], [blockerlist2,pos2]]
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
        #print(listcase)
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
        #print(f'listcase{listcase}')
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
        #print(f'listcase{listcase}')
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
        if listcase[position[1] + 2] == opponent_player and listcase[position[1] + 1] == 3 and listcase[position[1] + 3] == 3: 
            return True
        else:
            return False
        
def left_jump_available(board, position, opponent_player):
    if position[1] <= 2 :
        return False
    else:
        listcase = board[position[0]]
        if listcase[position[1] - 2] == opponent_player and listcase[position[1] - 1] == 3 and listcase[position[1] - 3] == 3:
            return True
        else:
            return False
        
def up_jump_available(board, position, opponent_player):
    if position[0] <= 2 :
        return False
    else:
        listcase = board[position[0] - 2]
        listcase1 = board[position[0] - 1]
        listcase3 = board[position[0] - 3]
        if listcase[position[1]] == opponent_player and listcase1[position[1]] == 3 and listcase3[position[1]] == 3:
            return True
        else:
            return False
        
def down_jump_available(board, position, opponent_player):
    if position[0] >= 14 :
        return False
    else:
        listcase = board[position[0] + 2]
        listcase1 = board[position[0] + 1]
        listcase3 = board[position[0] + 3]
        if listcase[position[1]] == opponent_player and listcase1[position[1]] == 3 and listcase3[position[1]] == 3:
            return True
        else:
            return False
    
    
    
def callfunction(board, position, opponent_player):

    # with open("partie5.txt", "a") as fichier:
# Convertir la variable en chaîne de caractères et l'écrire dans le fichier
        # fichier.write("Callfunction"+"\n")

    listefunction = []
    listefunction.append(right_available(board, position))
    listefunction.append(left_available(board, position))
    listefunction.append(up_available(board, position))
    listefunction.append(down_available(board, position))
    listefunction.append(right_jump_available(board,position,opponent_player))
    listefunction.append(left_jump_available(board,position,opponent_player))
    listefunction.append(up_jump_available(board,position,opponent_player))
    listefunction.append(down_jump_available(board,position,opponent_player))

# # Ouvrir le fichier en mode écriture
#     with open("partie5.txt", "a") as fichier:
# # Convertir la variable en chaîne de caractères et l'écrire dans le fichier
#         fichier.write(str(listefunction)+"\n")

    return listefunction

def get_position(server_json, player): # Indique position de où je suis 
    board = server_json["state"]["board"]

# [0,8] pour 0 et [16,8] pour 1
    for indicelist, elem in enumerate(board):  # Parcourt les 17 listes 
        #print(f'player{player}')
        if player in elem:  # Vérifie si zéro est présent dans la liste
            pos_in_list = elem.index(player)  # Obtient la position de zéro dans la liste
            #print(f'positionduplayer{[indicelist, pos_in_list] }')
            return [indicelist, pos_in_list]  # Renvoie le numéro de la liste et la position de zéro dans cette liste

def handle_ping_pong():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 8850))
        s.listen()
        while True:
            player, address = s.accept()
            with player:
                server_request = player.recv(204800).decode()
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

                    # # Ouvrir le fichier en mode écriture
                    # with open("partie5.txt", "a") as fichier:
                    # # Convertir la variable en chaîne de caractères et l'écrire dans le fichier
                    #     fichier.write(str(player_move)+"\n")
                        



                    # print(f'Réponse : {move_played} , {player_move}')
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
    "name": "Ayoub",
    "matricules": ["21061", "56625"]
}

# Définir l'adresse IP et le port du serveur local
server_address = ('localhost', 3000)

send_json_data(json_data, server_address)
handle_ping_pong()

# Définir limite de placement des blockers (doit laisser 1 chemin au min.)
# Définir le contour du plateau de jeu pour blocker verticaux. -> Made
# Demander comment éviter le cas avec 5 -> Made
# Demander pourquoi il met que des blockers verticaux -> Made
# Demander comment mettre le MinMax ou BFS -> Made
# Régler le problème avec le None quand on joue à gauche du plateau -> Problème vient des bloqueurs
# Faire le README
# Faire les tests

import Player
import json
import random

def test_get_position():
    player = random.choice([0,1])
    server_json = {
    "request": "play",
    "lives": 3,
    "errors": [],
    "state": {
        "players": ["Ayoub", "IbraGOAT"],
        "current": 0,
        "blockers": [10, 10],
        "board": 
        
            [[2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]]}
}
    if player == 0:
        assert Player.get_position(server_json, player) == [0,8]
    else:
        assert Player.get_position(server_json, player) == [16,8]

def test_moveorblocker():
    move_played = 0
    move_played += 1
    blockeravailable = 10
    blockeravailable -= 1
    if move_played % 2 == 0:
        assert Player.moveorblocker(blockeravailable) == 'blocker'
    elif blockeravailable == 0:
        assert Player.moveorblocker(blockeravailable) == 'move'
    else:
        assert Player.moveorblocker(blockeravailable) == 'move'

def test_get_opponent_player():
    player = [0,1]
    if player == 0:
        assert Player.get_opponent_player(player) == 1
    else:
        assert Player.get_opponent_player(player) == 0

def test_play_blocker():
    blockerlist = 1
    pos1 = 8
    pos2 = 10
    result = Player.play_blocker(blockerlist, pos1, pos2)
    expected_result = {
        "type": "blocker", 
        "position": [[blockerlist, pos1], [blockerlist, pos2]]
    }
    assert result == expected_result, "La fonction devrait renvoyer un JSON avec le type 'blocker' et les positions spécifiées"

def test_play_blocker_vertical():
    blockerlist = 0
    blockerlist2 = 2
    pos1 = 7
    pos2 = 7
    result = Player.play_blocker_vertical(blockerlist, blockerlist2, pos1, pos2)
    expected_result = {
        "type": "blocker", 
        "position": [[blockerlist, pos1], [blockerlist2, pos2]]
    }
    assert result == expected_result, "La fonction devrait renvoyer un JSON avec le type 'blocker' et les positions spécifiées"

def test_listposblockeravailable():
    board = [[2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]]
    posblocker = 8
    posblocker2 = 0
    listblockeravailable = board[posblocker2 + 1]
    listblockeravailableup = board[posblocker2 + 2]
    listblockeravailabledown = board[posblocker2]
    result = Player.listposblockeravailable(listblockeravailable, board, posblocker, posblocker2, listblockeravailableup, listblockeravailabledown)
    expected_result = [True, True, False, False, True, True]
    assert result == expected_result
        
def test_callfunction():
    board = [[2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]]
    position = [0, 8]
    opponent_player = 1
    result = Player.callfunction(board, position, opponent_player)
    expected_result = [True, True, False, True, False, False, False, False]
    assert result == expected_result

def test_get_list_position_true_index():
    move_available = [True, True, False, False, False, False, False, True]
    result = Player.get_list_position_true_index(move_available)
    expected_result = [0,1,7]
    assert result == expected_result

def test_down_move():
    position = [0, 8]
    result = Player.down_move(position)
    expected_result = {"type": "pawn", "position": [[2, 8]]}
    assert result == expected_result

def test_up_move():
    position = [2, 8]
    result = Player.up_move(position)
    expected_result = {"type": "pawn", "position": [[0, 8]]}
    assert result == expected_result
def test_right_move():
    position = [0, 8]
    result = Player.right_move(position)
    expected_result = {"type": "pawn", "position": [[0, 10]]}
    assert result == expected_result

def test_left_move():
    position = [0, 8]
    result = Player.left_move(position)
    expected_result = {"type": "pawn", "position": [[0, 6]]}
    assert result == expected_result

def test_down_jump_move():
    position = [0, 8]
    result = Player.down_jump_move(position)
    expected_result = {"type": "pawn", "position": [[4, 8]]}
    assert result == expected_result

def test_up_jump_move():
    position = [4, 8]
    result = Player.up_jump_move(position)
    expected_result = {"type": "pawn", "position": [[0, 8]]}
    assert result == expected_result

def test_right_jump_move():
    position = [0, 8]
    result = Player.right_jump_move(position)
    expected_result = {"type": "pawn", "position": [[0, 12]]}
    assert result == expected_result

def test_left_jump_move():
    position = [0, 8]
    result = Player.left_jump_move(position)
    expected_result = {"type": "pawn", "position": [[0, 4]]}
    assert result == expected_result

def test_verifyblocker():
    listpathavailable = [4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0]
    pos_joueur = 6
    result = Player.verifyblocker(listpathavailable, pos_joueur)
    expected_result = "left"
    assert result == expected_result

def test_get_index_path_available():
    listpathavailable = [4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0]
    result = Player.get_index_path_available(listpathavailable)
    expected_result = [8,10]
    assert result == expected_result

def test_find_closest_index():
    indices = [2, 7, 15]
    target = 5
    result = Player.find_closest_index(indices, target)
    expected_result = 7
    assert result == expected_result

def test_blocker_left():
    # Cas où posblocker est inférieur à 2
    listblockeravailableup = [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0]
    listblockeravailabledown = [1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    listblockeravailable = [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0]
    posblocker = 0
    result = Player.blocker_left(listblockeravailableup, listblockeravailabledown, listblockeravailable, posblocker)
    assert not result, "Le résultat devrait être False car posblocker est inférieur à 2"

    # Cas où posblocker est supérieur à 14
    posblocker = 16
    result = Player.blocker_left(listblockeravailableup, listblockeravailabledown, listblockeravailable, posblocker)
    assert not result, "Le résultat devrait être False car posblocker est supérieur à 14"

    # Cas où la case précédente à posblocker contient un blocker et les cases en haut et en bas contiennent des blockers
    listblockeravailableup = [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0]
    listblockeravailabledown = [2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    listblockeravailable = [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0]
    posblocker = 4
    result = Player.blocker_left(listblockeravailableup, listblockeravailabledown, listblockeravailable, posblocker)
    assert result, "Le résultat devrait être True car la case précédente contient un blocker et les cases en haut et en bas contiennent des blockers"

    # Cas où la case précédente à posblocker ne contient pas de blocker
    listblockeravailableup = [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0]
    listblockeravailabledown = [2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    listblockeravailable = [4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0]
    posblocker = 4
    result = Player.blocker_left(listblockeravailableup, listblockeravailabledown, listblockeravailable, posblocker)
    assert not result, "Le résultat devrait être False car la case précédente ne contient pas de blocker"

def test_blocker_right():

    # Cas où posblocker est inférieur à 2
    listblockeravailableup = [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0]
    listblockeravailabledown = [1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    listblockeravailable = [3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0]
    posblocker = 0
    result = Player.blocker_right(listblockeravailableup, listblockeravailabledown, listblockeravailable, posblocker)
    assert not result, "Le résultat devrait être False car posblocker est inférieur à 2"

    # Cas où posblocker est supérieur à 14
    posblocker = 16
    result = Player.blocker_right(listblockeravailableup, listblockeravailabledown, listblockeravailable, posblocker)
    assert not result, "Le résultat devrait être False car posblocker est supérieur à 14"

    # Cas où la case suivante à posblocker contient un blocker et les cases en haut et en bas contiennent des blockers
    listblockeravailableup = [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0]
    listblockeravailabledown = [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0]
    listblockeravailable = [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0]
    posblocker = 12
    result = Player.blocker_right(listblockeravailableup, listblockeravailabledown, listblockeravailable, posblocker)
    assert result, "Le résultat devrait être True car la case suivante contient un blocker et les cases en haut et en bas contiennent des blockers"

    # Cas où la case suivante à posblocker ne contient pas de blocker
    listblockeravailableup = [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0]
    listblockeravailabledown = [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0]
    listblockeravailable = [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0, 5.0, 4.0]
    posblocker = 12
    result = Player.blocker_right(listblockeravailableup, listblockeravailabledown, listblockeravailable, posblocker)
    assert not result, "Le résultat devrait être False car la case suivante ne contient pas de blocker"

def test_blocker_vert_right_up():
    # Plateau de jeu
    board = [
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    ]

    # Cas où posblocker est en position 16 (en bas à droite)
    posblocker = 16
    posblocker2 = 0
    result = Player.blocker_vert_right_up(board, posblocker, posblocker2)
    assert not result, "Le résultat devrait être False car posblocker est en position 16"

    # Cas où posblocker2 est inférieur à 2
    posblocker = 0
    posblocker2 = 0
    result = Player.blocker_vert_right_up(board, posblocker, posblocker2)
    assert not result, "Le résultat devrait être False car posblocker2 est inférieur à 2"

    # Cas où les conditions pour placer un blocker sont remplies
    posblocker = 0
    posblocker2 = 16
    result = Player.blocker_vert_right_up(board, posblocker, posblocker2)
    assert not result, "Le résultat devrait être True car les conditions pour placer un blocker sont remplies"

    # Cas où les conditions pour placer un blocker ne sont pas remplies
    posblocker = 4
    posblocker2 = 12
    result = Player.blocker_vert_right_up(board, posblocker, posblocker2)
    assert result, "Le résultat devrait être False car les conditions pour placer un blocker ne sont pas remplies"

def test_blocker_vert_left_up():
    # Plateau de jeu
    board = [
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    ]

    # Cas où posblocker est en position 16 (en bas à droite)
    posblocker = 16
    posblocker2 = 0
    result = Player.blocker_vert_left_up(board, posblocker, posblocker2)
    assert not result, "Le résultat devrait être False car posblocker est en position 16"

    # Cas où posblocker2 est inférieur à 2
    posblocker = 0
    posblocker2 = 0
    result = Player.blocker_vert_left_up(board, posblocker, posblocker2)
    assert not result, "Le résultat devrait être False car posblocker2 est inférieur à 2"

    # Cas où les conditions pour placer un blocker sont remplies
    posblocker = 2
    posblocker2 = 16
    result = Player.blocker_vert_left_up(board, posblocker, posblocker2)
    assert not result, "Le résultat devrait être True car les conditions pour placer un blocker sont remplies"

    # Cas où les conditions pour placer un blocker ne sont pas remplies
    posblocker = 4
    posblocker2 = 12
    result = Player.blocker_vert_left_up(board, posblocker, posblocker2)
    assert result, "Le résultat devrait être False car les conditions pour placer un blocker ne sont pas remplies"


def test_blocker_vert_right_down():
    # Plateau de jeu
    board = [
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    ]

    # Cas où posblocker est en position 0 (en haut à gauche)
    posblocker = 8 #opponent_position[1] -> position dans liste
    posblocker2 = 0#opponent_position[0] -> liste adversaire 
    result = Player.blocker_vert_right_down(board, posblocker, posblocker2)
    assert result, "Le résultat devrait être False car posblocker est en position 0" 

    # # Cas où posblocker2 est supérieur à 14
    posblocker = 16
    posblocker2 = 10
    result = Player.blocker_vert_right_down(board, posblocker, posblocker2)
    assert not result, "Le résultat devrait être False car posblocker2 est supérieur à 14"

    # Cas où les conditions pour placer un blocker sont remplies
    posblocker = 2
    posblocker2 = 10
    result = Player.blocker_vert_right_down(board, posblocker, posblocker2)
    assert not result, "Le résultat devrait être True car les conditions pour placer un blocker sont remplies"

    # Cas où les conditions pour placer un blocker ne sont pas remplies
    posblocker = 4
    posblocker2 = 8
    result = Player.blocker_vert_right_down(board, posblocker, posblocker2)
    assert result, "Le résultat devrait être False car les conditions pour placer un blocker ne sont pas remplies"

def test_blocker_left_down():
    # Plateau de jeu
    board = [
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    ]

    # Cas où posblocker est en position 0 (en haut à gauche)
    posblocker = 0
    posblocker2 = 0
    result = Player.blocker_vert_left_down(board, posblocker, posblocker2)
    assert not result, "Le résultat devrait être False car posblocker est en position 0"

    # # Cas où posblocker2 est supérieur à 14
    posblocker = 10
    posblocker2 = 16
    result = Player.blocker_vert_left_down(board, posblocker, posblocker2)
    assert not result, "Le résultat devrait être False car posblocker2 est supérieur à 14"

    # Cas où les conditions pour placer un blocker sont remplies
    posblocker = 4
    posblocker2 = 10
    result = Player.blocker_vert_left_down(board, posblocker, posblocker2)
    assert not result, "Le résultat devrait être True car les conditions pour placer un blocker sont remplies"

    # Cas où les conditions pour placer un blocker ne sont pas remplies
    posblocker = 6
    posblocker2 = 8
    result = Player.blocker_vert_left_down(board, posblocker, posblocker2)
    assert result, "Le résultat devrait être False car les conditions pour placer un blocker ne sont pas remplies"

    # Cas ou il est au dessus de 16
    posblocker = 16
    posblocker2 = 0
    assert result

def test_right_available():
    # Plateau de jeu
    board = [
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 4.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 4.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    ]

    # Cas où le déplacement à droite est possible
    position = [0, 8]  # Position dans le coin supérieur gauche
    result =Player.right_available(board, position)
    assert result, "Le déplacement à droite devrait être possible"

    # Cas où le déplacement à droite n'est pas possible
    position = [0, 16]  # Position dans le coin supérieur droit
    result = Player.right_available(board, position)
    assert not result, "Le déplacement à droite ne devrait pas être possible"

    # Cas où le déplacement à droite n'est pas possible car un blocage
    position = [8, 2]  # Position où il y a un blocage
    result = Player.right_available(board, position)
    assert not result, "Le déplacement à droite ne devrait pas être possible car il y a un blocage"

def test_left_available():
    # Plateau de jeu
    board = [
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 4.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 4.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    ]

    # Cas où le déplacement à droite est possible
    position = [0, 8]  # Position dans le coin supérieur gauche
    result =Player.left_available(board, position)
    assert result, "Le déplacement à droite devrait être possible"

    # Cas où le déplacement à droite n'est pas possible
    position = [0, 0]  # Position dans le coin supérieur droit
    result = Player.left_available(board, position)
    assert not result, "Le déplacement à droite ne devrait pas être possible"

    # Cas où le déplacement à droite n'est pas possible car un blocage
    position = [4, 2]  # Position où il y a un blocage
    result = Player.left_available(board, position)
    assert not result, "Le déplacement à droite ne devrait pas être possible car il y a un blocage"

def test_up_available():
    # Plateau de jeu
    board = [
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    ]

    # Cas où le déplacement vers le haut est possible
    position = [8, 0]  # Position dans le coin inférieur gauche
    result = Player.up_available(board, position)
    assert result, "Le déplacement vers le haut devrait être possible"

    # Cas où le déplacement vers le haut n'est pas possible
    position = [0, 8]  # Position dans le coin supérieur gauche
    result = Player.up_available(board, position)
    assert not result, "Le déplacement vers le haut ne devrait pas être possible"

    # Cas où le déplacement vers le haut n'est pas possible car un blocage
    position = [6, 2]  # Position où il y a un blocage
    result = Player.up_available(board, position)
    assert not result, "Le déplacement vers le haut ne devrait pas être possible car il y a un blocage"

def test_down_available():
    # Plateau de jeu
    board = [
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    ]

    # Cas où le déplacement vers le haut est possible
    position = [0, 8]  # Position dans le coin inférieur gauche
    result = Player.down_available(board, position)
    assert result, "Le déplacement vers le haut devrait être possible"

    # Cas où le déplacement vers le haut n'est pas possible
    position = [16, 6]  # Position dans le coin supérieur gauche
    result = Player.down_available(board, position)
    assert not result, "Le déplacement vers le haut ne devrait pas être possible"

    # Cas où le déplacement vers le haut n'est pas possible car un blocage
    position = [12, 4]  # Position où il y a un blocage
    result = Player.down_available(board, position)
    assert not result, "Le déplacement vers le haut ne devrait pas être possible car il y a un blocage"

def test_right_jump_available():
    # Plateau de jeu
    board = [
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 4.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 4.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    ]

    # Cas où le saut à droite est possible
    position = [0, 8]  # Position où le saut à droite est possible
    opponent_player = 1  # Adversaire du joueur
    result = Player.right_jump_available(board, position, opponent_player)
    assert result, "Le saut à droite devrait être possible"

    # Cas où le saut à droite n'est pas possible
    position = [4, 8]  # Position où le saut à droite n'est pas possible
    result = Player.right_jump_available(board, position, opponent_player)
    assert not result, "Le saut à droite ne devrait pas être possible"

    # Cas où le saut à droite n'est pas possible car un blocage
    position = [8, 2]  # Position où le saut à droite n'est pas possible car un blocage
    result = Player.right_jump_available(board, position, opponent_player)
    assert not result, "Le saut à droite ne devrait pas être possible car un blocage"

    # Cas où il est plus grand que 15
    position = [0,15]
    result = Player.right_jump_available(board, position, opponent_player)
    assert not result 

def test_left_jump_available():
    # Plateau de jeu
    board = [
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 4.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 4.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    ]

    # Cas où le saut à droite est possible
    position = [0, 8]  # Position où le saut à droite est possible
    opponent_player = 1  # Adversaire du joueur
    result = Player.left_jump_available(board, position, opponent_player)
    assert result, "Le saut à droite devrait être possible"

    # Cas où le saut à droite n'est pas possible
    position = [6, 2]  # Position où le saut à droite n'est pas possible
    result = Player.left_jump_available(board, position, opponent_player)
    assert not result, "Le saut à droite ne devrait pas être possible"

    # Cas où le saut à droite n'est pas possible car un blocage
    position = [8, 4]  # Position où le saut à droite n'est pas possible car un blocage
    result = Player.left_jump_available(board, position, opponent_player)
    assert not result, "Le saut à droite ne devrait pas être possible car un blocage"

def test_up_jump_available():
    # Plateau de jeu
    board = [
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    ]

    # Cas où le saut vers le haut est possible
    position = [6, 10]  # Position où le saut vers le haut est possible
    opponent_player = 1  # Adversaire du joueur
    result = Player.up_jump_available(board, position, opponent_player)
    assert result, "Le saut vers le haut devrait être possible"

    # Cas où le saut vers le haut n'est pas possible
    position = [2, 2]  # Position où le saut vers le haut n'est pas possible
    result = Player.up_jump_available(board, position, opponent_player)
    assert not result, "Le saut vers le haut ne devrait pas être possible"

    # Cas où le saut vers le haut n'est pas possible car un blocage
    position = [4, 8]  # Position où le saut vers le haut n'est pas possible car un blocage
    result = Player.up_jump_available(board, position, opponent_player)
    assert not result, "Le saut vers le haut ne devrait pas être possible car un blocage"

def test_up_down_available():
    # Plateau de jeu
    board = [
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [4.0, 5.0, 4.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
        [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
        [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]
    ]

    # Cas où le saut vers le haut est possible
    position = [0, 8]  # Position où le saut vers le haut est possible
    opponent_player = 1  # Adversaire du joueur
    result = Player.down_jump_available(board, position, opponent_player)
    assert result, "Le saut vers le bas devrait être possible"

    # Cas où le saut vers le haut n'est pas possible
    position = [16, 8]  # Position où le saut vers le haut n'est pas possible
    result = Player.down_jump_available(board, position, opponent_player)
    assert not result, "Le saut vers le bas ne devrait pas être possible"

    # Cas où le saut vers le haut n'est pas possible car un blocage
    position = [10, 2]  # Position où le saut vers le haut n'est pas possible car un blocage
    result = Player.down_jump_available(board, position, opponent_player)
    assert not result, "Le saut vers le bas ne devrait pas être possible car un blocage"

def test_player_mover():
    # Objet JSON de test
    test_server_json = {
    "request": "play",
    "lives": 3,
    "errors": [],
    "state": {
        "players": ["Ayoub", "BOT"],
        "current": 0,
        "blockers": [10, 10],
        "board": 
        
            [[2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 0.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0],
             [3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0, 5.0, 3.0],
             [2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0, 3.0, 2.0]]}
}

    # Exécute player_mover avec les données de test
    result = Player.player_mover(test_server_json)
    assert result == {'position': [[15, 6], [15, 8]], 'type': 'blocker'}

    
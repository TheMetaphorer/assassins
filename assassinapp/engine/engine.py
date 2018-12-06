import exceptions

from random import randint

class GameManager:

    def __init__(self, uuid, created_timestamp, expires, key, **players):
        self.uuid = uuid
        self.created_timestamp = created_timestamp
        self.expires = expires
        self.key = key
        self.players = players
        self.matched_players = []
    
    def add_player(self, name, auth, uuid):
        if name != self.key:
            raise exceptions.AuthenticationException('Invalid key.')
        else:
            players['name'] = uuid

    def assign_players(self):
        temp_player_dic = self.players
        while len(temp_player_dic.keys()) > 1:
            player_1_key = temp_player_dic.keys()[randint(0, len(temp_player_dic.keys()-1))]
            temp_player_dic.pop(player_1_key)
            player_2_key = temp_player_dic.keys()[randint(0, len(temp_player_dic.keys()-1))]
            temp_player_dic.pop(player_2_key)
        matched_players.append((player_1_key, player_2_key))
            
    
    def kill_player(self, player):
        self.players.pop(player)


import random
from random import randint


class Timeout(Exception):
    pass


def custom_score0(game, player):

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves)

def custom_score1(game, player):

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = game.get_legal_moves(player)
    opp_moves = game.get_legal_moves(game.get_opponent(player))
    return float(len(set(own_moves) & set(opp_moves)))

def custom_score2(game, player):

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    return float(own_moves)

def custom_score3(game, player):

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    
    for move in game.get_legal_moves(player):
        game_forecast = game.forecast_move(move)
        own_moves += len(game_forecast.get_legal_moves(player))
        opp_moves += len(game_forecast.get_legal_moves(game_forecast.get_opponent(player)))
    
    return float(own_moves - opp_moves)

def custom_score(game, player):

    if len(game.get_blank_spaces()) > 20:
        return custom_score0(game, player)
    else:
        return custom_score3(game, player)

class CustomPlayer:

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=20.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

    def get_move(self, game, legal_moves, time_left):

        self.time_left = time_left

        if not legal_moves:
            return (-1, -1)

        if (3, 3) in legal_moves:
            return 3, 3

        best_move = legal_moves[randint(0, len(legal_moves) - 1)]

        try:
            depth = 1
            while (self.iterative or depth <= self.search_depth):
                
                best_move = (self.minimax(game, depth)[1] if self.method == 'minimax' 
                else self.alphabeta(game, depth)[1])
                
                depth += 1
                #print("Best move {}".format(best_move))

                if self.time_left() < self.TIMER_THRESHOLD:
                    raise Timeout()

        except Timeout:
            #print("Depth {}: Timeout of iterative deepening.".format(depth))
            return best_move

        return best_move


# Minimax algorithm - CustomPlayer.minimax()
    def minimax(self, game, depth, maximizing_player = True):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        return (self.maxvalue(game, depth) if maximizing_player else self.minvalue(game, depth))


# Alpha-beta pruning for minimax - CustomPlayer.alphabeta()
    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player = True):
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        return (self.maxvalue(game, depth, alpha, beta) if maximizing_player 
            else self.minvalue(game, depth, alpha, beta))


# Max value
    def maxvalue(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        if not game.get_legal_moves() or depth == 0:
            return (self.score(game, self), (-1, -1))

        moves = {}
        for move in game.get_legal_moves():
            game_forecast = game.forecast_move(move)
            if depth == 1:
                moves[move] = self.score(game_forecast, game.active_player)
            else:
                moves[move] = self.minvalue(game_forecast, depth - 1, alpha, beta)[0]
                alpha = moves[min(moves, key = moves.get)]

            if self.time_left() < self.TIMER_THRESHOLD:
                raise Timeout()

            if self.method == "alphabeta" and moves[move] >= beta:
                break

        best_move = max(moves, key = moves.get)
        return (moves[best_move], best_move)

# Min value
    def minvalue(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        if not game.get_legal_moves() or depth == 0:
            return (self.score(game, self), (-1, -1))

        moves = {}
        for move in game.get_legal_moves():
            game_forecast = game.forecast_move(move)
            if depth == 1:
                moves[move] = self.score(game_forecast, game.inactive_player)
            else:
                moves[move] = self.maxvalue(game_forecast, depth - 1, alpha, beta)[0]
                beta = moves[max(moves, key = moves.get)]

            if self.time_left() < self.TIMER_THRESHOLD:
                raise Timeout()

            if self.method == "alphabeta" and moves[move] <= alpha:
                break

        best_move = min(moves, key = moves.get)
        return (moves[best_move], best_move)

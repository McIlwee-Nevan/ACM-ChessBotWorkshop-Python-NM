import chess as ch # AKA python-chess
import random

class Bot:
    # Properties:
        # - class: Board 
        #   - (class object imported from python-chess; not defined by us)
        #   - legal_moves: property of Board
        # - enum: Color
        #   - takes python-chess defined enums ch.WHITE / ch.BLACK
        # - int: max_depth
        #   - higher depth = bigger brain, slower computing time

    # Methods:
        # public:
        #   - getBestMove() (called by Main.py)
        #       - calls recursive search
        #       - returns Move with best evaluation
        # private: 
        #   - search()
        #   - evaluate()

    def __init__(self, Board, max_depth, Color):
        self.Board = Board
        self.Color = Color
        self.max_depth = max_depth

        self.piece_values = {
             ch.PAWN : 1,
             ch.ROOK : 5,
             ch.BISHOP : 3,
             ch.KNIGHT : 3,
             ch.QUEEN : 9,
             ch.KING : 100,
        }
    
    def getBestMove(self):
        best_move, best_value = self.search(1)
        print(best_move, best_value)
        return best_move

    # Move score based on current board state
    def evaluate(self):
        score = 0

        for i in range(64):
            score += self.evalSquareValue(ch.SQUARES[i])

        return score

    def evalSquareValue(self, square):
        piece_type = self.Board.piece_type_at(square)
        if piece_type:
             piece_value = self.piece_values[piece_type]
             return piece_value if (self.Board.color_at(square) == self.Color) else -piece_value
        return 0

    # Recursive search function
    def search(self, depth):
        if depth == self.max_depth or self.Board.legal_moves.count() == 0:
            return None, self.evaluate()
        
        is_maximizing = depth % 2 != 0

        if is_maximizing:
            best_value = float("-inf")
            best_move = None

            for move in self.Board.legal_moves:
                self.Board.push(move)

                _, value_candidate = self.search(depth + 1)

                if value_candidate > best_value:
                        best_value = value_candidate
                        best_move = move

                self.Board.pop()
            
            return best_move, best_value
        
        elif not is_maximizing:
            best_value = float("inf")
            best_move = None

            for move in self.Board.legal_moves:
                self.Board.push(move)

                _, value_candidate = self.search(depth + 1)

                if value_candidate < best_value:
                        best_value = value_candidate
                        best_move = move

                self.Board.pop()
            
            return best_move, best_value
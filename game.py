from board import Board
import random
from variable import PLAYER1_ID, PLAYER2_ID

class Game:
    def __init__(self) -> None:
        self.is_selected = False
        self.select = None
        self.turn = None
        self.board = Board()
        self.vaild_moves = []
    
    def change_turn(self):
        if self.turn == None:
            num = random.randint(1,2)
            if num == 1:
                self.turn = PLAYER1_ID
            else:
                self.turn = PLAYER2_ID
        else:
            if self.turn == PLAYER1_ID:
                self.turn = PLAYER2_ID
            else:
                self.turn = PLAYER1_ID
    
    def select_piece(self,row,col):
        if self.is_selected:
            piece = self.select
            self.move(piece,row,col)
        else:
            piece = self.board.get_pieces(row,col)
            if piece == None:
                return None
            else:
                piece.is_selected = True
                self.select = piece
                self.is_selected = True
        
        return True
    
    def move(self,piece,row,col):
        if piece.id == self.turn:
            can = self.check_can_move(piece,row,col)
            if can:
                pass

    def check_vaild_moves(self,row,col):
        moves = {}
        left = col-1
        right = col+1

        piece = self.get_pieces(row,col)
        if piece != None:
            if piece.id == PLAYER1_ID or piece.is_king:
                pass
            
            if piece.id == PLAYER2_ID or piece.is_king:
                pass

    def _tranverse_left(self,start,stop,step,id,left,skipped=[]):
        moves = {}
        last = []

        for r in range(start,stop,step):
            if r < 0:
                break

            piece = self.get_pieces(r,left)
            if piece == None:
                if skipped and not last:
                    break

            left -= 1


    
    def _tranverse_right(self,start,stop,step,id,right,skipped=[]):
        pass


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
    
    def select(self,row,col):
        if self.is_selected:
            piece = self.select
            self.move(piece,row,col)
        else:
            piece = self.board.get_pieces(row,col)
            if piece == None:
                pass
            else:
                self.select = piece
                self.is_selected = True
    
    def move(self,piece,row,col):
        if piece.id == self.turn:
            can = self.check_can_move(piece,row,col)
            if can:
                pass
    
    def check_can_move(self,piece,row,col):
        if piece.id == PLAYER1_ID:
            #check right
            for i in range(8):
                if row-i >= 0 and col+i <= 7:
                    if self.board[row-i][col+i] in [0,1]:
                        self.vaild_moves.append([row,col])
                        return True
                    else:
                        if self.board[row-i][col+i].id == PLAYER2_ID:
                            if row-i+1 >= 0 and col+i <= 7:
                                if self.board[row-i][col+i] not in [0,1]:
                                    self.vaild_moves.append([row,col])
                                    return True


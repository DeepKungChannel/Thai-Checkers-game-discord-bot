from pieces import Pieces
from variable import PLAYER1_ID, PLAYER2_ID

class Board:
    def __init__(self) -> None:
        self.board = [
            [1,0,1,0,1,0,1,0,1],
            [0,1,0,1,0,1,0,1,0],
            [1,0,1,0,1,0,1,0,1],
            [0,1,0,1,0,1,0,1,0],
            [1,0,1,0,1,0,1,0,1],
            [0,1,0,1,0,1,0,1,0],
            [1,0,1,0,1,0,1,0,1],
            [0,1,0,1,0,1,0,1,0]]
        self.defualt_board = [
            [1,0,1,0,1,0,1,0,1],
            [0,1,0,1,0,1,0,1,0],
            [1,0,1,0,1,0,1,0,1],
            [0,1,0,1,0,1,0,1,0],
            [1,0,1,0,1,0,1,0,1],
            [0,1,0,1,0,1,0,1,0],
            [1,0,1,0,1,0,1,0,1],
            [0,1,0,1,0,1,0,1,0]]
        self.add_player_into_a_board()
    
    def add_player_into_a_board(self):
        # Add Yellow into the board | on the top
        for i in range(2): #row 1-2
            for j in range(8):
                item = self.board[i][j]
                if item == 0:
                    self.board[i][j] = Pieces(PLAYER2_ID)
        
        #Add RED into the board | on the bottom
        for i in range(6,8): #row 7-8
            for j in range(8):
                item = self.board[i][j]
                if item == 0:
                    self.board[i][j] = Pieces(PLAYER1_ID)
    
    def draw(self):
        text = ""
        for i in range(8):
            for j in range(8):
                item = self.board[i][j]
                if item == 0:
                    text += "⬜"
                elif item == 1:
                    text += "🟫"
                elif isinstance(item,Pieces):
                    if item.is_selected:
                        text += "🔵"
                    else:
                        text += item.emoji
            text += "\n"
        return text
    
    def get_pieces(self,row,col):
        if self.board[row][col] not in [1,0]:
            return self.board[row][col]
        return None
    
    
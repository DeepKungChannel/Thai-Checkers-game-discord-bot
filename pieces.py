class Pieces:
    def __init__(self,id) -> None:
        self.is_king = False
        self.is_selected = False
        self.id = id
        if id == "RED":
            self.emoji = "🔴"
        elif id == "YELLOW":
            self.emoji = "🟡"
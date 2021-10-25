class Pieces:
    def __init__(self,id) -> None:
        self.is_king = False
        self.id = id
        if id == "RED":
            self.emoji = "🔴"
        elif id == "YELLOW":
            self.emoji = "🟡"
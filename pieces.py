class Pawn():
    def __init__(self, name, x, y, hasMoved = False):
        self.name = name
        self.x = x
        self.y = y
        self.hasMoved = hasMoved
    
    def print(self):
        print(f'Unit name: {self.name}\n Unit X: {self.x}\n Unit Y: {self.y}\n Has it moved?: {self.hasMoved}')

    def move(self):
        self.x = self.x - 1 if (self.x - 1) >= 0 else False
        if self.hasMoved == False:
            self.y = self.y + 2 if (self.y + 2) <= 8 else False
        else:
            self.y = self.y + 1 if (self.y + 1) <= 8 else False
        
        self.hasMoved = True
        return self.x, self.y if self.x and self.y != False else None


pawn = Pawn('nick', 1, 1)
pawn.move()
pawn.print()
pawn.move()
pawn.print()
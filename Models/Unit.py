class Unit:
    def __init__(self, posX, posY, unitType, type):
        self.posX = posX
        self.posY = posY
        self.unitType = unitType
        self.type = type
    def update_coords(self, new_posX, new_posY):
        self.posX = new_posX
        self.posY = new_posY
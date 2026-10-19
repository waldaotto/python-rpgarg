from core.Model import Model

class Backpack(Model):

    def __init__(self):
        super().__init__()
        self.TABLE = "backpack"
        self.COLUMNS = (
            'player_id',
            'slots',
        )






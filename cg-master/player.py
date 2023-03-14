class Player:

    def __init__(self, user, id):
        self.user = user
        self.id = id
        self.maxlife = 30
        self.maxmana = 10
        self.life = 30
        self.mana = 0
        self.hero = None
        self.deck = []
        self.hand = []
        self.board = []

    def __str__(self):
        return self.user

    def __hash__(self):
        return self.id.__hash__()

    
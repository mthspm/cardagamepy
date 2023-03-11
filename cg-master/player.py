class Player:

    def __init__(self, user, id):
        self.user = user
        self.id = id
        self._maxlife = 30
        self._maxmana = 10
        self._life = 30
        self._mana = 0
        self._hero = None
        self._deck = []
        self._hand = []
        self._board = []

    def __str__(self):
        return self.user

    def __hash__(self):
        return self.id.__hash__()
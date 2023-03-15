from tags import *

class BaseCard:
    def __init__(self,data) -> None:

        self.name = data.get("name")
        self.type = data.get("type")
        self.rarity = data.get("rarity")
        self.info = data.get("info")
        self.manacost = data.get("manacost")
        self.effect = data.get("effect")
        self.img = data.get("img") #?
        self._zone = Zone.INVALID

    def __str__(self):
        return (f'{self.name} : {self.type}')

    def __hash__(self):
        return self.id.__hash__()

    def __eq__(self, other):
        return self.id == other.id

    @property
    def zone(self):
        return self._zone

    @zone.setter
    def zone(self, value):
        self._set_zone(value)

    def _set_zone(self, value):
        """
        __sumary__
        value == target to place the card

        [Deck <-> Hand <-> BOARD <-> GRAVEYARD <-> ...]
        __end__
        """

        old = self._zone

        if old == value:
            return

        zones = {
            Zone.HAND: 'funcao que mostra a mao',
            Zone.DECK: 'funcao que mostra o deck',
			Zone.GRAVEYARD: 'funcao que mostra o cemiterio',
			Zone.SETASIDE: 'funcao que coloca uma carta em campo',
        }

        if zones.get(old) is not None:
            'tira a carta da zona'

        if zones.get(value) is not None:
            'coloca a carta na zona nova'

        self._zone = value

class MinionCard(BaseCard):

    def __init__(self, data) -> None:
        super().__init__(data)
        self.hp = data.get("hp")
        self.atk = data.get("atk")
        self.guild = data.get("guild")

class SpellCard(BaseCard):

    def __init__(self, data) -> None:
        super().__init__(data)

class TrapCard(BaseCard):

    def __init__(self, data) -> None:
        super().__init__(data)

class WeaponCard(BaseCard):

    def __init__(self, data) -> None:
        super().__init__(data)
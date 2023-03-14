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

        old = self.zone

        if old == value:
            return

        """
        value == target to place the card

        [Deck <-> Hand <-> BOARD <-> GRAVEYARD <-> ...]
        """
        zones = {
            Zone.HAND: 'funcao pra ir pra mao',
            Zone.DECK: '...',
			Zone.GRAVEYARD: '...',
			Zone.SETASIDE: '...',
        }

        self._zone = value

        if zones.get(old) is not None:
            zones[old].remove(self)




    


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
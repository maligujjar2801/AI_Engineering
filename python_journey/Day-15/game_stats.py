class GameCharacter :
    def __init__(self,name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self) :
        return self._name
    
    @property 
    def health(self):
        return self._health
    
    @health.setter
    def health(self,other):
        if other < 0 :
            self._health = 0
        elif other > 100 :
            self._health = 100
        else :
            self._health = other
    
    @property
    def mana(self):
        return self._mana
    
    @mana.setter 
    def mana(self,other):
        if other < 0 :
            self._mana = 0
        elif other > 50 :
            self._mana = 50
        else :
            self._mana = other

    @property 
    def level(self) :
        return self._level  
    
    def level_up(self) :
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")
    def __str__(self) :
        return f"Name: {self._name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"

hero = GameCharacter("Ali")
print(hero)

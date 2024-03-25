from playermodel import SuperPlayer

# Voici ici un exemple d'un héritage. Un héritage est la copie d'une classe (parent) à une autre 
# classe (son fils) 
class Guerrier (SuperPlayer):
        def __init__(self, pseudo):
            super().__init__(pseudo)
            self.armor = 3                    
        def damage(self, damage):   
            if self.armor > 0:
                self.armor -= 1
                damage = 0
            super().damage(damage)
        def re_armor(self):
            self.armor = 3
        def get_armor(self):
            return self.armor
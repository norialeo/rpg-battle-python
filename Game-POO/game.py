import random

class Personagem:
    '''Classe mae do projeto'''
    def __init__(self, name, life, level):
        self.__name = name
        self.__life = life
        self.__level = level
        
    def get_name(self):
        return self.__name
    
    def get_life(self):
        return self.__life
    
    def get_level(self):
        return self.__level
    
    def show_attributes(self):
        return f"Name: {self.get_name()}\nLife: {self.get_life()}\nLevel: {self.get_level()}"
    
    def receive_attack(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0

    def attack(self, target):
        damage = random.randint(self.get_level() * 2, self.get_level() * 4)
        target.receive_attack(damage)
        if damage == self.get_level() * 4:
            print(print(f"\n{self.get_name()} atacou {target.get_name()} e causou um ataque critico de {damage} de dano!"))
        else:
            print(f"\n{self.get_name()} atacou {target.get_name()} e causou {damage} de dano!")


class Heroi(Personagem):
    '''Classe para criação do personagem do usuário'''
    def __init__(self, name, life, level, ability):
        super().__init__(name, life, level)
        self.__ability = ability
    
    def get_ability(self):
        return self.__ability
    
    def show_attributes(self):
        return f"{super().show_attributes()}\nAbility: {self.get_ability()}\n"
    
    def special_attack(self, target):
        damage = random.randint(self.get_level() * 5, self.get_level() * 8)
        target.receive_attack(damage)
        if damage == self.get_level() * 8:
            print(f"\n{self.get_name()} usou a habilidade especial {self.get_ability()} em {target.get_name()} e causou um ataque critico de {damage} de dano!")
        else:
            print(f"\n{self.get_name()} usou a habilidade especial {self.get_ability()} em {target.get_name()} e causou {damage} de dano!")
    
    
class Inimigo(Personagem):
    '''Classe para criação dos inimigos do usuário'''
    def __init__(self, name, life, level, type):
        super().__init__(name, life, level)
        self.__type = type
        
    def get_type(self):
        return self.__type
    
    def show_attributes(self):
        return f"{super().show_attributes()}\nType: {self.get_type()}\n"


class Game:
    '''Classe orquestradora do jogo'''
    def __init__(self):
        self.heroi = Heroi(name="Hero", life=100, level=5, ability="Strength")
        self.inimigo = Inimigo(name="Snake", life=80, level=5, type="Flying")
    
    def start_battle(self):
        '''Função para gestão da batalha em turnos'''
        print("Iniciando a batalha!")
        while self.heroi.get_life() > 0 and self.inimigo.get_life() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.show_attributes())
            print(self.inimigo.show_attributes())

            input("Pressione enter para atacar...")
            escolha = input("Escolha: \n 1 - Ataque Normal \n 2 - Ataque Especial \n")
            
            if escolha == "1":
                self.heroi.attack(target=self.inimigo)
            elif escolha == "2":
                self.heroi.special_attack(target=self.inimigo)
            else:
                print("Escolha inválida, escolha novamente!")
            
            if self.inimigo.get_life() > 0:
                self.inimigo.attack(target=self.heroi)

        if self.heroi.get_life() > 0:
            print("\nParabens, você venceu a batalha!\n")
        else:
            print("\nVocê foi derrotado!") 




game = Game()
game.start_battle()
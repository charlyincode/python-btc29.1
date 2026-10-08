class Attack :
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Pokemon:
    def __init__(self,name,attacks,hp):
        self.name = name
        self.attacks = attacks
        self.hp = hp

    def attack(self, index, opponent):
        selected_attack = self.attacks[index]
        opponent.hp -= selected_attack.damage

class Battle:
    def __init__(self,pokemon1,pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def run(self):
        attacker = self.pokemon1
        defender = self.pokemon2
        while attacker.hp >0 and defender.hp > 0:
            print(f"{self.pokemon1.name} : {self.pokemon1.hp} hp")
            print(f"{self.pokemon2.name} : {self.pokemon2.hp} hp")
            print(f"C'est au tour de {attacker.name} d'attaquer !")
            print("Choisissez une attaque : ")
            list_attacks = attacker.attacks
            for i in range(len(list_attacks)):
                print(f"{i} : {list_attacks[i].name}")
            choice = int(input("Votre choix : "))
            attacker.attack(choice,defender)
            attacker, defender = defender, attacker

pikachu = Pokemon("Pikachu",[Attack("fatal-foudre",150), Attack('Tonnerre',90)],500)
salameche = Pokemon('Salameche',[Attack("lance-flamme",120),Attack("Deflagration",150)],500)
battle = Battle(pikachu,salameche)
battle.run()
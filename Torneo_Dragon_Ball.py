
# #42 TORNEO DRAGON BALL
import random


## Dificultad: Difícil | Publicación: 14/10/24 | Corrección: 21/10/24

## Ejercicio

'''
/*
 * EJERCICIO:
 * ¡El último videojuego de Dragon Ball ya está aquí!
 * Se llama Dragon Ball: Sparking! ZERO.
 *
 * Simula un Torneo de Artes Marciales, al más puro estilo
 * de la saga, donde participarán diferentes luchadores, y el
 * sistema decidirá quién es el ganador.
 *
 * Luchadores:
 * - Nombre.
 * - Tres atributos: velocidad, ataque y defensa
 *   (con valores entre 0 a 100 que tú decidirás).
 * - Comienza cada batalla con 100 de salud.
 * Batalla:
 * - En cada batalla se enfrentan 2 luchadores.
 * - El luchador con más velocidad comienza atacando.
 * - El daño se calcula restando el daño de ataque del
 *   atacante menos la defensa del oponente.
 * - El oponente siempre tiene un 20% de posibilidad de
 *   esquivar el ataque.
 * - Si la defensa es mayor que el ataque, recibe un 10%
 *   del daño de ataque.
 * - Después de cada turno y ataque, el oponente pierde salud.
 * - La batalla finaliza cuando un luchador pierde toda su salud.
 * Torneo:
 * - Un torneo sólo es válido con un número de luchadores
 *   potencia de 2.
 * - El torneo debe crear parejas al azar en cada ronda.
 * - Los luchadores se enfrentan en rondas eliminatorias.
 * - El ganador avanza a la siguiente ronda hasta que sólo
 *   quede uno.
 * - Debes mostrar por consola todo lo que sucede en el torneo,
 *   así como el ganador.
 */
'''
class Fighter:
    def __init__(self, name: str, speed:int, attack:int, defense:int):
        self.name = name
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.health = 100
        
    def reset_health(self):
        self.health = 100 
    
    def is_alive(self) -> bool:
        return self.health > 0 
    
    def take_damage(self, damage:int):
        
        attack_damage = 0
        
        if random.random() < 0.2:
            print(f"{self.name} ha esquivado el ataque!")
        else:
            if self.defense >= damage:
                attack_damage = damage * 0.1
            else:
                attack_damage = damage - self.defense
                
                
        self.health = max(self.health - attack_damage, 0)
        print(f"{self.name} recibe {attack_damage} de daño") 
        print(f"Salud restante de {self.name}: {self.health}")
            
        
class Battle:
    
    def __init__(self, fighter1: Fighter, fighter2: Fighter):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        
    def fight(self)-> Fighter:
        
        print(f"\n=== BATALLA ENTRE {self.fighter1.name} vs. {self.fighter2.name} ===")
        
        while self.fighter1.is_alive() and self.fighter2.is_alive():
            
            if self.fighter1.speed >= self.fighter2.speed:
                self.turn(self.fighter1, self.fighter2)
                if self.fighter2.is_alive():
                    self.turn(self.fighter2, self.fighter1)
            else:
                self.turn(self.fighter2, self.fighter1)
                if self.fighter1.is_alive():
                    self.turn(self.fighter1, self.fighter2)
            
        
        if self.fighter1.is_alive(): 
            print(f"\n*** {self.fighter1.name} GANA LA BATALLA! ***")
            return self.fighter1
        else:
            print(f"\n*** {self.fighter2.name} GANA LA BATALLA! ***")   
            return self.fighter2
    
    def turn(self, attacker: Fighter, defender: Fighter):
        print(f"\n{attacker.name} ataca a {defender.name}")  
        defender.take_damage(attacker.attack)
        

fighter1 = Fighter("Goku", 90, 95, 80)
fighter2 = Fighter("Vegeta", 95, 90, 82)

battle = Battle(fighter1, fighter2)
winner = battle.fight()
print(f"Ganador: {winner.name}")
import random
import time

player_hp = 100
monster_hp = 60

print("⚔️ A wild Goblin approaches! ⚔️\n")
time.sleep(1)
while player_hp > 0 and monster_hp > 0:
    choice = input("Do you want to (A)ttack or (H)eal? ")
    if choice == "A":
        damage = random.randint(10, 20)
        monster_hp -= damage
        print(f"You attack the Goblin for {damage} damage! Goblin HP: {monster_hp}")
        time.sleep(1)
    elif choice == "H":
        heal = random.randint(5, 15)
        player_hp += heal
        print(f"You heal yourself for {heal} HP! Your HP: {player_hp}")
        time.sleep(1)

    if monster_hp > 0:
            monster_damage = random.randint(5, 15)
            player_hp -= monster_damage
            print(f"The Goblin attacks you for {monster_damage} damage! Your HP: {player_hp}")
            goblin_heal = random.randint(5, 10)
            monster_hp += goblin_heal
            print(f"The Goblin heals itself for {goblin_heal} HP! Goblin HP: {monster_hp}")
    time.sleep(1)

if player_hp <= 0:
    print("You have been defeated by the Goblin! 💀")
elif monster_hp <= 0:
    print("You have defeated the Goblin! 🎉")

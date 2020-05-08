from classes.game import Person, bcolours
from classes.magic import spell
from classes.inventory import Item
import random


# CREATE BLACK MAGIC

fire = spell("fire", 25, 600, "black")
thunder = spell("thunder", 25, 600, "black")
blizzard = spell("blizzard", 25, 600, "black")
meteor = spell("meteor", 40, 1200, "black")
quake = spell("quake", 14, 140, "black")


# CREATE WHITE MAGIC
cure = spell("cure", 25, 620, "white")
cura = spell("cura", 32, 1500, "white")


# CREATE SOME ITEMS
potion = Item("potion", "potion", "heals 50 hp", 50)
hipotion = Item("hipotion", "potion" , "heals for 100 hp", 100)
superpotion = Item("superpotion", "potion", "heals for 500 hp", 500)
elixer = Item("elixer", "elixer", "FULLY RESTORES THE HP/MP OF ONE  PARTY MEMBER", 9999)
hielixer = Item("megaelixer", "elixer", "fully restores the party's hp /mp" , 9999)

grenade = Item("grenade", "attack", "deals 500 damage", 500)

player_spell = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_item = [potion, hipotion, superpotion, elixer, hielixer, grenade]

# INSTANTIATE THE PLAYER
player1 = Person("valos", 3260, 132, 34, 300, player_spell, player_item)
player2 = Person("nick ", 4160, 188, 34, 320, player_spell, player_item)
player3 = Person("robot", 3089, 174, 34, 288, player_spell, player_item)

enemy1 = Person("imp  ", 1250, 130, 325, 560, [], [])
enemy2 = Person("magus", 18200, 700, 25, 525, [], [])
enemy3 = Person("imp  ", 1250, 130, 325, 560, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]
running = True
i = 0
print(bcolours.FAIL + bcolours.BOLD + "AN ENEMY ATTACK!" + bcolours.ENDC)

while running:
    print("====================")
    print("NAME                  HP                                  MP")
    print()

    for item in players:
        item.get_stats()

    for enemy in enemies:
        enemy.get_enemy_stats()


    for player in players:

        player.choose_action()
        choice = input("   choose action")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)
            print("you attacked " + enemies[enemy].name + "for", dmg)
        if enemies[0].get_hp() == 0:
            print(enemies[enemy].name + "has died ")
            del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("CHOOSE MAGIC:")) -1

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            if magic_choice == -1:
                continue
            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print("    " + bcolours.FAIL + "\n not enough mp\n" + bcolours.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print("    " + bcolours.OKBLUE + "\n" + spell.name + "heals for",str(magic_dmg), "hp:"+ bcolours.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)
                print("    " + bcolours.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage to" + enemies[enemy].name + bcolours.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died ")
                    del enemies[enemy]

        elif index == 2:
            player.choose_item()
            choose_item = int(input("CHOOSE ITEMS:")) - 1

            if choose_item == -1:
                continue

            item = player.items[choose_item]

            if player.items[choose_item] == 0:
                print(bcolours.OKGREEN + "\n" + " none left...." + bcolours.ENDC)
                continue


            if item.type == "potion":
                player.heal(item.prop)
                print(bcolours.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "hp" + bcolours.ENDC)
            elif item.type == "elixer":

                if item.name == "megaelixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp

                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolours.OKGREEN + "\n" + item.name + "fully restores hp/mp" + bcolours.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(item.prop)
                print(bcolours.FAIL + "\n" + item.name + "deals", str(item.prop), "points of damage to" + enemies[enemy].name + bcolours.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy.name] + "has died")
                    del enemies[enemy]


    enemy_choice = 1
    target = random.randrange(0, 2)
    enemy_dmg = enemies[0].generate_damage()

    players[target].take_damage(enemy_dmg)
    print("enemy attack for", enemy_dmg)
    if players[target].get_hp() == 0:
        print(players[target].name + " has died")
        del players[target]


    defeated_enemies = 0
    defeated_players = 0
    for enemy in enemies:
        if defeated_enemies == 0:
            defeated_enemies += 1
    for player in players:
        if defeated_players == 0:
            defeated_players += 1
    if defeated_enemies == 2:
        print(bcolours.OKGREEN + "YOU WIN" + bcolours.ENDC)
        running = False

    elif defeated_players == 2:
        print(bcolours.FAIL + "your enemy has defeated you" + bcolours.ENDC)
        running = False

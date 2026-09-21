import time

monster = {
    "Name": "Goblin",
    "Health": 60,

    }

print(f"A wild {monster['Name']} appeared with {monster['Health']} hp!")

time.sleep(1)
monster["Health"] -= 20
print(f"You attacked the {monster['Name']} for 20 damage! It now has {monster['Health']} hp left.")
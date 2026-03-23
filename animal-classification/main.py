print("\nIn main.py...")

# import vertebrates.cold_blooded.fish as cb_fish
# print("\nFish Attributes")
# print(f"has fins: {cb_fish.has_fins}")
# print(f"has scales: {cb_fish.has_scales}")
# print(f"breathes through: {cb_fish.breathes_through}")

# print("\nShark Attributes")
# print(f"has fins: {cb_fish.shark.has_fins}")
# print(f"has scales: {cb_fish.shark.has_scales}")
# print(f"breathes through: {cb_fish.shark.breathes_through}")

# print("\nDorado Attributes")
# print(f"has fins: {cb_fish.dorado.has_fins}")
# print(f"has scales: {cb_fish.dorado.has_scales}")
# print(f"breathes through: {cb_fish.dorado.breathes_through}")

# import vertebrates.cold_blooded.amphibians
# print("\nAmphibian Attributes")
# print(f"egg_type: {vertebrates.cold_blooded.amphibians.attributes.egg_type}")
# print(f"skin_type: {vertebrates.cold_blooded.amphibians.attributes.skin_type}")
# print(f"breathes_through: {vertebrates.cold_blooded.amphibians.attributes.breathes_through}")

# import vertebrates.cold_blooded.amphibians as amphibians
# import sys
# for k,v in sys.modules.items():
#     if "vertebrates" in k:
#         print(f"{k}:\n{v}}}")
# print("\nAmphibian Attributes")
# print(f"egg_type: {vertebrates.cold_blooded.amphibians.egg_type}")
# print(f"skin_type: {vertebrates.cold_blooded.amphibians.skin_type}")
# print(f"breathes_through: {vertebrates.cold_blooded.amphibians.breathes_through}")

# print("\nFrog Attributes")
# print(f"egg_type: {amphibians.frog.egg_type}") # both work? Does both the alias and the original module get bound at runtime?
# print(f"skin_type: {vertebrates.cold_blooded.amphibians.frog.skin_type}")
# print(f"breathes_through: {vertebrates.cold_blooded.amphibians.frog.breathes_through}")

# print("\nNewt Attributes")
# print(f"egg_type: {vertebrates.cold_blooded.amphibians.newt.egg_type}")
# print(f"skin_type: {vertebrates.cold_blooded.amphibians.newt.skin_type}")
# print(f"breathes_through: {vertebrates.cold_blooded.amphibians.newt.breathes_through}")

# import vertebrates.cold_blooded.reptiles
# print("\nReptile Attributes")
# print(f"egg_type: {vertebrates.cold_blooded.reptiles.skin_type}")
# print(f"skin_type: {vertebrates.cold_blooded.reptiles.lays_eggs}")
# print(f"breathes_through: {vertebrates.cold_blooded.reptiles.has_scales}")

# print("\nSnake Attributes")
# print(f"egg_type: {vertebrates.cold_blooded.reptiles.snake.skin_type}")
# print(f"skin_type: {vertebrates.cold_blooded.reptiles.snake.lays_eggs}")
# print(f"breathes_through: {vertebrates.cold_blooded.reptiles.snake.has_scales}")

# print("\nLizard Attributes")
# print(f"egg_type: {vertebrates.cold_blooded.reptiles.lizard.skin_type}")
# print(f"skin_type: {vertebrates.cold_blooded.reptiles.lizard.lays_eggs}")
# print(f"breathes_through: {vertebrates.cold_blooded.reptiles.lizard.has_scales}")

def call_birds():
    import vertebrates.warm_blooded.birds # this is now a lazy import since it will only be run when the call_birds() function runs
    print("\nBird Attributes")
    print(f"has_wings: {vertebrates.warm_blooded.birds.has_wings}")
    print(f"has_feathers: {vertebrates.warm_blooded.birds.has_feathers}")
    print(f"egg_type: {vertebrates.warm_blooded.birds.egg_type}")

    print("\nParrot Attributes")
    print(f"has_wings: {vertebrates.warm_blooded.birds.parrot.has_wings}")
    print(f"has_feathers: {vertebrates.warm_blooded.birds.parrot.has_feathers}")
    print(f"egg_type: {vertebrates.warm_blooded.birds.parrot.egg_type}")

    print("\nToucan Attributes")
    print(f"has_wings: {vertebrates.warm_blooded.birds.toucan.has_wings}")
    print(f"has_feathers: {vertebrates.warm_blooded.birds.toucan.has_feathers}")
    print(f"egg_type: {vertebrates.warm_blooded.birds.toucan.egg_type}")

# import vertebrates.warm_blooded.mammals
# print("\nMammal Attributes")
# print(f"has_hair: {vertebrates.warm_blooded.mammals.has_hair}")
# print(f"birth_type: {vertebrates.warm_blooded.mammals.birth_type}")
# print(f"breathes_through: {vertebrates.warm_blooded.mammals.breathes_through}")

# print("\nKoala Attributes")
# print(f"has_hair: {vertebrates.warm_blooded.mammals.koala.has_hair}")
# print(f"birth_type: {vertebrates.warm_blooded.mammals.koala.birth_type}")
# print(f"breathes_through: {vertebrates.warm_blooded.mammals.koala.breathes_through}")

# print("\nPlatypus Attributes")
# print(f"has_hair: {vertebrates.warm_blooded.mammals.platypus.has_hair}")
# print(f"birth_type: {vertebrates.warm_blooded.mammals.platypus.birth_type}")
# print(f"breathes_through: {vertebrates.warm_blooded.mammals.platypus.breathes_through}")
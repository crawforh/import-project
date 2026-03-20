print("\nIn main.py...")

import vertebrates.cold_blooded.fish
print("Fish Attributes")
print(f"has fins: {vertebrates.cold_blooded.fish.has_fins}")
print(f"has scales: {vertebrates.cold_blooded.fish.has_scales}")
print(f"breathes through: {vertebrates.cold_blooded.fish.breathes_through}")

print("Shark Attributes")
print(f"has fins: {vertebrates.cold_blooded.fish.shark.has_fins}")
print(f"has scales: {vertebrates.cold_blooded.fish.shark.has_scales}")
print(f"breathes through: {vertebrates.cold_blooded.fish.shark.breathes_through}")


import vertebrates.cold_blooded.amphibians.attributes # nothing in amphibians.__init__.py so need to import the attributes module
print("\nAmphibian Attributes")
print(f"egg_type: {vertebrates.cold_blooded.amphibians.attributes.egg_type}")
print(f"skin_type: {vertebrates.cold_blooded.amphibians.attributes.skin_type}")
print(f"breathes_through: {vertebrates.cold_blooded.amphibians.attributes.breathes_through}")

import vertebrates.cold_blooded.amphibians.frog # nothing in amphibians.__init__.py so reimporting to add frog attribute access (can also do this for newt)
print("\nFrog Attributes")
print(f"egg_type: {vertebrates.cold_blooded.amphibians.frog.egg_type}")
print(f"skin_type: {vertebrates.cold_blooded.amphibians.frog.skin_type}")
print(f"breathes_through: {vertebrates.cold_blooded.amphibians.frog.breathes_through}")

from vertebrates.cold_blooded.amphibians import newt # nothing in amphibians.__init__.py so reimporting to add newt attribute access
print("\nNewt Attributes")
print(f"egg_type: {vertebrates.cold_blooded.amphibians.newt.egg_type}")
print(f"skin_type: {vertebrates.cold_blooded.amphibians.newt.skin_type}")
print(f"breathes_through: {vertebrates.cold_blooded.amphibians.newt.breathes_through}")

import vertebrates.cold_blooded.reptiles
print("\nReptile Attributes")
print(f"egg_type: {vertebrates.cold_blooded.reptiles.skin_type}")
print(f"skin_type: {vertebrates.cold_blooded.reptiles.lays_eggs}")
print(f"breathes_through: {vertebrates.cold_blooded.reptiles.has_scales}")

print("\nSnake Attributes")
print(f"egg_type: {vertebrates.cold_blooded.reptiles.snake.skin_type}")
print(f"skin_type: {vertebrates.cold_blooded.reptiles.snake.lays_eggs}")
print(f"breathes_through: {vertebrates.cold_blooded.reptiles.snake.has_scales}")

print("\nLizard Attributes")
print(f"egg_type: {vertebrates.cold_blooded.reptiles.lizard.skin_type}")
print(f"skin_type: {vertebrates.cold_blooded.reptiles.lizard.lays_eggs}")
print(f"breathes_through: {vertebrates.cold_blooded.reptiles.lizard.has_scales}")

import vertebrates.warm_blooded.birds
print("\nBird Attributes")
print(f"has_wings: {vertebrates.warm_blooded.birds.has_wings}")
print(f"has_feathers: {vertebrates.warm_blooded.birds.has_feathers}")
print(f"egg_type: {vertebrates.warm_blooded.birds.egg_type}")

import vertebrates.warm_blooded.birds.parrot
print("\nParrot Attributes")
print(f"has_wings: {vertebrates.warm_blooded.birds.parrot.has_wings}")
print(f"has_feathers: {vertebrates.warm_blooded.birds.parrot.has_feathers}")
print(f"egg_type: {vertebrates.warm_blooded.birds.parrot.egg_type}")

import vertebrates.warm_blooded.mammals.attributes
print("\nMammal Attributes")
print(f"has_hair: {vertebrates.warm_blooded.mammals.attributes.has_hair}")
print(f"birth_type: {vertebrates.warm_blooded.mammals.attributes.birth_type}")
print(f"breathes_through: {vertebrates.warm_blooded.mammals.attributes.breathes_through}")

import vertebrates.warm_blooded.mammals.koala
print("\nKoala Attributes")
print(f"has_hair: {vertebrates.warm_blooded.mammals.koala.has_hair}")
print(f"birth_type: {vertebrates.warm_blooded.mammals.koala.birth_type}")
print(f"breathes_through: {vertebrates.warm_blooded.mammals.koala.breathes_through}")

import vertebrates.warm_blooded.mammals
print("\nPlatypus Attributes")
print(f"has_hair: {vertebrates.warm_blooded.mammals.platypus.has_hair}")
print(f"birth_type: {vertebrates.warm_blooded.mammals.platypus.birth_type}")
print(f"breathes_through: {vertebrates.warm_blooded.mammals.platypus.breathes_through}")
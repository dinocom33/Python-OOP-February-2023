from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []
        self.health = 0

    def add_pokemon(self, pokemon: Pokemon):
        pok_name, pok_health = pokemon.name, pokemon.health
        if pok_name in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pok_name)
            self.health = pok_health
            return f"Caught {pok_name} with health {pok_health}"

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name in self.pokemons:
            self.pokemons.remove(pokemon_name)
            return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n- {self.pokemons[0]} with health {self.health}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

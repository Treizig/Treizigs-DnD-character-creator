import random
import json


def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)


def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def print_options(items):
    print(", ".join(items[:-1]) + " and " + items[-1] + ".")


def main():
    Races = load_json("races.json")
    Characters = load_json("character.json")

    command = input("Commands: /roll SIDES or /create\n").strip()

    if command.startswith("/roll"):
        try:
            sides = int(command.replace("/roll", "", 1).strip())
            roll(sides)
        except ValueError:
            print("You must provide a number. Example: /roll 20")

    elif command.startswith("/create"):
        create_character(Races, Characters)
        save_json("character.json", Characters)

    else:
        print("Unknown command. Try /roll or /create.")


def roll(sides):
    print(random.randint(1, sides))

def choose_option(prompt, options):
    print(prompt)
    print_options(options)

    while True:
        choice = input("> ").lower()
        if choice in options:
            return choice
        print("Not valid. Try again.")



def create_character(races_data, characters):
    classes = ["bard","barbarian","rogue","ranger","cleric","paladin",
               "wizard","sorcerer","warlock","monk","druid","fighter"]

    char_class = choose_option("Choose your class:", classes)
    characters[0]["class"] = char_class

    race_options = list(races_data.keys())
    char_race = choose_option("Choose your race:", race_options)

    race_stats = races_data[char_race]
    characters[0].update(race_stats)

    print("Character created successfully!")
    print(json.dumps(characters[0], indent=4))

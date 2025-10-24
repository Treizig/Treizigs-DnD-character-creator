import argparse
import json
import random
from enum import Enum
from typing import Dict, List, Any


class CharacterClass(Enum):
    BARD = "bard"
    BARBARIAN = "barbarian"
    ROGUE = "rogue"
    RANGER = "ranger"
    CLERIC = "cleric"
    PALADIN = "paladin"
    WIZARD = "wizard"
    SORCERER = "sorcerer"
    WARLOCK = "warlock"
    MONK = "monk"
    DRUID = "druid"
    FIGHTER = "fighter"


class Race(Enum):
    DEEPLING = "deepling"
    DWARF = "dwarf"
    GNOME = "gnome"
    ELF = "elf"
    ZWOELF = "zwölf"
    HUMAN = "human"
    DRAGONBORN = "dragonborn"


def load_json(filename: str) -> Dict[str, Any] | List[Dict[str, Any]]:
    with open(filename, "r") as f:
        return json.load(f)


def save_json(filename: str, data: Any) -> None:
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def roll_dice(notation: str) -> List[int]:
    if "d" not in notation:
        raise ValueError("Invalid dice format. Example: 3d6")

    number, sides = notation.lower().split("d")
    number = int(number)
    sides = int(sides)

    return [random.randint(1, sides) for _ in range(number)]


def create_character(characters: List[Dict[str, Any]], races_data: Dict[str, Any],
                     chosen_class: str, chosen_race: str) -> None:

    if chosen_class not in [c.value for c in CharacterClass]:
        raise ValueError("Invalid class choice")

    if chosen_race not in [r.value for r in Race]:
        raise ValueError("Invalid race choice")

    stats = races_data[chosen_race]

    new_character = {
        "class": chosen_class,
        "race": chosen_race
    }
    new_character.update(stats)

    characters.append(new_character)
    save_json("player_character.json", characters)
    print("Character created:")
    print(json.dumps(new_character, indent=4))


def show_ascii_dragon() -> None:
    dragon = """
                   __====-_  _-====__
             _--^^^#####//      \\\\#####^^^--_
          _-^##########// (    ) \\\\##########^-_
         -############//  |\\^^/|  \\\\############-
       _/############//   (@::@)   \\\\############\\_
      /#############((     \\\\//     ))#############\\
     -###############\\\\    (oo)    //###############-
    -#################\\\\  / `' \\\\  //#################-
   -###################\\\\/      \\\\//###################-
  _#/|##########/\\######(   /\\   )######/\\##########|#\\_
 |/ |#/#\\#/\\#/\\/  \\#/\\##\\  :  /##/\\#/\\#/  \\/\\#/\\#/\\#| \\|
 `  |/  V  V  `   V  \\#\\\\|  | |  |//##/  V   '  V  V  \\|  '
                 (  \\#\\| | | | |/#/  )
                  \\  | | | | | |  /
"""
    print(dragon)


def main() -> None:
    races = load_json("Races.json")
    characters = load_json("player_character.json")

    parser = argparse.ArgumentParser(description="D&D Helper Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    roll_parser = subparsers.add_parser("roll")
    roll_parser.add_argument("dice", type=str, help="Dice format NdM (example: 3d6)")

    create_parser = subparsers.add_parser("create")
    create_parser.add_argument("--classs", required=True, help="Character class")
    create_parser.add_argument("--race", required=True, help="Character race")

    dragon_parser = subparsers.add_parser("dragon")

    args = parser.parse_args()

    if args.command == "roll":
        results = roll_dice(args.dice)
        print(f"Roll results: {results}  Total: {sum(results)}")

    elif args.command == "create":
        create_character(characters, races, args.classs.lower(), args.race.lower())

    elif args.command == "dragon":
        show_ascii_dragon()


if __name__ == "__main__":
    main()

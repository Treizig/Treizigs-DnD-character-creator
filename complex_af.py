"""
D&D Helper CLI (Option 1 storage: single player_character.json file)

Features:
- roll NdM (e.g. 3d6)
- create characters (random or manual)
- 5e stat generation (4d6 drop lowest)
- special case: race "zwölf" => 12 points evenly distributed (2 each) before racial bonuses
- list & delete characters
- ASCII dragon
- colored terminal output via colorama
"""

from __future__ import annotations
import argparse
import json
import random
from enum import Enum
from pathlib import Path
from typing import Dict, List, Any, Tuple
from colorama import init as colorama_init, Fore, Style

colorama_init(autoreset=True)

DATA_FILE = Path("player_character.json")
RACES_FILE = Path("Races.json")


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


# Race enum values should match keys in your Races.json (we use string values).
class Race(Enum):
    DEEPLING = "deepling"
    DWARF = "dwarf"
    GNOME = "gnome"
    ELF = "elf"
    ZWOELF = "zwölf"
    HUMAN = "human"
    DRAGONBORN = "dragonborn"


ABILITIES = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]


def load_json_file(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json_file(path: Path, data: Any) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def roll_die(sides: int) -> int:
    return random.randint(1, sides)


def roll_dice_notation(notation: str) -> List[int]:
    """
    Accepts NdM or dM (e.g. 3d6 or d20), returns list of individual die results.
    """
    notation = notation.strip().lower()
    if "d" not in notation:
        raise ValueError("Invalid dice notation. Use NdM, e.g. 3d6 or d20.")
    parts = notation.split("d")
    if parts[0] == "":
        n = 1
    else:
        n = int(parts[0])
    m = int(parts[1])
    if n < 1 or m < 1:
        raise ValueError("Dice counts and sides must be positive.")
    return [roll_die(m) for _ in range(n)]


def roll_4d6_drop_lowest() -> int:
    rolls = [roll_die(6) for _ in range(4)]
    return sum(sorted(rolls)[1:])  # drop lowest


def generate_6_ability_scores(race_value: str | None = None) -> Tuple[Dict[str, int], Dict[str, int]]:
    """
    Returns (raw_stats, final_stats_without_racebonuses).
    raw_stats = the base scores BEFORE racial bonuses (what player "rolled")
    final_stats = raw_stats (we'll later apply racial bonuses to produce modified stats)
    Special-case: if race_value == "zwölf", we set raw stats to equal distribution of 12 pts:
      - evenly distributed across 6 abilities -> 12 // 6 = 2 each (sum 12).
      This is deliberately exactly what you requested.
    """
    raw: Dict[str, int] = {}
    if race_value and race_value == "zwölf":
        # 12 points evenly across 6 abilities -> each 2 (user request)
        for a in ABILITIES:
            raw[a] = 2
    else:
        for a in ABILITIES:
            raw[a] = roll_4d6_drop_lowest()
    # final_stats initially same as raw; racial bonuses applied later
    final = raw.copy()
    return raw, final


def apply_racial_bonuses(final_stats: Dict[str, int], races_data: Dict[str, Any], race_value: str) -> Dict[str, int]:
    """
    Apply racial bonuses from races_data. We expect races_data to contain keys for each race,
    and each race entry should be a dict with ability bonus keys, e.g. {"strength": 2, "dexterity": 1}
    If races_data doesn't contain a specific ability, it's treated as 0.
    """
    bonuses = races_data.get(race_value, {}) if isinstance(races_data, dict) else {}
    result = final_stats.copy()
    for a in ABILITIES:
        add = int(bonuses.get(a, 0)) if bonuses else 0
        result[a] = result.get(a, 0) + add
    return result


def pretty_print_character(char: Dict[str, Any], index: int | None = None) -> None:
    prefix = f"[{index}] " if index is not None else ""
    name = char.get("name", "<unnamed>")
    cclass = char.get("class", "unknown")
    crace = char.get("race", "unknown")
    print(Fore.CYAN + f"{prefix}{name} " + Style.RESET_ALL + f"({Fore.YELLOW}{cclass}{Style.RESET_ALL}, {Fore.MAGENTA}{crace}{Style.RESET_ALL})")
    raw = char.get("raw_stats", {})
    final = char.get("final_stats", {})
    for a in ABILITIES:
        raw_v = raw.get(a, 0)
        final_v = final.get(a, 0)
        # highlight difference if any racial bonus applied
        if final_v != raw_v:
            print(f"  {a.title():12}: {raw_v:2} -> {Fore.GREEN}{final_v}{Style.RESET_ALL}")
        else:
            print(f"  {a.title():12}: {final_v:2}")
    print()


def ensure_files_exist() -> None:
    # Ensure player_character.json exists (start with empty list)
    if not DATA_FILE.exists():
        save_json_file(DATA_FILE, [])
    # If RACES_FILE doesn't exist, create a minimal default to avoid crashes (user should edit actual file)
    if not RACES_FILE.exists():
        default_races = {
            "human": {},
            "elf": {"dexterity": 2},
            "dwarf": {"constitution": 2},
            "gnome": {"intelligence": 2},
            "dragonborn": {"strength": 2, "charisma": 1},
            "deepling": {},
            "zwölf": {}  # special race — handled in code
        }
        save_json_file(RACES_FILE, default_races)
        print(Fore.YELLOW + f"Created default {RACES_FILE}. Edit it to customize racial bonuses." + Style.RESET_ALL)


def random_choice_enum(enum_cls: Enum) -> str:
    return random.choice([e.value for e in enum_cls])


def create_character(
    characters: List[Dict[str, Any]],
    races_data: Dict[str, Any],
    name: str | None = None,
    class_value: str | None = None,
    race_value: str | None = None,
    randomize: bool = False
) -> Dict[str, Any]:
    # pick random class/race if requested or if missing
    if randomize:
        if not class_value:
            class_value = random_choice_enum(CharacterClass)
        if not race_value:
            race_value = random_choice_enum(Race)
    if class_value is None or race_value is None:
        raise ValueError("Class and race must be provided (or use --random).")

    class_value = class_value.lower()
    race_value = race_value.lower()

    # basic validation
    if class_value not in [c.value for c in CharacterClass]:
        raise ValueError(f"Invalid class: {class_value}")
    if race_value not in [r.value for r in Race]:
        raise ValueError(f"Invalid race: {race_value}")

    raw_stats, final_stats = generate_6_ability_scores(race_value)
    # apply racial bonuses (from Races.json)
    final_stats = apply_racial_bonuses(final_stats, races_data, race_value)

    # build character
    new_char: Dict[str, Any] = {
        "name": name or f"PC_{len(characters) + 1}",
        "class": class_value,
        "race": race_value,
        "raw_stats": raw_stats,
        "final_stats": final_stats
    }

    characters.append(new_char)
    save_json_file(DATA_FILE, characters)
    return new_char


ASCII_DRAGON = r"""
                   __====-_  _-====__
             _--^^^#####//      \\#####^^^--_
          _-^##########// (    ) \\##########^-_
         -############//  |\^^/|  \\############-
       _/############//   (@::@)   \\############\_
      /#############((     \\//     ))#############\
     -###############\\    (oo)    //###############-
    -#################\\  / `' \\  //#################-
   -###################\\/      \\//###################-
  _#/|##########/\######(   /\   )######/\##########|#\_
 |/ |#/\#/\#/\/  \#/\##\  :  /##/\#/\/  \/ \/\#/\#/\#| \|
 `  |/  V  V  `   V  \#\\|  | |  |//##/  V   '  V  V  \|  '
                 (  \#\| | | | |/#/  )
                  \  | | | | | |  /
"""

def list_characters(characters: List[Dict[str, Any]]) -> None:
    if not characters:
        print(Fore.YELLOW + "No characters found." + Style.RESET_ALL)
        return
    for idx, ch in enumerate(characters):
        pretty_print_character(ch, index=idx)


def delete_character(characters: List[Dict[str, Any]], index: int) -> bool:
    if index < 0 or index >= len(characters):
        return False
    removed = characters.pop(index)
    save_json_file(DATA_FILE, characters)
    print(Fore.RED + f"Deleted character: {removed.get('name', '<unnamed>')}" + Style.RESET_ALL)
    return True


def main() -> None:
    ensure_files_exist()
    races_data = load_json_file(RACES_FILE, {})
    characters = load_json_file(DATA_FILE, [])

    parser = argparse.ArgumentParser(description="D&D Helper CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    # roll subcommand
    sp_roll = sub.add_parser("roll", help="Roll NdM dice, e.g. 3d6 or d20")
    sp_roll.add_argument("dice", type=str, help="Dice notation NdM (example: 3d6)")

    # create subcommand
    sp_create = sub.add_parser("create", help="Create a character")
    sp_create.add_argument("--name", type=str, help="Character name (optional)")
    sp_create.add_argument("--class", dest="class_value", type=str, help="Character class (e.g. wizard)")
    sp_create.add_argument("--race", dest="race_value", type=str, help="Character race (e.g. elf)")
    sp_create.add_argument("--random", dest="randomize", action="store_true", help="Randomize class & race if not provided")

    # list subcommand
    sp_list = sub.add_parser("list", help="List all characters")

    # delete subcommand
    sp_delete = sub.add_parser("delete", help="Delete a character by index (use 'list' to see indices)")
    sp_delete.add_argument("index", type=int, help="Index of character to delete (0-based)")

    # dragon subcommand
    sp_dragon = sub.add_parser("dragon", help="Show ASCII dragon (for morale)")

    args = parser.parse_args()

    if args.command == "roll":
        try:
            results = roll_dice_notation(args.dice)
            total = sum(results)
            print(Fore.CYAN + f"Rolls: {results}  Total: {total}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "Error rolling dice: " + str(e) + Style.RESET_ALL)

    elif args.command == "create":
        try:
            new_char = create_character(
                characters=characters,
                races_data=races_data,
                name=args.name,
                class_value=(args.class_value.lower() if args.class_value else None),
                race_value=(args.race_value.lower() if args.race_value else None),
                randomize=args.randomize
            )
            print(Fore.GREEN + "Character created:" + Style.RESET_ALL)
            pretty_print_character(new_char)
        except Exception as e:
            print(Fore.RED + "Failed to create character: " + str(e) + Style.RESET_ALL)

    elif args.command == "list":
        list_characters(characters)

    elif args.command == "delete":
        idx = args.index
        if not delete_character(characters, idx):
            print(Fore.RED + f"Invalid index: {idx}" + Style.RESET_ALL)

    elif args.command == "dragon":
        print(Fore.MAGENTA + ASCII_DRAGON + Style.RESET_ALL)


if __name__ == "__main__":
    main()

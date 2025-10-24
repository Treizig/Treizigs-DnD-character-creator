D&D Helper CLI
==============

A command-line assistant for **Dungeons & Dragons** players and Dungeon Masters.  
Supports **dice rolling**, **character creation**, **listing & deleting characters**, and even **ASCII dragons** 🐉.  
Fully customizable, colorful terminal output, and follows **D&D 5e standard rules**.

* * *

Features
--------

*   **Roll dice using standard notation** (`NdM` or `dM`)
    
*   **Create characters**:
    
    *   Manual class and race selection
        
    *   Random class and race generation
        
    *   Standard 5e stat generation (4d6 drop lowest)
        
    *   Special race `"zwölf"` with 12 points evenly distributed
        
*   **Apply racial bonuses** from `Races.json`
    
*   **Colorful, readable terminal output** using `colorama`
    
*   **List and delete characters** saved in `player_character.json`
    
*   **ASCII dragon command** for morale and fun
    

* * *

Requirements
------------

*   Python **3.9+**
    
*   `colorama` library


```bash
pip install colorama
```

* * *

Installation
------------

1.  Clone or download this repository
    
2.  Ensure `Races.json` exists in the same folder (contains racial bonuses).
    
3.  `player_character.json` will be created automatically if missing.
    

* * *

Races.json Example
------------------

```json
{
    "human": {

    },
    "elf": {
        "dexterity": 2
    },
    "dwarf": {
        "constitution": 2
    },
    "gnome": {
        "intelligence": 2
    },
    "dragonborn": {
        "strength": 2,
        "charisma": 1
    },
    "deepling": {

    },
    "zwölf": {

    }
}
```

*   Use `zwölf` for a special 12-point evenly distributed character.
    
*   All other races apply bonuses on top of rolled stats.
    

* * *

Usage
-----

### Roll dice


```bash
python complex_af.py roll 3d6 python complex_af.py roll d20
```

*   Rolls dice using standard notation.
    
*   Outputs individual rolls and total.
    

* * *

### Create a character

#### Random character


```bash
python complex_af.py create --random
```

#### Manual character


```bash
python complex_af.py create --name "Asha" --class wizard --race elf
``` 

*   Stats are generated using **4d6 drop the lowest** per ability.
    
*   Racial bonuses are applied automatically.
    

* * *

### List characters


```bash
python complex_af.py list
```

*   Shows all saved characters with color-coded stats.
    
*   Lists indices for easy deletion.
    

* * *

### Delete a character


```bash
python complex_af.py delete 1
```

*   Deletes character at index `1` (0-based).
    
*   Use `list` first to see indices.
    

* * *

Character Storage
-----------------

*   Characters are saved in **`player_character.json`** (a list).
    
*   Example entry:
    


```json
{
    "name": "PC_1",
    "class": "wizard",
    "race": "elf",
    "raw_stats": {
        "strength": 12,
        "dexterity": 15,
        "constitution": 13,
        "intelligence": 14,
        "wisdom": 10,
        "charisma": 8
    },
    "final_stats": {
        "strength": 12,
        "dexterity": 17,
        "constitution": 13,
        "intelligence": 14,
        "wisdom": 10,
        "charisma": 8
    }
}
```

* * *

Notes
-----

*   The CLI uses **standard 5e rolling rules**: `4d6 drop the lowest` per ability.
    
*   Special race `"zwölf"` is unique: base stats = 2 per ability (total 12) before bonuses.
    
*   Customize `Races.json` to add new races or modify racial bonuses.
    
*   All commands are color-coded for readability.
    

* * *

Next Planned Features
---------------------

*   Point-buy or standard array stat methods
    
*   One JSON file per character for easier management
    
*   Printable character sheets
    
*   Extended race/class/customization options
    

* * *

Example Workflow
----------------


```bash
# Roll dice
python complex_af.py roll 4d6
# Create a random character
python complex_af.py create --random
# List all characters
python complex_af.py list
# Delete a character by index
python complex_af.py delete 0
```

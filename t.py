import random
import json


with open('Classes.json') as json_file:
    Class_list = json.load(json_file)

with open('Races.json') as json_file:
    Races = json.load(json_file)

with open('Allignments.json') as json_file:
    Alignment = json.load(json_file)

with open('player_character.json') as json_file:
    player_character = json.load(json_file)

user_input = str(input("Give me a command. There are he following: /roll d4, 6, 8, 10, 12, 20. /character-creation."
                       "with /roll you can roll a dice with the number of sides, that were mentioned before."
                       "With /character-creation you can start the creation process of a character for "
                       "Dungeons & Dragons."))

if user_input == '/roll d4':
    print(str(random.randint(1, 4)))
elif user_input == '/roll d6':
    print(str(random.randint(1, 6)))
elif user_input == '/roll d8':
    print(str(random.randint(1, 8)))
elif user_input == '/roll d10':
    print(str(random.randint(1, 10)))
elif user_input == '/roll d12':
    print(str(random.randint(1, 12)))
elif user_input == '/roll d20':
    print(str(random.randint(1, 20)))
elif user_input == '/roll percentile dice':
    print(str(random.randint(00, 9)*10))
    print(str(random.randint(0, 9)))
elif user_input == '/character-creation' or '/character creation':
    character_input = str(input("Would you like to create a character manuel or automatically generate one ?"
                                " [manuel/automatic]"))

if character_input == 'manuel':
    print("there are the following classes")
    for item in Class_list:
        print(item["name"])
    class_exinput = str(input("if you want an explanation of one of them, type: /explanation "
                              "(class you want an explanation about)."
                              "If you want an explanation on how to build them, just ask the same way, but instead of"
                              "/explanation use /details."))
    print("if you're ready to choose a class for your character, just press ENTER")
while class_exinput.startswith("/explanation" or "/details"):

    if class_exinput == '/explanation Barde':
        print(Class_list[0]["explanation"])
    elif class_exinput == '/explanation Barbarian':
        print(Class_list[1]["explanation"])
    elif class_exinput == '/explanation Rouge':
        print(Class_list[2]["explanation"])
    elif class_exinput == '/explanation Ranger':
        print(Class_list[3]["explanation"])
    elif class_exinput == '/explanation Cleric':
        print(Class_list[4]["explanation"])
    elif class_exinput == '/explanation Paladin':
        print(Class_list[5]["explanation"])
    elif class_exinput == '/explanation Wizard':
        print(Class_list[6]["explanation"])
    elif class_exinput == '/explanation Sorcerer':
        print(Class_list[7]["explanation"])
    elif class_exinput == '/explanation Warlock':
        print(Class_list[8]["explanation"])
    elif class_exinput == '/explanation Monk':
        print(Class_list[9]["explanation"])
    elif class_exinput == '/explanation Druid':
        print(Class_list[10]["explanation"])
    elif class_exinput == '/explanation Fighter':
        print(Class_list[11]["explanation"])
    elif class_exinput == '/details Barde':
        print(Class_list[0]["details"])
    elif class_exinput == '/details Barbarian':
        print(Class_list[1]["details"])
    elif class_exinput == '/details Rouge':
        print(Class_list[2]["details"])
    elif class_exinput == '/details Ranger':
        print(Class_list[3]["details"])
    elif class_exinput == '/details Cleric':
        print(Class_list[4]["details"])
    elif class_exinput == '/details Paladin':
        print(Class_list[5]["details"])
    elif class_exinput == '/details Wizard':
        print(Class_list[6]["details"])
    elif class_exinput == '/details Sorcerer':
        print(Class_list[7]["details"])
    elif class_exinput == '/details Warlock':
        print(Class_list[8]["details"])
    elif class_exinput == '/details Monk':
        print(Class_list[9]["details"])
    elif class_exinput == '/details Druid':
        print(Class_list[10]["details"])
    elif class_exinput == '/details Fighter':
        print(Class_list[11]["details"])
    class_exinput = str(input("If you want the explanation of another class, you can just ask the same way again"))

character_class_input = str(input("Now which class do you want "))
character_class_input = character_class_input.lower()

if (character_class_input == 'barde' or 'barbarian' or 'rouge' or 'ranger' or 'cleric' or 'paladin' or 'wizard' or
        'sorcerer' or 'warlock' or 'monk' or 'druid' or 'fighter'):
    player_character[0]["character-class"] = character_class_input


print("next you'll have to choose what race your character will be.")
print("there are the following")
for item in Races:
    print(item["name"])
Race_exinput = str(input("If you want an explanation to one of them do its the same as before with the classes,"
                         "but this time with the race you want an explanation to."))


while Race_exinput.startswith("/explanation" or "/details"):
    if Race_exinput == '/explanation Tiefling':
        print(Races[0]["explanation"])
    elif Race_exinput == '/explanation Dwarf':
        print(Races[1]["explanation"])
    elif Race_exinput == '/explanation Gnome':
        print(Races[2]["explanation"])
    elif Race_exinput == '/explanation Elf':
        print(Races[3]["explanation"])
    elif Race_exinput == '/explanation Half_Elf':
        print(Races[4]["explanation"])
    elif Race_exinput == '/explanation Halfling':
        print(Races[5]["explanation"])
    elif Race_exinput == '/explanation Half_Orc':
        print(Races[6]["explanation"])
    elif Race_exinput == '/explanation Human':
        print(Races[7]["explanation"])
    elif Race_exinput == '/explanation Dragonborn':
        print(Races[8]["explanation"])
    elif Race_exinput == '/details Tiefling':
        print(Races[0]["details" and "Attribute_Bonus"])
    elif Race_exinput == '/details Dwarf':
        print(Races[1]["details" and "Attribute_Bonus"])
    elif Race_exinput == '/details Gnome':
        print(Races[2]["details" and "Attribute_Bonus"])
    elif Race_exinput == '/details Elf':
        print(Races[3]["details" and "Attribute_Bonus"])
    elif Race_exinput == '/details Half_Elf':
        print(Races[4]["details" and "Attribute_Bonus"])
    elif Race_exinput == '/details Halfling':
        print(Races[5]["details" and "Attribute_Bonus"])
    elif Race_exinput == '/details Half_Orc':
        print(Races[6]["details" and "Attribute_Bonus"])
    elif Race_exinput == '/details Human':
        print(Races[7]["details" and "Attribute_Bonus"])
    elif Race_exinput == '/details Dragonborn':
        print(Races[8]["details" and "Attribute_Bonus"])
    Race_exinput = str(input("If you want the explanation of another class, you can just ask the same way again"))

character_race_input = str(input("Which race would you like your character to be ?"))
character_race_input = character_race_input.lower()

if character_race_input == 'tiefling' or "Tiefling":
    player_character[0]["character-race"] = "Tiefling"
    player_character[0]["charisma-attribute"] += 2
    player_character[0]["intelligence-attribute"] = 1
elif character_race_input == 'dwarf' or "Dwarf":
    player_character[0]["character-race"] = "Dwarf"
    player_character[0]["constitution-attribute"] += 2
    Dwarf_subrace_exinput = str(input("There are 3 types of dwarfs in D&D. The standard dwarf, the mountain dwarf "
                                    "and the hill dwarf. you can now ask for an explanation or the technical details,"
                                    " the same as before with the classes and races. So /explanation for an explanation"
                                    " and /details for the technical details of the hill/mountain dwarfs. And if you're ready to choose the subrace"
                                    ", just press ENTER."))
    Dwarf_subrace_exinput = Dwarf_subrace_exinput.lower()
    while Dwarf_subrace_exinput.startswith("/explanation" or "/details"):
        if Dwarf_subrace_exinput == '/explanation hill dwarf':
            print("Hill dwarfs are a subrace of dwarfs that ")
        if Dwarf_subrace_exinput == '/details hill dwarfs':
            print("Hill dwarfs have a +1 increase in your wisdom attribute")
        if Dwarf_subrace_exinput == '/explanation Mountain dwarfs':
            print("Mountain dwarfs are ......")
        if Dwarf_subrace_exinput == '/details mountain dwarfs' or "/details mountain dwarf":
            print("Mountain dwarfs have a +2 in your strength attribute.")
        Dwarf_subrace_exinput = str(input("if you need any other explanations or details, you can just aks again. "
                                    "And if you're done just press ENTER."))

    Dwarf_subrace_input = str(input("Now which dwarven subrace have you decided on ? "
                                "The regular-, hill- or mountain-dwarf ?"))
    Dwarf_subrace_input = Dwarf_subrace_input.lower()

    if Dwarf_subrace_input == "mountain dwarf":
        player_character[0]["strength-attribute"] += 2
        player_character[0]["character-race"] = "Moutnain dwarf"
    elif Dwarf_subrace_input == "hill dwarf":
        player_character[0]["character-race"] = "Hill dwarf"
        player_character[0]["wisdom-attribute"] += 1
    elif Dwarf_subrace_input == "regular dwarf" or "dwarf":
        player_character[0]["character-race"] = "Dwarf"


elif character_race_input == 'Gnome' or "gnome":
    player_character[0]["character-race"] = "Gnome"
    player_character[0]["intelligence-attribute"] += 2
    Gnome_subrace_exinput = str(input("There are 3 main types of gnomes in D&D. The standard gnome, the rock gnome and the "
                                      "forest gnome. You can now ask for an explanation or the technical details, the "
                                      "same way as before with the classes and races. So /explanation for an "
                                      "explanation or /details for the technical details of the rock/forest gnomes. And if you are ready to "
                                      "choose the subrace you want your character to be, just press ENTER"))
    Gnome_subrace_exinput = Gnome_subrace_exinput.lower()
    while Gnome_subrace_exinput.startswith("/explanation" or "/details"):
        if Gnome_subrace_exinput == '/explanation forest gnome' or '/explanation forest gnomes' :
            print("forest gnomes are a subrace of gnomes that live, as the name suggests, in forests. They are the "
                  "smallest subrace of gnomes.")
        elif Gnome_subrace_exinput == "/explanation rock gnome" or "/explanation rock gnomes":
            print("Rock gnomes are the subrace of gnomes, that is the most common. ")
        elif Gnome_subrace_exinput == "/details forest gnome" or "/details forest gnomes":
            print("Forest gnomes have a +1 increase in your dexterity attribute")
        elif Gnome_subrace_exinput == "/details rock gnomes" or "/details rock gnome":
            print("Rock gnomes have a +1 increase in your constitution attribute.")
        Gnome_subrace_exinput = str(input("If you need any other explanations or details, you can just ask again."
                                          "And if you are done just press ENTER."))

    Gnome_subrace_input = str(input("Now which gnome subrace have you decided on ?"
                                "The regular-, forest- or rock-gnome ?"))
    Gnome_subrace_input = Gnome_subrace_input.lower()

    if Gnome_subrace_input == "regular-gnome" or "regular gnome" or "gnome":
        player_character[0]["character-race"] = "Gnome"
    elif Gnome_subrace_input == "rock-gnome" or "rock gnome":
        player_character[0]["constitution-attribute"] += 1
        player_character[0]["character-race"] = "Rock Gnome"
    elif Gnome_subrace_input == "forest-gnome" or "forest gnome":
        player_character[0]["dexterity-attribute"] += 1
        player_character[0]["character-race"] = "Forest Gnome"


elif character_race_input == "Elf" or "elf":
    player_character



for character in player_character:
    for key, value in character.items():
        print(key + ":", value)
    print()
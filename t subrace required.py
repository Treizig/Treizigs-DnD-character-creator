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
    character_input = str(input("Would you like to create a character manually or automatically generate one ?"
                                " [manually/automatically]"))

if character_input == 'manually':
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
Race_exinput = Race_exinput.lower()
Race_exinput = Race_exinput.replace('-', ' ').replace('_', ' ')

while Race_exinput.startswith("/explanation" or "/details" or 'explanation' or 'details'):
    if Race_exinput == '/explanation tiefling' or 'explanation tiefling':
        print(Races[0]["Explanation"])
    elif Race_exinput == '/explanation dwarf' or 'explanation dwarf':
        print(Races[1]["Explanation"])
    elif Race_exinput == '/explanation gnome' or 'explanation gnome':
        print(Races[2]["Explanation"])
    elif Race_exinput == '/explanation elf' or 'explanation elf':
        print(Races[3]["Explanation"])
    elif Race_exinput == 'explanation half elf' or '/explanation half elf':
        print(Races[4]["Explanation"])
    elif Race_exinput == '/explanation halfling' or 'explanation halfling':
        print(Races[5]["Explanation"])
    elif Race_exinput == '/explanation half orc' or 'explanation half orc':
        print(Races[6]["Explanation"])
    elif Race_exinput == '/explanation human' or 'explanation human':
        print(Races[7]["Explanation"])
    elif Race_exinput == '/explanation dragonborn' or 'explanation dragonborn':
        print(Races[8]["Explanation"])
    elif Race_exinput == '/details tiefling' or 'details tiefling':
        print(Races[0]["Attribute_Bonus"])
    elif Race_exinput == '/details dwarf' or 'details dwarf':
        print(Races[1][ "Attribute_Bonus"])
    elif Race_exinput == '/details gnome' or ' details gnome':
        print(Races[2][ "Attribute_Bonus"])
    elif Race_exinput == '/details elf' or 'details elf':
        print(Races[3][ "Attribute_Bonus"])
    elif Race_exinput == '/details half elf' or 'details half elf':
        print(Races[4][ "Attribute_Bonus"])
    elif Race_exinput == '/details halfling' or 'details halfling':
        print(Races[5][ "Attribute_Bonus"])
    elif Race_exinput == '/details half orc' or 'details half orc':
        print(Races[6][ "Attribute_Bonus"])
    elif Race_exinput == '/details human' or 'details human':
        print(Races[7][ "Attribute_Bonus"])
    elif Race_exinput == '/details dragonborn' or 'details dragonborn':
        print(Races[8][ "Attribute_Bonus"])
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
    Dwarf_subrace_exinput = str(input("There are 2 main types of dwarfs in D&D. The mountain dwarf and the hill dwarf."
                                      " You can now ask for an explanation or the technical details, the same as before"
                                      " with the classes and races. So /explanation for an explanation and /details for"
                                      " the technical details of the hill/mountain dwarfs. And if you're ready to "
                                      "choose the subrace, just press ENTER."))
    Dwarf_subrace_exinput = Dwarf_subrace_exinput.lower()

    while Dwarf_subrace_exinput.startswith("/explanation" or "/details"):
        if Dwarf_subrace_exinput == '/explanation hill dwarf':
            print("Hill dwarfs are a subrace of dwarfs that ")
        elif Dwarf_subrace_exinput == '/details hill dwarfs':
            print("Hill dwarfs have a +1 increase in your wisdom attribute")
        elif Dwarf_subrace_exinput == '/explanation Mountain dwarfs':
            print("Mountain dwarfs are ......")
        elif Dwarf_subrace_exinput == '/details mountain dwarfs' or "/details mountain dwarf":
            print("Mountain dwarfs have a +2 in your strength attribute.")
        Dwarf_subrace_exinput = str(input("if you need any other explanations or details, you can just aks again. "
                                    "And if you're done just press ENTER."))

    Dwarf_subrace_input = str(input("Now which dwarven subrace have you decided on? The hill- or the mountain-dwarf?"))
    Dwarf_subrace_input = Dwarf_subrace_input.lower()

    if Dwarf_subrace_input == "mountain dwarf":
        player_character[0]["strength-attribute"] += 2
        player_character[0]["character-race"] = "Moutnain dwarf"
    elif Dwarf_subrace_input == "hill dwarf":
        player_character[0]["character-race"] = "Hill dwarf"
        player_character[0]["wisdom-attribute"] += 1


elif character_race_input == 'Gnome' or "gnome":
    player_character[0]["character-race"] = "Gnome"
    player_character[0]["intelligence-attribute"] += 2
    Gnome_subrace_exinput = str(input("There are 2 main types of gnomes in D&D. The rock gnome and the forest gnome. "
                                      "You can now ask for an explanation or the technical details, the "
                                      "same way as before with the classes and races. So /explanation for an "
                                      "explanation or /details for the technical details of the rock/forest gnomes."
                                      " And if you are ready to choose the subrace you want your character to be, "
                                      "just press ENTER"))
    Gnome_subrace_exinput = Gnome_subrace_exinput.lower()
    while Gnome_subrace_exinput.startswith("/explanation" or "/details"):
        if Gnome_subrace_exinput == '/explanation forest gnome' or '/explanation forest gnomes':
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

    Gnome_subrace_input = str(input("Now which gnome subrace have you decided on ? The forest- or rock-gnome ?"))

    Gnome_subrace_input = Gnome_subrace_input.lower()

    if Gnome_subrace_input == "rock-gnome" or "rock gnome":
        player_character[0]["constitution-attribute"] += 1
        player_character[0]["character-race"] = "Rock Gnome"
    elif Gnome_subrace_input == "forest-gnome" or "forest gnome":
        player_character[0]["dexterity-attribute"] += 1
        player_character[0]["character-race"] = "Forest Gnome"


elif character_race_input == "Elf" or "elf":
    player_character[0]["character-race"] = "Elf"
    player_character[0]["dexterity-attribute"] += 2
    Elf_subrace_exinput = str(input("Elves are the race with the most subclasses, but im just gonna mention 2 of them "
                                    "here. There are the wood- and the high- elves. These two are the most common "
                                    "elves. Now you can ask for an explanation or the technical details, the "
                                    "same way as before with the classes and races. So /explanation for an "
                                    "explanation or /details for the technical details of the rock/forest gnomes."
                                    " And if you are ready to choose the subrace you want your character to be, "
                                    "just press ENTER"))
    Elf_subrace_exinput = Elf_subrace_exinput.lower()
    Elf_subrace_exinput = Elf_subrace_exinput.replace('-', ' ').replace('_', ' ')
    if Elf_subrace_exinput.startswith("explanation"):
        Elf_subrace_exinput = "/" + Elf_subrace_exinput
    if Elf_subrace_exinput.startswith("details"):
        Elf_subrace_exinput = "/" + Elf_subrace_exinput

    while Elf_subrace_exinput.startswith("/explanation" or "/details"):
        if Elf_subrace_exinput == '/explanation high elf' or '/explanation high elves':
            print("High elves aren't necessarily more common than wood elves, but the likelihood of encountering one"
                  " is much higher since they more often live in cities, towns, and villages as opposed to wood elves."
                  "Its not unusual to find a high elf within the higher ranks of a city.")
        elif (Elf_subrace_exinput == '/explanation wood elves' or '/explanation wood-elves' or '/explanation wood-elf'
              or '/explanation wood elf'):
            print("Wood elves are attuned to nature, often dwelling in secluded woodlands and forests and are therefore"
                  " exceptionally skilled in archery wilderness survival. You can often find them protecting the nature"
                  " of the forgotten realms similar to some druid exclaves.")
        elif (Elf_subrace_exinput == '/details high elf' or '/details high-elf' or '/details high elves' or
              '/details high-elves'):
            print("High elves have a +1 increase in your intelligence-atribute.")
        elif (Elf_subrace_exinput == '/details wood elves' or '/details wood-elves' or '/details wood elf'
              or '/details wood-elf'):
            print("Wood elves have a +1 increae in your wisdom attribute.")


for character in player_character:
    for key, value in character.items():
        print(key + ":", value)
    print()

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

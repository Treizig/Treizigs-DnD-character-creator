races = ["tiefling","dwarf","gnome","elf","half_elf","half_orc","human","dragonborn"]

while Race_exinput.startswith("/explanation" or "/details"):
    if Race_exinput.startswith("/explanation"):
        for race in range(len(races)):
            if Race_exinput.replace("/explanation", "").strip().lower() == races[race].strip().lower():
                print(Races[race]["explanation"])
    elif Race_exinput.startswith("/details")
        for race in range(len(races)):
            if Race_exinput.replace("/explanation", "").strip().lower() == races[race].strip().lower():
                print(Races[race]["details" and "Attribute_Bonus"]):
    Race_exinput = str(input("If you want the explanation of another race, you can just ask the same way again"))

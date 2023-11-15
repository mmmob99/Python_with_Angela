with open("./Input/Names/invited_names.txt", "r") as name:
    name_list = []
    for i in name:
        i = i.strip("\n")
        name_list.append(i)
    for invite_name in name_list:
        with open(f"./Output/ReadyToSend/{invite_name}.txt", "w") as invite_latter:
            with open("./Input/Letters/starting_letter.txt", "r") as letter:
                letter = letter.read()
                invite_latter.write(letter.replace("[name]", f"{invite_name}"))


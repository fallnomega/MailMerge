# get list of names
names = []
with open("Input/Names/invited_names.txt") as file:
    names = file.read().splitlines()
with open("Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
for x in names:
    temp_content = content
    temp_content = temp_content.replace("[name]", x)
    new_letter = open(f"Output/ReadyToSend/{x}.txt", "w")
    new_letter.write(temp_content)
    new_letter.close()

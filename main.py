#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


with open("Input/Names/invited_names.txt") as file:
    contents = file.read()
    names = contents.splitlines()

with open("Input/Letters/starting_letter.txt") as file:
    contents = file.read()
    letter_text = contents

for name in names:
    new_letter_text = letter_text.replace("[name]", name)
    with open("Output/ReadyToSend/"+name+".txt", 'w') as file:
        file.write(new_letter_text)
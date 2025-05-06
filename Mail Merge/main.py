#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# required files are in contrived folders to practice indexing using relative filepaths

# Mail Merge
#     Input
#         Letters
#             starting_letter.txt
#         Names
#             invited_names.txt
#     Output
#         ReadyToSend
#         main.py

PLACEHOLDER = "[names]" # the string that will be replaced

# for each name in invited_names.txt store the names in a list using readlines()
with open("./Input/Names/invited_names.txt") as names_file:
    name_list = names_file.readlines() # names currently has "\n"

# create a letter using starting_letter.docx
with open("./Input/Letters/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read() # letter contents read as a string

    # find and replace placeholder with names in name_list
    for name in name_list:
        stripped_name = name.strip() # removes "\n" from the names
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name) # replace("old_text", "new_text")

        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter: # dynamically creates new file
            completed_letter.write(new_letter) # writes the new_letter to the new file

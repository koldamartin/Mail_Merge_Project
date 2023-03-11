#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(".\\Input\\Letters\\starting_letter.txt", "r") as original_file:
    content = original_file.read()

with open(".\\Input\\Names\\invited_names.txt", "r") as replacement_file:
    names = replacement_file.readlines() #creates a list of names
    for name in names:
        replacement_word = name.strip() #strip new lines for each name
        with open(f".\\Output\\ReadyToSend\\letter_for_{replacement_word}", "w") as updated_file:
            updated_content = content.replace("[name]", replacement_word) #replace [name] with one from the list
            updated_file.write(updated_content) #write the updated content inside the newlz created file

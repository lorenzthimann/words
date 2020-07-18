# This is a new mix word
essayes_original = []
# ask for the word and an essaye
essayes = []
word_original = input("Please give me the original word we are going to work on: ")
word = word_original
while True:
    error = False
    essaye_original = input('By mixing the letters and adding characters like ",", "apostropher", "1", "2","3", "4", "5", "6", "7", "8", " ", "9", "0", ".", "-", try to find a new word that makes sense: ')
    essaye = essaye_original
    # remove nb in words, and spaces...
    mot_channge = word
    no_matter_characters = (",", "'", "1", "2","3", "4", "5", "6", "7", "8", " ", "9", "0", ".", "-", " ")
    for letter in essaye:
        if letter in no_matter_characters:
            essaye = essaye.replace(letter, "")
    for letter in word:
        if letter in no_matter_characters:
            mot_channge = mot_channge.replace(letter, "")
        for letter in mot_channge:
            if letter in no_matter_characters:
                mot_channge = word.replace(letter, "")
        # check if all letters in word are in the test and if there are no other letters
    if len(mot_channge) != len(essaye):
        print("Check the mixed word. The length of the original word and the new word are not the same.")
        error = True
    else:
        for letter in essaye:
            if letter not in word:
                print(f"We found the letter {letter} that is not in the word. Please double check it.")
                error = True
    # check if essaye is already in essayes
    if essaye_original in essayes_original:
        error = True
        print("Search a bit more to find something else, 'cause this word/ sentence is already in the list of tried items.")
    #print all the essayes
   
    if not error:
        essayes_original.append(essaye_original)
        essayes.append(essaye)
    if len(essayes) > 0:
        print("Here are all the words you found:")
        for i in essayes_original:
            print(f"--> {i}")
    print(f"mot channge = {mot_channge}, essaye = {essaye}.")
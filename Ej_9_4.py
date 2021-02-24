def longest_word_per_character(text):
    """Function that receives a text, and for each character in that string, it returns the longest
    string where that character is present."""

    text = text.lower()
    character_dictionary = {}
    word_list = []
    aux_word = ''
    valid_characters = "'abcdefghijklmnopqrstuvwxyz"

    for i in text:
        if i in valid_characters:
            character_dictionary[i] = ''
        if i == ' ' or i == '.' or i == ',':
            word_list.append(aux_word)
            aux_word = ''
        else:
            aux_word = aux_word + i
    word_list.sort(key = len, reverse = True)

    for i in character_dictionary:
        for j in word_list:
            for k in range(len(j)):
                if i == j[k] and character_dictionary[i] == '':
                    character_dictionary[i] = j
            
    return character_dictionary, word_list
    
text = "Sometimes we must go half out of our way just to appreciate the beauty in the journey."
e, d = longest_word_per_character(text)
print(e)
print('')
print(d)
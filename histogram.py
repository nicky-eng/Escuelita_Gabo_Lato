def histogram(string):
    """
    Returns a dictionary with a histogram of the corresponding string.

            Parameters:
                    string (str): The string that will be histogramed.
            
            Returns:
                    histo (dict): A dictionary with all the charaters.
    """

    histo = dict()
    for character in string:
        histo[character] = histo.get(character, 0) + 1
    
    return histo


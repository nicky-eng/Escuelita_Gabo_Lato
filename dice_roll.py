def dice_roll(rolls, dice):
    """Using random, it creates a number of dice rolls equal to <rolls> with <dice> amount of dice each, saves them in
    tuples and returns them in a list."""
    
    import random

    total_rolls = []
    aux_roll = ()
    for i in range(rolls):
        aux_roll = ()
        for j in range (dice): #A for loop is used instead of random.sample, to allow for repeated numbers.
            aux_roll = aux_roll + tuple((random.randint(1,6),))
        total_rolls.append(aux_roll)
    
    return total_rolls

#print(dice_roll(6, 3))
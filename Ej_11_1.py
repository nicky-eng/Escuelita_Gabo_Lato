def head(file, n):
    """
    Function that reads the first n lines in a file.
        Parameters:
            file - file to read
            n - number of lines to read
        
        Outputs:
            Prints the read lines
    """
    import os
    dirname = os.path.dirname(__file__)
    filename = file

    with open(os.path.join(dirname, filename), "r") as f:
        for i in range(n):
            print(f.readlines(), end="")
    

text = "My file.txt"
n = 3
head (text, n)
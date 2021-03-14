def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I am happy, that's how I am.")
    print("I am happy so give me more sun.")

repeat_lyrics()


import histogram
d = histogram.histogram('Alberquque')
r = 2

#print (d)

def reverse_lookup(d, r):
    for k in d:
        if d[k] == r:
            return k
    raise LookupError

#print(reverse_lookup(d, r))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
#print(fibonacci(39))


known = {0:0, 1:1}
def fibonacciknown(n):
    if n in known:
        return known[n]
    res = fibonacciknown(n-1) + fibonacciknown(n-2)
    known[n] = res
    return res

print(fibonacciknown(39))

def spin_words(sentence):
    a = sentence.split()
    b = ""
    for a in a:
        if(len(a) >= 5):
            a = a[::-1]
        if(b):
            b += " "+a
        else:
            b   += a

    return b
print(spin_words("this is amazing"))
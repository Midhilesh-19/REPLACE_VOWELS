
def translate(phrase):
    trans = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                trans = trans + "V*"    #REPLACING VOWEL WITH PARICULAR WORD
            else:
                trans = trans + "v*"  # WHERE V* & v* = VOWEL
        else:
            trans = trans + letter
    return trans

print(translate(input("Enter a phrase:")))                
      
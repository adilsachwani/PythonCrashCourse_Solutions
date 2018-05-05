favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }

for name,languages in favorite_languages.items():
    print(name.title() + "'s favourite language", end="")

    if len(languages)>1:
        print("s are ", end="")
    else:
        print(" is ", end="")

    for i,language in enumerate(languages) :
        if(i == len(languages)-1):
            print(language.title() + ".", end="")
        else:
            print(language.title() + ", ", end="")

    print("")
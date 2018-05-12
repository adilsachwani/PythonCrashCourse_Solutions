def count_book(file,word):

    try:
        with open(file) as book:
            contents = book.read()
    except:
        pass
    else:
        count = contents.lower().count(word)
        print("Book has " + str(count) + " times " + word.upper())

count_book('michelangelo.txt','the')
count_book('adil.txt','the')
count_book('fairytales.txt','the')
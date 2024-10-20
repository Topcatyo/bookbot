def main():
    # user chooses book from directory
    input = "frankenstein"
    chosen_book = f"books/{input}.txt"

    # book  text is printed
    text = get_book(chosen_book)

    #get word count
    word_count = get_word_count(text)
    
    #print assignment junk
    #print(text)
    print(word_count)


def get_book(chosen_book):
    with open(chosen_book) as b:
        book = b.read()
        return book

def get_word_count(book):
    text = book
    words = text.split()
    return len(words)

def get_character_counts(words):
    
    #!!!!!!!!!   TO DO LIST   !!!!!!!!!
    #0. Convert entire book to lowercase
    #1. Create dictionary of each letter
    #2. For a for loop on each character with a comparison that adds to a counter
    #3. Return each counter
    #4. Prettify all the outputs, even the commented out ones

main()
def main():
    # user chooses book from directory if interactive
    book_title = "Frankenstein"
    chosen_book = f"books/{book_title}.txt"


    # book  text is printed
    text = get_book(chosen_book)

    #-------- ASSIGNMENTS -------
    #get word count
    word_count = get_word_count(text)[0]
    #get character counts
    letter_count = get_character_counts(text)
    
    #print assignment junk
    print(f"This is the story {book_title}")
    print("Some stats:")
    print(f"This book has {word_count} words.")
    print("Here is every instance of every letter in the book:")
    print(format_letter_counts(letter_count))
    print("Anyways, here's the book!")
    #print(text)


def get_book(chosen_book):
    with open(chosen_book) as b:
        book = b.read()
        return book


def get_word_count(book):
    text = book
    indiv_words = text.split()
    return len(indiv_words), indiv_words


def get_character_counts(book):
    unsorted = {}
    letters = {}

    for char in book.lower():
        if char.isalpha():
            unsorted[char] = unsorted.get(char, 0) +1

    letters = dict(sorted(unsorted.items()))
    return letters

def format_letter_counts(letter_count, letters_per_line=7):
    result = []
    header = "Letter: Count  "
    result.append((header).rstrip())
    result.append("-" * (len(header) * letters_per_line))
    
    for i, (letter, count) in enumerate(letter_count.items(), 1):
        result.append(f"{letter.upper()}: {count:6}")
        if i % letters_per_line == 0:
            result.append("\n")
        elif i < len(letter_count):
            result.append("  |  ")
    
    return "".join(result)


main()
def main():
    # user chooses book from directory if interactive
    book_title = "Frankenstein by Mary Shelley"
    chosen_book = f"books/{book_title}.txt"

    # book  text is printed
    text = get_book(chosen_book)

    #-------- ASSIGNMENTS -------
    #get word count
    word_count = get_word_count(text)[0]
    #get character counts
    letter_count, formatted_letter_count = count_letters(text)
    
    #print assignment junk
    print(f"You have chosen the book {book_title}")
    print("But first, some statistics!")
    print(f"This book has {word_count} words.")
    print("Here is every instance of every letter in the book:")
    print(formatted_letter_count)
    print("Anyways, here's the book!")
    #print(text)


###########################################


def get_book(chosen_book):
    with open(chosen_book) as b:
        book = b.read()
        return book


def get_word_count(book):
    text = book
    indiv_words = text.split()
    return len(indiv_words), indiv_words


import string

def count_letters(text):
    def format_letter_counts(letter_count, letters_per_line=7):
        result = []
        item_width = 10  # Width for each "LETTER: COUNT" item
        total_width = (item_width + 2) * letters_per_line  # +2 for the "  |  " separator

        result.append("-" * total_width)  # Just the hyphen line
        
        line = []
        for i, (letter, count) in enumerate(sorted(letter_count.items()), 1):
            line.append(f"{letter.upper()}: {count:6}")
            if i % letters_per_line == 0:
                result.append("  |  ".join(line))
                line = []
        
        if line:  # Add any remaining items
            result.append("  |  ".join(line))
        
        return "\n".join(result)

    # Initialize a dictionary with all lowercase letters set to 0
    letter_counts = {letter: 0 for letter in string.ascii_lowercase}
    
    # Count the letters in the text
    for char in text.lower():
        if char.isalpha():
            letter_counts[char] += 1
    
    # Format the letter counts
    formatted_counts = format_letter_counts(letter_counts)
    
    return letter_counts, formatted_counts


main()
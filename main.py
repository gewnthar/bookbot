#defining main function to be called later
def main():
    #make the path available to use by creating a variable
    book_path = "books/frankenstein.txt"
    # assign a new variable to store the text whiole we call the function from below
    text = get_book_text(book_path)
    #this prints the entire text of frankenstein in the terminal
    #print(text)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def get_num_words(text):
    #split the book into words with the split method. this uses whitespace as the seperator
    words = text.split()
    #using return we can then do one last method on the now split words
    return len(words)

# the variable path here is created and will inherit book_path when it is called in the main function
def get_book_text(path):
    # with was in a tip from boot.dev to make sure that the memory gets freed after the with statement
    with open(path) as f:
        return f.read()


# calling main function many places insist on usintg the __name__ thing not sure what thats about.
main()
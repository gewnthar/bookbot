#defining main function to be called later
def main():
    #make the path available to use by creating a variable
    book_path = "books/frankenstein.txt"
    # assign a new variable to store the text whiole we call the function from below
    text = get_book_text(book_path)
    #this prints the entire text of frankenstein in the terminal
    #print(text)
    #call get_num_words
    num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    
    #call count_characters
    char_count = count_characters(text)
    print(f"Character counts!:{char_count}")
    print_report(char_count, num_words)


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

#back to the old text call again old hat by now
def count_characters(text):
    #only wanted lower characters so making them all lower
    text = text.lower()
    #make a dictionary as called for in the instructions
    char_count = {}
    #use char to iterate over everything in text
    for char in text:
        #check the text to see if the character exists if it does add 1
        if char in char_count:
            char_count[char] += 1
        #if it doesn't exist in the dictionary its the first time its being put in so count 1
        else:
            char_count[char] = 1
    return char_count
        

def sort_on(dict):
    return dict["num"]

def print_report(char_count, num_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    
    char_list = [
        {"char": char, "num": count}
        for char, count in char_count.items() if char.isalpha()]
    char_list.sort(key=sort_on, reverse=True)

    for char, count in char_count.items():
        if char.isalpha():
            char_dict = {"char": char, "num": count}
            char_list.append(char_dict)
    
    char_list.sort(key=sort_on, reverse=True)
    
    # Now loop through the sorted list and print each line
    for char_dict in char_list:
        print(f"The {char_dict['char']} character was found {char_dict['num']} times")
    print("--- End report ---")
# calling main function many places insist on usintg the __name__ thing not sure what thats about.
main()
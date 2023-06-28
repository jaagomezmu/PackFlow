# Example of Lookup Table - Category Assignment

category_lookup = {
    'fruit': ['apple', 'pear', 'banana', 'orange'],
    'animal': ['dog', 'cat', 'elephant', 'giraffe'],
    'color': ['red', 'blue', 'green', 'yellow']
}

def lookup_category(word):
    for category, words in category_lookup.items():
        if word in words:
            return category
    return 'Category not found'


if __name__ == '__main__':
    user_word = input("Enter a word: ")

    category = lookup_category(user_word)
    print(f"The category of '{user_word}' is: {category}")

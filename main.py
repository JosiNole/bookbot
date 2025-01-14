
def track(text):
    words = text.split()
    return len(words)

def specific_count(file_contents):
    character_count = {}
    for character in file_contents:
        character = character.lower()
        if not character.isalpha():
            continue
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = track(file_contents)
    character_count = specific_count(file_contents)
    
    sorting(word_count, character_count)
    return character_count

def sorting(word_count, character_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print("{} words found in the document\n".format(word_count))

    sorted_characters = sorted(character_count.items(), key=lambda item: item[1], reverse=True)
    for letter, count in sorted_characters:
        print("The '{}' character was found {} times".format(letter, count))
    print("----THE END----")
result = main()

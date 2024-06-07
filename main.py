def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)

    lowered_case  = file_contents.lower()
    characters = {}
    for char in lowered_case:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    letter_list = []

    def sort_on(dict):
        return dict["num"]

    for char, count in characters.items():
        char_dict = {"char": char, "num": count}
        letter_list.append(char_dict)
    letter_list.sort(reverse=True, key=sort_on)

    print("-- Report of Book: frankenstein.txt")
    print(word_count, " words found")
    for dic in letter_list:
        print("The ", dic["char"], " was found ", dic["num"], " times")   
main()


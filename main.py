def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print_report(count_characters(file_contents), count_words(file_contents))    
   

def count_words(text):
    return len(text.split())

def count_characters(text):
    charsMap = {}
    for char in text:
        l_char = char.lower()
        if l_char >= 'a' and l_char <= 'z':
            if l_char not in charsMap:
                charsMap[l_char] = 1
            else:
                charsMap[l_char] += 1
    sortedChars  = sorted(charsMap.items(), key=lambda x:x[1], reverse=True)
    return dict(sortedChars)

def print_report(charsMap, words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} found in the document")
    print()
    for char in charsMap:
        print(f"The '{char}' character was found {charsMap[char]} times") 
    print("--- End Report ---")
main()
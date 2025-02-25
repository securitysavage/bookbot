def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents) <- only needed by the insane
        word_count = wordcount(file_contents)
        char_count = charcount(file_contents)
        dict_sort = dictsort(char_count)
        
        # report header with word count
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        
        # print char count
        for entry in dict_sort:
            print(f"The '{entry['char']}' character was found {entry['num']} times")

        # report footer
        print(f"--- End report ---")

def wordcount(file_contents):
    file_contents = file_contents.split()
    return len(file_contents)

def charcount(file_contents):
    count = {}
    text = file_contents.lower()
    for char in text:
        if not char.isalpha():
            continue
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    return count

def dictsort(count):
    dict_list = [{"char": char, "num": num} for char, num in count.items()]
    dict_list.sort(key=lambda x: x["num"], reverse = True)
    return dict_list


main()

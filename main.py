import sys
from stats import count_words, count_characters, report_data

def get_book_text(filename):
    with open(filename) as f:
        file_contents = f.read()
    return file_contents


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        pass

    book = sys.argv[1]

    file = get_book_text(book)

    count = str(count_words(file))

    countdict = count_characters(file)

    data = report_data(countdict)

    

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book)

    print("----------- Word Count ----------")
    print("Found " + count + " total words")

    print("--------- Character Count -------")

    for num in data: 
        if num["character"].isalpha() == True:
            print(num["character"] + ": " + str(num["count"]))
        else:
            pass
        #str.isalpha()
    #print(countdict)


main()

from stats import count_words, count_characters, report_data

def get_book_text(filename):
    with open(filename) as f:
        file_contents = f.read()
    return file_contents


def main():
    file = get_book_text("books/frankenstein.txt")

    count = str(count_words(file))

    countdict = count_characters(file)

    data = report_data(countdict)
    
    print(count + " words found in the document")

    print(data)

    #print(countdict)


main()
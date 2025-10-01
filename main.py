import sys
from stats import get_num_words
from stats import get_num_char
from stats import dict_chars_count

#function to take a filepath as input and return the contents of file as string
def get_book_text(filepath):
        #open the file and read its contents 
        with open(filepath) as f:
            file_contents = f.read() 
        return file_contents 




def main():

    if len(sys.argv) < 2:
            print ("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
            
        #Call the function and store the book text in a variable
    bt = get_book_text(sys.argv[1]) 
    wm = get_num_words(bt)
    cc = get_num_char(bt)
    pt = dict_chars_count(bt)
    filepath = sys.argv[1]


    print("============ BOOKBOT ============")
    print("Analyzing book found at", filepath, "...")
    print("----------- Word Count ----------")
    print("Found",wm,"total words")
    print("--------- Character Count -------")
    for char, count in pt:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__": 
    main()

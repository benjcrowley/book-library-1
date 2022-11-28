### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

def add_local_books(lib):
    for i in range(len(lib)):
        # for item in lib[i].items():
        #     print(item)
        title = lib[i]["title"]
        author = lib[i]["author"]
        year = lib[i]["year"]
        rating = lib[i]["rating"]
        pages = lib[i]["pages"]
        f = open("/Users/bennettcrowley/Desktop/devMountain/dev_python/1-unit-setup/book-library-1/library.txt", "a")
        f.write(f'{title}, {author}, {year}, {rating}, {pages}\n')



def add_new_book():
    title = input("What is the title of your book? ")
    author = input("Who wrote your book? ")
    try:
        year = int(input("what year did your book get published? "))
    except:
        year = int(input("Please enter a year for the date"))
    try:
        rating = float(input("What is your books rating out of 5? "))
    except:
        rating = float(input("Please enter a valid rating "))
    try:
        pages = int(input("How many pages in your book? "))
    except:
        pages = int(input("Please enter a number for the # of pages "))
    f = open("/Users/bennettcrowley/Desktop/devMountain/dev_python/1-unit-setup/book-library-1/library.txt", "a")
    f.write(f'{title}, {author}, {year}, {rating}, {pages}')
    f.close()
    book_dictionary = {
            'title': title,
            'author': author,
            'year': int(year),
            'rating': float(rating),
            'pages': int(pages),
        }
    local_library.append(book_dictionary)

### Step 2 - Read data from a .txt
local_library = []
def download_local():
    f = open("/Users/bennettcrowley/Desktop/devMountain/dev_python/1-unit-setup/book-library-1/library.txt", "r")
    file = f.readlines()

    for line in file:
        title, author, year, rating, pages = line.split(', ')
        book_dictionary = {
            'title': title,
            'author': author,
            'year': int(year),
            'rating': float(rating),
            'pages': int(pages),
        }
        local_library.append(book_dictionary)



## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def see_all_books():
    f = open("/Users/bennettcrowley/Desktop/devMountain/dev_python/1-unit-setup/book-library-1/library.txt", "r")

    file = f.readlines()

    for line in file:
        title, author, year, rating, pages = line.split(', ')
        book_dictionary = {
            'title': title,
            'author': author,
            'year': int(year),
            'rating': float(rating),
            'pages': int(pages),
        }
        print(f'{title}, by {author}: {rating}/5')

def search_by_title():
    title = input("name of book: ")
    for i in range(len(local_library)):
        if local_library[i]["title"] == title:
            return f'{local_library[i]["title"]}, written by {local_library[i]["author"]} in {local_library[i]["year"]} is rated {local_library[i]["rating"]}/5 and is {local_library[i]["pages"]} pages long; It would take me (Bennett) about {int(local_library[i]["pages"] * 2.3 / 60)} hours to read.'
    

def best_rated_book():
    best_book = "yeet"
    highest_rating = 0
    for i in range(len(local_library)):
        if local_library[i]["rating"] > highest_rating:
            highest_rating = local_library[i]["rating"]
            best_book = local_library[i]["title"]
    return f"{best_book}, rating: {highest_rating}"

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

def main_menu():
    n = None
    while n != 5:
        n = int(input("Main Menu: \n 1. Add new book \n 2. See all books\n 3. Search by Title \n 4. Best Rated Book \n 5. Quit Program \n "))
        if n == 1:
            add_new_book()
        elif n == 2:
            see_all_books()
        elif n == 3:
            print(search_by_title())
        elif n == 4:
            print(best_rated_book())

if __name__ == '__main__':
    download_local()
    main_menu()


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!


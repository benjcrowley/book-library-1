my_library = [
    {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
},
{
    "title": "The Mocking Jay",
    "author": "Suzanne Collins",
    "year": 2010,
    "rating": 4.425,
    "pages": 370
},
{
    "title": "Capitan Underpants",
    "author": "Dav Pilkey",
    "year": 1997,
    "rating": 5.0,
    "pages": 125
},
{
    "title": "Capitan Underpants",
    "author": "Dav Pilkey",
    "year": 1997,
    "rating": 5.0,
    "pages": 125
}]
### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
def input_book_info():
    title = input("What is the title of your book? ")
    author = input("Who wrote your book? ")
    year = input("what year did your book get published? ")
    rating = input("What is your books rating out of 5? ")
    pages = input("How many pages in your book? ")
    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    return new_book

# print(input_book_info())
### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def enter_book_info():
#     title = input("What is the title of your book? ")
#     author = input("Who wrote your book? ")
#     year = int(input("what year did your book get published? "))
#     rating = float(input("What is your books rating out of 5? "))
#     pages = int(input("How many pages in your book? "))
#     new_book = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }
#     return new_book

# my_book = enter_book_info()
# print(type(my_book["year"]))
# print(type(my_book["title"]))
# print(type(my_book["pages"]))
# print(type(my_book["rating"]))
### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
def enter_book_info():
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

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }
    return new_book

# my_book = enter_book_info()
# print(type(my_book["year"]))
# print(type(my_book["title"]))
# print(type(my_book["pages"]))
# print(type(my_book["rating"]))
# print(my_book)

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
def main_menu():
    n = None
    while n != 4:
        n = int(input("Main Menu: \n 1. Add new book \n 2. See all books\n 3. Search by Title \n 4. Quit Program \n "))
        if n == 1:
            my_library.append(enter_book_info())
        elif n == 2:
            print(my_library)
        elif n == 3:
            print('Function not available')

main_menu()
### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here


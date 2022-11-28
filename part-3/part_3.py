import statistics
my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}
your_book = {
    "title": "The Mocking Jay",
    "author": "Suzanne Collins",
    "year": 2010,
    "rating": 4.425,
    "pages": 370
}
their_book = {
    "title": "Capitan Underpants",
    "author": "Dav Pilkey",
    "year": 1997,
    "rating": 5.0,
    "pages": 125
}
book_list = [my_book, your_book, their_book]
book_list_2 = [
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

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def get_all(book):
    '''pass in a dictionary, and return the title, author, year, rating, and number of pages'''
    return f'This {book["pages"]} page book, titled {book["title"]}, by {book["author"]} in {book["year"]} is rated {book["rating"]}/5'

# print(get_all(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def get_title(book):
    return book["title"]

def get_author(book):
    return book["author"]

def get_year(book):
    return book["year"]

def get_rating(book):
    return book["rating"]

def get_pages(book):
    return book["pages"]

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps think of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def most_published_author(lst):
    author_list = []
    res_str = ''
    for i in range(len(lst)):
        author_list.append(lst[i]["author"])
        # print(author_list)
    res = statistics.multimode(author_list)
    if len(res) == 1:
        return f'The most published author in this library is {res[0]}.'
    elif len(res) == 2:
        return f'The most published authors are {res[0]} and {res[1]}'
    elif len(res) > 2:
        return f'The most published authors are {res[0]}, {res[1]}, and {res[2]}'

    

def get_author_set(lst):
    author_set = set()
    for i in range(len(lst)):
        author_set.add(lst[i]["author"])
    return author_set

def best_rated_book(lst):
    best_book = "yeet"
    highest_rating = 0
    for i in range(len(lst)):
        if lst[i]["rating"] > highest_rating:
            highest_rating = lst[i]["rating"]
            best_book = lst[i]["title"]
    return f"{best_book}, rating: {highest_rating}"

# print(get_author_set(book_list))
# print(best_rated_book(book_list))
# print(most_published_author(book_list_2))
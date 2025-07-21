library = ["english", "maths", "operating system", "data structures", "machine learning", "programming fundamentals", "programming in cpp","calculus"]
lend_books_data ={}

def display_books():
    with open('demo_file.txt', 'r') as f:
        books = f.readlines()
        if not books:
            print("Books are not available at the moment")
        else:
            for book in books:
                print(f"{book.strip()}")
def add_book():
    with open('demo_file.txt', 'a+') as f:
        book = input("Enter book name: ")
        user = input("Enter your name: ")
        f.write(f"{book}")
        print(f"{book} is added by {user}")
def lend_book():
    global lend_books_data
    book_to_lend = input("Enter book name: ")
    user = input("Enter your name")
    with open('demo_file.txt', 'r') as f:
        books = f.readlines()
        books = [book.strip() for book in books]

    if book_to_lend in books:
            if book_to_lend not in lend_books_data:
                lend_books_data[book_to_lend] = user
                print(f"Book {book_to_lend} has been lend to {user}")
                books.remove(book_to_lend)
                with open('demo_file.txt', 'w') as f:
                    for book in books:
                        f.write(book + '\n')


    else:
        print(f"Sorry {book_to_lend} is not available.{book_to_lend} is already lent.")



def return_book():
    book_to_return = input("Enter the book name: ")
    if book_to_return in lend_books_data:
            del lend_books_data[book_to_return]
            print("Thanks for returning the book")
            with open('demo_file.txt', 'a') as f_a:
                f_a.write(book_to_return + '\n')
    else:
            print(f"{book_to_return} book was not lent out")

while True:
    print("\n LIBRARY BOOKS MENU")
    print("1. Display books")
    print("2. Add  book")
    print("3.Lend  book")
    print("4.Return book ")

    choice = input("Enter your choice(1-5): ")

    match choice:
        case '1':
            display_books()
        case '2':
            add_book()
        case '3':
            lend_book()
        case '4':
            return_book()
            break
        case _:
            print("Invalid option")
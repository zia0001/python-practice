#--------Reading file--------
from os import remove


def read_file_data():
    with open('C:/Users/ziawc/OneDrive/Desktop/file_handling_practice.txt', 'r') as f:
        f_data = f.readlines()
        for data in f_data:
            print(data.strip())

#--------writing to file
def write_to_file():
    user_data = input("write data to file: ")
    with open('C:/Users/ziawc/OneDrive/Desktop/file_handling_practice.txt', 'w') as f:   # overwrite/truncate the file and replace previous data with current added data
        written_data = f.write(user_data + '\n')
        print(f"You overwrite the file with {user_data}")



def append_file():
    data =input("Enter data to add: ")
    with open('C:/Users/ziawc/OneDrive/Desktop/file_handling_practice.txt', 'a+') as f:
        add_data = f.write(data + '\n')
        print(f"You added {data}")

#-------delete from file

def delete_from_file():
    book_name = input("Enter book name: ")
    with open('C:/Users/ziawc/OneDrive/Desktop/file_handling_practice.txt', 'r') as f:
        books = f.readlines()

    books = [book.strip() for book in books]
    if book_name not in books:
            print("Sorry this book is not availabe in library")
    else:

        books.remove(book_name)
        # Write updated list back to the file
        with open('C:/Users/ziawc/OneDrive/Desktop/file_handling_practice.txt', 'w') as f:
            for book in books:
                    f.write(book + '\n')
    print(f"{book_name} successfully deleted from library")


# append_file()
read_file_data()
# delete_from_file()
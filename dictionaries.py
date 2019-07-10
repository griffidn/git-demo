books = {}
books['The Hunger Games'] = 'Susan Collins'
books['Harry Potter'] = 'J K Rowling'
books['Lord of the Rings'] = 'Tolkien'

for book, author in books.items():
    print("Author of {} is {}".format(book, author))

if 'Harry Potter' in books:
    if books['Harry Potter'] == 'J K Rowling':
        print("true")

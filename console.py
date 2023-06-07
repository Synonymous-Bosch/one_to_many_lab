import pdb
from models.author import Author
from models.book import Book

from repositories import author_repo, book_repo

book_repo.delete_all()
author_repo.delete_all()

author1 = Author("Brandon Sanderson")
author_repo.save(author1)
author2 = Author("Joseph Heller")
author_repo.save(author2)

book1 = Book("The Final Empire", author1, "Fantasy")
book_repo.save(book1)
book2 = Book("Catch-22", author2, "War, Comedy, Fiction")
book_repo.save(book2)


# book_results = book_repo.select_all()

# author_results = author_repo.select_all()

# for item in book_results:
#     print(item.__dict__)

# for item in author_results:
#     print(item.__dict__)

# pdb.set_trace()




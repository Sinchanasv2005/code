class library:
    def __init__(self,rows,columns):
        self.rows=rows
        self.columns=columns
        
    def ece_branch(self):
        print(f"{self.rows}  rows are there in the library")
        print(f"{self.columns}  columns are there in the library")
        
class book(library):
    def __init__(self,name,author):
        self.name=name
        self.author=author
        self.book_info={
            'title': self.name,
            'author': self.author,
            
        }
    def books(self):
        print(f"{self.book_info['title']} is the book name")
        print(f"{self.book_info['author']} is the author of that book")
a=library('5','3')
a.ece_branch()
b=book("python programming language","Guido van Rossum")
b.books()

    
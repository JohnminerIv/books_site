Create a file in your project’s root folder called README.md. In it, answer the following questions:

How would we filter for all books with titles containing the word ‘Django’?
bset = Book.objects.get(title__contains='Django')

How would we filter for all books with tag ‘Fiction’?

bset = Book.objects.get(tags__name='Fiction')

How would we filter for all authors who have written books containing the word ‘Django’? HINT: We can use the book field to refer to an author’s books, even though the Author model doesn’t explicitly contain it!

aset = Author.objects.get(book__title__contains=‘Django’)


from django.http import HttpResponse


from front.models import Author, Publisher, Book


def index(request):
    author = Author(author_name='GL', author_email='123@163.com', author_phone='147852369')
    author.save()
    publish = Publisher(pub_name='江迅奇', pub_email="369@163.com", address='你的心里')
    publish.save()
    return HttpResponse('index')


# 增
def insert(request):
    book = Book(book_name="欧若拉", price="25.6")
    author = Author.objects.first()
    publisher = Publisher.objects.first()
    book.author = author
    book.publisher = publisher
    book.save()
    return HttpResponse('success')


# 删
def delete(request):
    books = Book.objects.filter(book_id=1)
    books.delete()
    return HttpResponse("删除成功")
# 改
def update(request):
    books = Book.objects.get(book_id=2)
    books.book_name = "姐姐出嫁"
    books.save()
    return HttpResponse("修改成功")

# 查
def find(request):
    author = Author.objects.first()
    books = author.book_set.all()
    for book in books:
        print(book)
    return HttpResponse('success')


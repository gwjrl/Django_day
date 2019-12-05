from django.db import models


# 创建数据库
class Book(models.Model):
    book_id = models.AutoField(primary_key=True, null=False)
    book_name = models.CharField(max_length=200, unique=True, null=False)
    author = models.ForeignKey(to="Author", on_delete=models.CASCADE, null=True)
    price = models.FloatField(null=False, default=0)
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "(Book:(book_id:%s, book_name:%s, price:%s)" % (self.book_id, self.book_name, self.price)


class Publisher(models.Model):
    pub_name = models.CharField(primary_key=True, unique=True, max_length=200, null=False)
    address = models.CharField(max_length=200, null=False)
    pub_email = models.EmailField(unique=True)

    def __str__(self):
        return "(Publisher:(pub_name:%s, address:%s, pub_email:%s)" % (self.pub_name, self.address, self.pub_email)


class Author(models.Model):
    author_name = models.CharField(max_length=200, primary_key=True, unique=True, null=False)
    author_email = models.EmailField(unique=True)
    author_phone = models.CharField(max_length=200, null=False)

    def __str__(self):
        return "(Author:(author_name:%s, author_email:%s, author_phone:%s)" % (self.author_name, self.author_email, self.author_phone)



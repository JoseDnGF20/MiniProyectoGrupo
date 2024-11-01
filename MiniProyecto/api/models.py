from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class Category(models.Model):  # Model for categories
    category_name = models.CharField(max_length=100)
    category_id = models.CharField(max_length=100)

    def _str_(self): 
        return self.category_name
    
class Author(models.Model):  # Model for authors
    author_name = models.CharField(max_length=100)
    author_last_name = models.CharField(max_length=100)
    author_review = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.author_name} {self.author_last_name}"
    
class Editorial(models.Model):  # Model for editorial
    editorial_name = models.CharField(max_length=100)

    def _str_(self):
        return self.editorial_name
    
class Book(models.Model):  # Model for books
    book_title = models.CharField(max_length=100)
    book_year = models.DateField()  # Use DateField instead of DateTimeField
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Change field names to be more Django-conventional
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    
    def _str_(self):
        return self.book_title
    

    
    
class TypeClient(models.Model):  # Model for types of clients
    type_client = models.CharField(max_length=100)

    def _str_(self):
        return self.type_client
    
class Client(models.Model):  # Model for clients
    client_name = models.CharField(max_length=100,unique=True)
    client_last_name = models.CharField(max_length=100,unique=True)
    client_email = models.EmailField(max_length=254,unique=True)
    client_phone = models.PositiveBigIntegerField(unique=True)
    client_id = models.CharField(max_length=100)
    type_client = models.ForeignKey(TypeClient, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.client_name} {self.client_last_name}"
    
class DetailRequest(models.Model):  # Model for request details
    detail_request_type = models.CharField(max_length=100)

    def _str_(self):
        return self.detail_request_type
    
class Request(models.Model):  # Model for requests
    request_date = models.DateField()
    detail_request_type = models.ForeignKey(DetailRequest, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.request_date)
    
class Sale(models.Model):  # Model for sales
    detail_sale_date = models.DateField()
    detail_sale_amount = models.IntegerField()

    def _str_(self):
        return f"Sale on {self.detail_sale_date}"

class DetailSale(models.Model):  # Model for sale details
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)

    def _str_(self):
        return f"Detail of Sale ID: {self.sale.id}"
    
class Inventory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity_available = models.IntegerField()
    
    def _str_(self):
        return f"{self.quantity_available} of {self.book}"
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rating = models.IntegerField() 
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Review for {self.book} by {self.client}"
    
class ClosedDay(models.Model):
    date = models.DateField()
    reason = models.TextField()
    
    def _str_(self):
        return f"{self.date} - {self.reason}"
    
class BookStatistic(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    total_sales = models.IntegerField(default=0)
    total_reservations = models.IntegerField(default=0)
    total_reviews = models.IntegerField(default=0)
    
    def _str_(self):
        return str(self.book)
    
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_at = models.DateField(auto_now_add=True)
    
    def _str_(self):
        return self.title




from rest_framework import generics
from .models import Category, Author, Editorial, Books, Type_Client, Client, Detail_Request, Request, Detail_Sale, Sale, Inventory, Review, ClosedDay, BookStatistic, BlogPost
from .serializers import CategorySerializer, AuthorSerializer, EditorialSerializer, BooksSerializer, Type_ClientSerializer, ClientSerializer, Detail_RequestSerializer, RequestSerializer, Detail_SaleSerializer, SaleSerializer, InventorySerializer, ReviewSerializer, ClosedDaySerializer,BookStatisticSerializer, BlogPostSerializer

#Categoria
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#CategoryDetail es el put y delete de categoria
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

##################################################################

#Author

class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


##################################################################

#Editorial

class EditorialListCreate(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    
class EditorialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

##################################################################

#Books

class BooksListCreate(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class BooksDetial(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    
##################################################################

#Type_Cliente

class Type_ClientListCreate(generics.ListCreateAPIView):
    queryset = Type_Client.objects.all()
    serializer_class = Type_ClientSerializer

class Type_ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type_Client.objects.all()
    serializer_class = Type_ClientSerializer

##################################################################

#Client

class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

##################################################################

#Detail_Request

class Detail_RequestListCreate(generics.ListCreateAPIView):
    queryset = Detail_Request.objects.all()
    serializer_class = Detail_Request

class Detail_RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detail_Request.objects.all()
    serializer_class = Detail_Request

##################################################################

#Request

class RequestListCreate(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = Request
    
class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = Request

##################################################################

#Detail_Sale

class Detail_SaleListCreate(generics.ListCreateAPIView):
    queryset = Detail_Sale.objects.all()
    serializer_class = Detail_Sale

class Detail_SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detail_Sale.objects.all()
    serializer_class = Detail_Sale
    
##################################################################

#Detail_Sale

class SaleListCreate(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = Sale

class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = Sale

##################################################################

#Inventary 

class InventorytListCreate(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    InventorySerializer = Inventory

class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    InventorySerializer = Inventory


##################################################################

#Review

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    ReviewSerializer = Review

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    ReviewSerializer = Review
    
##################################################################

#ClosedDay

class ClosedDayListCreate(generics.ListCreateAPIView):
    queryset = ClosedDay.all()
    ClosedDaySerializer = ClosedDay

class ClosedDayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClosedDay.objects.all()
    ClosedDaySerializer = ClosedDay
    
##################################################################

#BookStatistic

class BookStatisticListCreate(generics.ListCreateAPIView):
    queryset = BookStatistic.all()
    BookStatisticSerializer = BookStatistic

class ClosedDayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookStatistic.objects.all()
    BookStatisticSerializer = BookStatistic
    
##################################################################

#BlogPost

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.all()
    BlogPostSerializer = BlogPost

class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    BlogPostSerializer = BlogPost
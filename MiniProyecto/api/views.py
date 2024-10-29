from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated


from rest_framework import generics
from .models import Category, Author, Editorial, Book, TypeClient, Client, DetailRequest, Request, DetailSale, Sale, Inventory, Review, ClosedDay, BookStatistic, BlogPost
from .serializers import CategorySerializer, AuthorSerializer, EditorialSerializer, BookSerializer, TypeClientSerializer, ClientSerializer, DetailRequestSerializer, RequestSerializer, DetailSaleSerializer, SaleSerializer, InventorySerializer, ReviewSerializer, ClosedDaySerializer,BookStatisticSerializer, BlogPostSerializer

#Categoria
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#CategoryDetail es el put y delete de categoria
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes= [IsAuthenticated]

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

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
##################################################################

#Type_Cliente

class TypeClientListCreate(generics.ListCreateAPIView):
    queryset = TypeClient.objects.all()
    serializer_class = TypeClientSerializer

class TypeClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeClient.objects.all()
    serializer_class = TypeClientSerializer

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

class DetailRequestListCreate(generics.ListCreateAPIView):
    queryset = DetailRequest.objects.all()
    serializer_class = DetailRequestSerializer

class DetailRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetailRequest.objects.all()
    serializer_class = DetailRequestSerializer

##################################################################

#Request

class RequestListCreate(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    
class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

##################################################################

#Detail_Sale

class DetailSaleListCreate(generics.ListCreateAPIView):
    queryset = DetailSale.objects.all()
    serializer_class = DetailSaleSerializer

class DetailSaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetailSale.objects.all()
    serializer_class = DetailSaleSerializer
##################################################################

#Detail_Sale

class SaleListCreate(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

##################################################################

#Inventary 

class InventoryListCreate(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class= InventorySerializer

class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class=InventorySerializer 


##################################################################

#Review

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class=ReviewSerializer 

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class=ReviewSerializer 
    
##################################################################

#ClosedDay

class ClosedDayListCreate(generics.ListCreateAPIView):
    queryset = ClosedDay.objects.all()
    serializer_class=ClosedDaySerializer

class ClosedDayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClosedDay.objects.all()
    serializer_class=ClosedDaySerializer 
    
##################################################################

#BookStatistic

class BookStatisticListCreate(generics.ListCreateAPIView):
    queryset = BookStatistic.objects.all()
    serializer_class=BookStatisticSerializer 

class BookStatisticDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookStatistic.objects.all()
    serializer_class=BookStatisticSerializer 
    
##################################################################

#BlogPost

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class=BlogPostSerializer 


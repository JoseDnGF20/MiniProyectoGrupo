from rest_framework import serializers
from .models import Category, Author, Editorial, Books, Type_Client, Client, Detail_Request, Request, Detail_Sale, Sale, Inventory, Review, ClosedDay, BookStatistic, BlogPost

# cada serializer usado convierte el modelo en un formato como JSON para la API
# y convierte datos de entrada a objetos de django para guardarlos en la base de datos

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' # usa todos los campos del modelo

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class TypeClient_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Type_Client
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class Detail_RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail_Request
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class Detail_SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail_Sale
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory  
        fields = '__all__'  

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review 
        fields = '__all__'  

class ClosedDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosedDay  
        fields = '__all__' 

class BookStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStatistic 
        fields = '__all__'  

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost 
        fields = '__all__'  
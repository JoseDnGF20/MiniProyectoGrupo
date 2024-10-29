from django.urls import path
from . import views 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('/client', views.ClientListCreate.as_view(), name='Client-List'),
    path('/clients/<int:pk>', views.ClientDetail.as_view(), name= 'Client-Detail'),
    
    path('/typeclient', views.TypeClientListCreate.as_view(), name='Type_Client-List'),
    path('/typeclient/<int:pk>', views.TypeClienteDetail.as_view(), name='Type_Client-Detail'),
    
    path('/category',views.CategoryListCreate.as_view(), name='Category-List'),
    path('/category/<int:pk>', views.CategoryDetail.as_view(), name='Category-Detail'),
    
    path('/author', views.AuthorListCreate.as_view(), name='Author-List'),
    path('author/<int:pk>', views.AuthorDetail.as_view(), name='Author_Detail'),
    
    path('/book', views.BookListCreate.as_view(), name='Book-List'),
    path('/Book/int:pk>', views.BookDetail.as_view(), name='Book_Detail'),
    
    path('/detailrequest', views.DetailRequestListCreate.as_view(), name='Detail_request-List'),
    path('/detailrequest/<int:pk>', views.DetailRequestDetail.as_view(), name='detail_request-Detail'),
    
    path('/editorial', views.EditorialListCreate.as_view(), name='Editorial-List'),
    path('/editorial/<int:pk>', views.EditorialDetail.as_view(), name='Editorial-Detail'),
    
    path('/detailsale', views.DetailSaleListCreate.as_view(), name='Detail_sale-List'),
    path('/detailsale/<int:pk>', views.DetailSaleDetail.as_view(), name='Detail_sale-Detail'),
    
    path('/blogpost', views.BlogPostListCreate.as_view(), name='BlogPost-List'),
    path('blogpost/<int:pk>', views.BlogPostDetail.as_view(), name='BlogPost-Detail'),
    
    path('/inventory', views.InventoryListCreate.as_view(), name='Inventory-List'),
    path('/inventory/<int:pk>', views.InventoryListCreate.as_view(), name='Inventory-Detail'),
    
    path('/review',views.ReviewListCreate.as_view(), name='Review-List'),
    path('/review/<int:pk>', views.ReviewDetail.as_view(), name='Review-Detail'),
    
    path('/closeday', views.ClosedDayListCreate.as_view(), name='ClosedDay-List'),
    path('/closedday/<int:pk>', views.ClosedDayDetail.as_view(), name='ClosedDay-Detail'),
    
    path('/request', views.RequestListCreate.as_view(), name='Request-List'),
    path('/request/<int:pk>', views.RequestDetail.as_view(), name='Request-Detail'),
    
    path('/sale', views.SaleListCreate.as_view(), name='Sale'),
    path('/sale/<int:pk>', views.SaleDetail.as_view(), name='Sale-Detail'),
    
    path('/bookstatistic', views.BookStatisticListCreate.as_view(), name='BookStatistic'),
    path('/bookstatistic/<int:pk>', views.BookStatisticDetail.as_view(), name='BookStatistic-Detail'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', TokenRefreshView.as_view(), name='token_refresh')

]

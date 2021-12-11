from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('quotes/', views.quotes_index, name='index'),
    path('quotes/<int:quote_id>/', views.quotes_detail,name='detail'),
    path('quotes/new/', views.QuoteCreate.as_view(), name='create'),
    path('quotes/<int:pk>/update', views.QuoteUpdate.as_view(), name='quote_update'),
    path('quotes/<int:pk>/delete', views.QuoteDelete.as_view(), name='quote_delete'),
    path('quotes/<int:quote_id>/add_fan/', views.add_fan, name='add_fan'),
    path('quotes/<int:quote_id>/assoc_cat/<int:cat_id>/', views.assoc_cat, name='assoc_cat'),
    path('categories/', views.CatList.as_view(), name='cat_list'),
    path('categories/<int:pk>/', views.CatDetail.as_view(), name='cat_detail'),
    path('categories/create/', views.CatCreate.as_view(), name='cat_create')

]
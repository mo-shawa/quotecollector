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
]
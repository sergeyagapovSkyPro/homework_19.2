from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (ContactsTemplateView, HomeListView, ProductDetailView, ProductDeleteView, ProductCreateView,
                           ProductUpdateView)

app_name = 'catalog'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('catalog/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_view'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('category/<int:category_id>', HomeListView.as_view(), name='category')
]

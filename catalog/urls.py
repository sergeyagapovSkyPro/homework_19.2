from django.urls import path
from catalog.views import ContactsTemplateView, HomeListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('catalog/<int:pk>', ProductDetailView.as_view(), name='product_view')
]

from django.urls import path

from catalog.views import home, contacts
from catalog.apps import CatalogConfig

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]

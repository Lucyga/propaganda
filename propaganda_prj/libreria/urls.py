from django.urls import path
from .views import libreria, LibroDetailView, AutoriDetailView, GeneriDetailView, LibroListView, AutoriListView, EditoriDetailView, EditoriListView, GeneriListView

# from news.views import home

urlpatterns = [
    path('', libreria, name='libreria_view'),
    path('libro/<int:pk>', LibroDetailView.as_view(), name='libro_detail'),
    path('autori/<int:pk>', AutoriDetailView.as_view(), name='autori_detail'),
    path('editori/<int:pk>', EditoriDetailView.as_view(), name='editori_detail'),
    path('genere/<int:pk>', GeneriDetailView.as_view(), name='genere_detail'),
    path('libri/', LibroListView.as_view(), name='libri_list'),
    path('autori/', AutoriListView.as_view(), name='autori_list'),
    path('editori/', EditoriListView.as_view(), name='editori_list'),
    path('generi/', GeneriListView.as_view(), name='generi_list'),

]

from django.urls import path, include
from .views import registrazione

urlpatterns = [
    path('registrazione/', registrazione, name='registrazione'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

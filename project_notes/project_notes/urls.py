
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

#Manejo global de las url's, de la aplicación, login, admin y para redireccionar
urlpatterns = [
    path('', RedirectView.as_view(url='mynotes/', permanent=True)),
    path('mynotes/', include('mynotes.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))
]
from django.urls import path
from .views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', home, name="home"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


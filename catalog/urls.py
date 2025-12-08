# my_shop/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # ваши другие URL
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# catalog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
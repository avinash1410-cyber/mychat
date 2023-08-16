from django.contrib import admin
from django.urls import path, include



from django.urls import include, path, re_path
from django.views.static import serve

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
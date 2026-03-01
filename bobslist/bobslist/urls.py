

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from .settings import MEDIA_ROOT
from .settings import MEDIA_URL
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include('users.urls')),
    path("users/", include('django.contrib.auth.urls')),
    path("", include('pages.urls')),
    path("items/", include("items.urls"))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
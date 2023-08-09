from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Travel Site"
admin.site.site_title = "Travel Site Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('home.urls')),
    path("account/", include('account.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,
                                   document_root=settings.MEDIA_ROOT)

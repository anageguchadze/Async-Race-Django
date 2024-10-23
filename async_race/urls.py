# race_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('race_app.urls')),  # API URLs under /api/
    path('', include('race_app.urls')),  # Include for HTML pages, but usually good to separate
]

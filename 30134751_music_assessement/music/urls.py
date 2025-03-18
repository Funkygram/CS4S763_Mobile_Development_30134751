from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('api/')),  # Redirects root to /api/
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]

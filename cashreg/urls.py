from django.contrib import admin
from django.urls import path
from pos.views import scan_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scan_view, name='scan'),
]

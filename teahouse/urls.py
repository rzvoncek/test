from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
]

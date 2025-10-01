from django.contrib import admin
from django.urls import path
from api.views import home,fbv_crud

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('api/',fbv_crud),
    path('api/<int:pk>/',fbv_crud),
]

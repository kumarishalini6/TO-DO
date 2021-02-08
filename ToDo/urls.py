from django.contrib import admin
from django.urls import path
from .views import index, update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('update_task/<int:id>', update, name='edit'),
    path('delete_task/<int:id>', delete, name='del')
]

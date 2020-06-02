
from django.contrib import admin
from django.urls import path, include
from ToDoList import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ToDoList.urls")),

]

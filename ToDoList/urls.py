from django.urls import path, include
from django.contrib  import admin

from . import views

urlpatterns = [

    path("", views.home, name="home"),
    path("add_item/", views.add_item),
    path("delete_item/<int:item_id>/", views.delete_item),

]
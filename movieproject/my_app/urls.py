from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create,name="create"),
    path('edit/<pk>',views.edit,name="edit"),
    path('delete/<pk>',views.delete,name="delete"),
    path('list/',views.list,name="list"),

    path('blanklayout/',views.list,name='blanklayout')
]
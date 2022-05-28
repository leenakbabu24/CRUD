from django .urls import path
from .import views
from django.conf.urls import url
urlpatterns=[
    path('',views.home,name='home'),
    path('create',views.create,name='create'),
    path('read',views.read,name='read'),
    path('update/<int:id>',views.update,name="update"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('delete/(?P<pk>[0-9]+)/$', views.delete,name="delete"),
]
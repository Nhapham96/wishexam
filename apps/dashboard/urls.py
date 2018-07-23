from django.conf.urls import url
from.import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^logout$',views.logout, name='logout'),
    url(r'^/remove$',views.remove, name='remove'),
    url(r'^/add$',views.add, name='add'),
    url(r'^/delete$',views.delete, name='delete'),
    url(r'^/additem$',views.additem, name='add_item'),
    url(r'^/create$',views.create, name='create'),
    url(r'^/info/(?P<id>\d+)$',views.info, name='info'),
]
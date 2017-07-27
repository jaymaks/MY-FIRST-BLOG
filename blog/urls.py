from django.conf.urls import url
from . import views

viewsurlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]

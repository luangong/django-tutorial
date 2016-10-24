from django.conf.urls import url
from . import views

urlpatterns = [
    # e.g.: /polls/
    url(r'^$', views.index, name='index'),
]

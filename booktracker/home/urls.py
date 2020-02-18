from django.conf.urls import url
from home.views import HomeView
from . import views



urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^mybooks/$', views.my_books, name='my_books'),
]
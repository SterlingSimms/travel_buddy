from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.main),
    url(r'^schedule$', views.schedule),
    url(r'^add_trip$', views.add_trip),
    url(r'^description$', views.description),
    url(r'^login$', views.login),
]
""" Defines URL patterns for learning_logs """

from django.conf.urls import url

from . import views

app_name = 'll_app_name'

urlpatterns = [
    # Home page
    url('^$', views.index, name='index')
]

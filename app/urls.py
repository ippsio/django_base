from django.conf.urls import include, url

from app.views.test_api import test_api_view

urlpatterns = [
    url(r'^test/$', test_api_view, name='test'),
]
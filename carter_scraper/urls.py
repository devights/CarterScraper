from django.conf.urls import patterns,url
from carter_scraper.views import test_view

urlpatterns = patterns('',
    url(r'test/', test_view),
)

from django.conf.urls import patterns, include, url
from app.views import detect_dom_change

urlpatterns = [
    url(r'^dom/change-detect/$', detect_dom_change, name='dom-change-detect'),
]

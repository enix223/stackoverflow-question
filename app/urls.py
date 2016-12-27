from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'(?P<token>[-_:a-zA-Z0-9]+)/$', 'app.views.webhook', name='api_webhook'),
]

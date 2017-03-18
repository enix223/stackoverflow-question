from django.conf.urls import include, url
from app.views import BookUpdateView, BookPartialUpdateView
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from app.views import ConsoleView, LoginView, login_view
from django.contrib.auth.decorators import login_required


# urlpatterns = patterns(
#     '',
#     url(r'^login/$', LoginView.as_view(), name='login'),
#     url(r'^(?P<username>[0-9a-zA-Z._]+)/$', ConsoleView.as_view(), name='index'),
# )
app_name = 'accounts'

urlpatterns = [

    url(r'^login/', login_view, name='login'),
    url(r'^logout/', login_view, name='logout'),
    url(r'^register/', login_view, name='register'),
    url(r'^(?P<username>[0-9a-zA-Z._]+)/$', login_required(ConsoleView.as_view()), name='index'),

    # url(r'^login/', login_view, name='login'),
    # url(r'^logout/', logout_view, name='logout'),
    # url(r'^register/', register_view, name='register'),
    # url(r'^(?P<username>[0-9a-zA-Z._]+)/$', login_required(ConsoleView.as_view()), name='index'),
    # url(r'^(?P<username>[0-9a-zA-Z._]+)/$', ConsoleView.as_view(), name='index'),
]

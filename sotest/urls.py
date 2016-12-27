from django.conf.urls import patterns, include, url
from app.views import BookUpdateView, BookPartialUpdateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sotest.views.home', name='home'),
    # url(r'^sotest/', include('sotest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', 'app.views.test', name='test'),
    url(r'^multi/$', 'app.views.multi', name='multi'),

    url(r'^book/update/(?P<pk>\d+)/$', BookUpdateView.as_view(), name='book_update'),
    url(r'^book/update-partial/(?P<pk>\d+)/$', BookPartialUpdateView.as_view(), name='book_partial_update'),
    url(r'^webhook/', include('app.urls', namespace='api_webhook'), name='webhook'),
)

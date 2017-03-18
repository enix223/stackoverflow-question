from django.conf.urls import include, url
from app.views import BookUpdateView, BookPartialUpdateView
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from app.views import test, multi, ImageViewSet

from rest_framework.routers import DefaultRouter

admin.autodiscover()

app_name = "pto_request"

urlpatterns = [
    # Examples:
    # url(r'^$', 'sotest.views.home', name='home'),
    # url(r'^sotest/', include('sotest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', test, name='test'),
    url(r'^multi/$', multi, name='multi'),

    url(r'^accounts/', include('app.accounts_urls')),

    url(r'^book/update/(?P<pk>\d+)/$', BookUpdateView.as_view(), name='book_update'),
    url(r'^book/update-partial/(?P<pk>\d+)/$', BookPartialUpdateView.as_view(), name='book_partial_update'),

    # url(r'^app/', include('app.urls', namespace='api_webhook'), name='webhook'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Register viewset
router = DefaultRouter()
router.register(r'image', ImageViewSet)
urlpatterns += router.urls

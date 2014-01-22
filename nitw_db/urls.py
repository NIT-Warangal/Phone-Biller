from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from search import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nitw_db.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('search.urls', namespace='search')),
    url(r'^$', include('search.urls', namespace='search'))
) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

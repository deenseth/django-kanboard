from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('kanboard.views',
   url(r'^board/(?P<board_slug>[\w-]+)/$', 'board'),
   url(r'^board/(?P<board_slug>[\w-]+)/update/$', 'update'),
)


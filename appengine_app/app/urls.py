from django.conf.urls.defaults import url, patterns, include
#from django.contrib import admin
#admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns(
    '',
    url(r'^_ah/warmup$', 'djangoappengine.views.warmup'),
    #(r'^adminenter/', include(admin.site.urls)),

    url(r'^$', 'app.views.index', name='index'),
    url(r'^agenda/$', 'app.views.agenda', name='agenda'),
    url(r'^location/$', 'app.views.location', name='location'),
    url(r'^speakers/$', 'app.views.speakers', name='speakers'),
    url(r'^openhackday/$', 'app.views.openhackday', name='openhackday'),
    url(r'^techtalks/$', 'app.views.techtalks', name='techtalks'),
    url(r'^team/$', 'app.views.team', name='team'),
    url(r'^registration/$', 'app.views.registration', name='registration'),
    url(r'^workshops/$', 'app.views.workshops', name='workshops'),
)

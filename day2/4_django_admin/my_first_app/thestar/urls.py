from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    # Examples:
    url(r'^vote/', 'thestar.views.vote', name='vote'),

)
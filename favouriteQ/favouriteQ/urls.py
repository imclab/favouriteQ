from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'questions.views.current_question'),
    url(r'^ajax_suggest$', 'questions.views.ajax_suggest'),
    url(r'^archive$', 'questions.views.archive'),
    url(r'^archive/(?P<slug>[-\w]+)$', 'questions.views.detail'),
)

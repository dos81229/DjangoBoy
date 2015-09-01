from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #管理後台的 URL，將管理後台的網址設定為 /admin/
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^hello/$', 'trips.views.hello_world'),
    url(r'^$', 'trips.views.home'),
    url(r'^post/(?P<id>\d+)/$', 'trips.views.post_detail', name='post_detail'),
	url(r'^message/$','trips.views.message'),

	url(r'^menu/(?P<id>\d+)/$', 'trips.views.menu'),
	#url(r'^menu_detail/(?P<id>\d+)/$', 'trips.views.menu_detail', name='menu_detail'),

    url(r'^welcome/$', 'trips.views.welcome'),
    url(r'^restaurants/$', 'trips.views.restaurants_list'),
    url(r'^comment/(?P<id>\d+)/$', 'trips.views.comment'),

    url(r'^index/$',  'trips.views.index'),
    url(r'^accounts/login/$',  'trips.views.login'),
    url(r'^accounts/auth/$',  'trips.views.auth_view'),
    url(r'^accounts/loggedin/$', 'trips.views.loggedin'),
    url(r'^accounts/invalid/$', 'trips.views.invalid_login'),
    url(r'^accounts/logout/$', 'trips.views.logout'),
    url(r'^accounts/register/$', 'trips.views.register'),
    url(r'^accounts/register_success/$', 'trips.views.register_success'),
    url(r'^accounts/register_invalid/$', 'trips.views.register_invalid'),

    url(r'^contact/$','trips.views.contact'),

    url(r'^bands/$', 'trips.views.band'),
    url(r'^band_menu/(?P<id>\d+)/$', 'trips.views.band_menu'),
    url(r'^music_comment/(?P<id>\d+)/$', 'trips.views.music_comment'),
    url(r'^random_string/$', 'trips.tests.random_string'),
    url(r'^bitch_face/$', 'trips.views.bitch_face'),
)

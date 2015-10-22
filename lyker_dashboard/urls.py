from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user, name = 'user'),
    url(r'^object/(?P<object_id>[0-9]+)/$', views.object, name = 'object'),
    url(r'^customer/(?P<customer_id>[0-9]+)/$', views.customer, name = 'customer'),
    url(r'^video/(?P<video_id>[0-9]+)/$', views.video, name = 'video'),
    ]

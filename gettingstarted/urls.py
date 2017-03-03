from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

#URLconfiguration
#url(tarting with a URL requested by the user/browser, used method,  name of url pattern)
urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^orderHistory', hello.views.getAllOrders, name='orderHistory'),
    url(r'^checkout/(?P<id>\d+)/$', hello.views.checkout, name='checkout'),
    url(r'^admin/', include(admin.site.urls)),
]

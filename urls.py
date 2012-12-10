from django.conf.urls.defaults import *
from mysite.views import hello, registro, registrado

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^registro/$', registro),
    ('^registro/registrado/$', registrado),
)

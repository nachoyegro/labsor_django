from django.conf.urls.defaults import *
from mysite.views import hello
from registro.views import registro, registrado, form_info_usuario, datos_usuario

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^registro/$', registro),
    ('^registrado/$', registrado),
    ('^form_info_usuario/$', form_info_usuario),
    ('^datos_usuario/$', datos_usuario)

)

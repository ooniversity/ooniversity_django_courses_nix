from django.conf.urls import include, url
from django.contrib import admin
from pybursa.views import index, student_list, student_detail, contact

urlpatterns = [
    url(r'^$', index),
    url(r'^contact/$', contact),
    url(r'^student_list/$', student_list),
    url(r'^student_detail/$', student_detail),

    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
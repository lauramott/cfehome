from django.conf.urls import url, include

from django.views.generic import TemplateView
from django.contrib import admin

from django.contrib.auth.views import LoginView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]


urlpatterns += [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^u/', include('profiles.urls', namespace='profiles')),
    url(r'^items/', include('facescan.urls', namespace='facescan')),
    url(r'^contact/', include('menu.urls', namespace='menu')),
    url(r'^myprofile/$', TemplateView.as_view(template_name='myprofile.html'), name='myprofile'),
    url(r'^recognition/$', TemplateView.as_view(template_name='recognition.html'), name='recognition'),
]

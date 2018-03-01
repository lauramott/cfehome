from django.conf.urls import url, include

from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView

from profiles.views import RegisterView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
]


urlpatterns += [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^u/', include('profiles.urls', namespace='profiles')),
    url(r'^items/', include('facescan.urls', namespace='facescan')),
    url(r'^contact/', include('menu.urls', namespace='menu')),
    url(r'^myprofile/$', TemplateView.as_view(template_name='myprofile.html'), name='myprofile'),
    url(r'^recognition/$', TemplateView.as_view(template_name='recognition.html'), name='recognition'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
